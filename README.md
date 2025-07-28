# Persona-Driven Document Intelligence Engine

## 📘 Overview

This project, `persona-doc-engine`, extracts and ranks semantically relevant sections from a collection of research PDFs based on a specified persona and their job-to-be-done. It's designed to run fully offline, making it suitable for secure environments.

---

## 📁 Project Structure

persona-doc-engine/
├── backend/
│ ├── pdfs/ # Input PDFs
│ ├── output/ # Output JSON
│ ├── extract_outline.py # Extracts title/headings
│ ├── semantic_ranker.py # Performs semantic similarity scoring
│ ├── output_generator.py # Generates ranked JSON
│ ├── pdf_utils.py # Helper functions for parsing
│ ├── main.py # Entry script
│ ├── persona_job.json # Persona & job input
│ ├── approach_explanation.md # Hackathon explanation
├── model/
│ └── all-MiniLM-L6-v2/ # Pre-downloaded model (HuggingFace format)
├── wheels/ # Local .whl dependencies
├── run.sh # Shell script to run everything
├── Dockerfile # Dockerized setup
├── requirements.txt
├── README.md

yaml
Copy
Edit

---

## ⚙️ How to Run

### 🔹 Option 1: Python (Offline)

> Pre-req: Python 3.13, model and `.whl` dependencies already downloaded.

```bash
cd backend
python main.py --persona_file persona_job.json --input_dir pdfs/ --output_dir output/
🔹 Option 2: Docker (If buildable)
bash
Copy
Edit
docker build -t persona-doc-engine .
docker run -v $(pwd)/backend:/app/backend persona-doc-engine
🧠 Features
Offline-compatible (no internet dependency)

Pretrained Transformers model for ranking section relevance

Persona-aware output with ranked sections and metadata

Configurable output size, section length threshold, and title-match weighting

📦 Output Format
Located in backend/output/challenge1b_output.json, the output includes:

json
Copy
Edit
{
  "pdf_name": "gnn_review_1.pdf",
  "matched_sections": [
    {
      "title": "Introduction to GNNs",
      "content": "Graph Neural Networks (GNNs) are ...",
      "score": 0.8745,
      "page_number": 2
    },
    ...
  ]
}
🔧 Tech Stack
Python 3.13

scikit-learn, numpy, pdfplumber

Installed offline via .whl files in wheels/

👤 Author
Vartika Jain
GitHub: [your-profile-link]
Email: [your-email@example.com]
