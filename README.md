# Adobe Hackathon – Round 1B: Persona-Driven Document Intelligence

## 🔍 Goal
Extract the most relevant sections from a collection of PDFs based on a specific persona and their job-to-be-done.

## 🧠 Inputs
- PDFs placed in `/backend/input/`
- `persona_job.json` with persona & job description

## ✅ Outputs
- `challenge1b_output.json` in `/backend/output/`

## 🐳 Run Using Docker

```bash
docker build -t insightpdf-persona:vartika1b backend/
docker run --rm -v ${PWD}/backend/input:/app/input -v ${PWD}/backend/output:/app/output --network none insightpdf-persona:vartika1b
