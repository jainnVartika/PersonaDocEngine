# backend/extract_outline.py
import pdfplumber
import os

def extract_outline_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found")

    sections = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) > 10:
                    sections.append({
                        "title": line[:100],
                        "content": line,
                        "page": i + 1
                    })
    return sections
