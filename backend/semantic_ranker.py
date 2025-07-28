# backend/semantic_ranker.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

class SemanticRanker:
    def __init__(self, model_path: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModel.from_pretrained(model_path)

    def encode(self, texts):
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).numpy()

    def rank_sections(self, persona_query, sections, min_len=30, max_sections=5, title_weight=0.3):
        filtered = [s for s in sections if len(s.get("content", "")) >= min_len]
        if not filtered:
            return []

        persona_vec = self.encode([persona_query])[0]
        section_texts = [s["title"] + ". " + s["content"] for s in filtered]
        section_vecs = self.encode(section_texts)
        sims = cosine_similarity([persona_vec], section_vecs)[0]

        for i, score in enumerate(sims):
            title_match = 1.0 if persona_query.lower() in filtered[i]["title"].lower() else 0.0
            filtered[i]["score"] = float(score + title_weight * title_match)

        return sorted(filtered, key=lambda x: x["score"], reverse=True)[:max_sections]
