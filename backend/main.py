# backend/main.py
import os
import argparse
from extract_outline import extract_outline_from_pdf
from semantic_ranker import SemanticRanker
from output_generator import generate_output

def main(pdf_dir, persona, job, model_path, output_path):
    all_sections = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            print(f"🔍 Parsing {filename}")
            sections = extract_outline_from_pdf(pdf_path)
            for sec in sections:
                sec["source"] = filename
            all_sections.extend(sections)

    if not all_sections:
        print("⚠️ No valid sections extracted.")
        return

    query = f"{persona}: {job}"
    ranker = SemanticRanker(model_path)
    ranked = ranker.rank_sections(query, all_sections)

    generate_output(persona, job, ranked, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_dir", required=True)
    parser.add_argument("--persona", required=True)
    parser.add_argument("--job", required=True)
    parser.add_argument("--model_path", default="./model")
    parser.add_argument("--output_path", default="output.json")
    args = parser.parse_args()

    main(args.pdf_dir, args.persona, args.job, args.model_path, args.output_path)
