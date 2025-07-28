# backend/output_generator.py
import json
import os

def generate_output(persona, job_to_be_done, ranked_sections, output_path):
    output = {
        "persona": persona,
        "job_to_be_done": job_to_be_done,
        "top_sections": ranked_sections
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"✅ Output saved to {output_path}")
