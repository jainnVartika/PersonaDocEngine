# Persona-Driven Document Intelligence – Backend Approach

## Goal:
Extract the most relevant sections from PDF documents tailored to a specific **persona** and their **job-to-be-done**, and output a JSON with section-wise scores and text.

---

## Offline & Efficient Execution:
- Python 3.13 compatible
- Runs entirely offline with no internet access
- Uses `transformers + sklearn` (no `sentence-transformers`)
- Model loaded from local cache
- CPU-only, finishes under 60s for up to 5 PDFs

---

## Methodology:

1. **PDF Parsing (fitz/PyMuPDF)**  
   - Extracts blocks of readable text, page-wise

2. **Section Filtering**
   - Removes too-short or noisy text (<100 characters)

3. **Embedding (Transformers)**
   - `paraphrase-MiniLM-L6-v2` used locally via `transformers`
   - Text embedded using `AutoTokenizer` + `AutoModel`

4. **Relevance Ranking**
   - Compute cosine similarity between query & each section
   - Top `k=5` sections retained per file

5. **Output**
   - JSON containing page numbers, text, and relevance scores

---

## Folder Structure

