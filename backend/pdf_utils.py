import fitz  # PyMuPDF
import re

def extract_sections_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for i, page in enumerate(doc):
        text = page.get_text()
        lines = text.split('\n')

        for line in lines:
            if is_section_heading(line):
                sections.append({
                    "document": pdf_path.split("/")[-1],
                    "page_number": i + 1,
                    "section_title": line.strip(),
                    "text": extract_section_text(page, line),
                })

    return sections

def is_section_heading(text):
    return bool(re.match(r'^([0-9]+\.){1,3}\s+.+', text.strip())) or text.strip().isupper()

def extract_section_text(page, heading_line):
    all_text = page.get_text()
    lines = all_text.split('\n')
    start = lines.index(heading_line) if heading_line in lines else 0
    subsection_text = "\n".join(lines[start:start+5])
    return subsection_text.strip()
