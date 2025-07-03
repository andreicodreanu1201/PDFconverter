import PyPDF2
import os
import re

# Natural sorting helper
def natural_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

merger = PyPDF2.PdfMerger()

# Get and sort PDFs naturally
pdf_files = sorted(
    [f for f in os.listdir(os.curdir) if f.lower().endswith('.pdf')],
    key=natural_key
)

# Append PDFs in correct order
for file in pdf_files:
    print(f'Found PDF: {file}')
    try:
        merger.append(file, import_outline=False)
    except Exception as e:
        print(f"Error appending {file}: {e}")

# Write output
merger.write('combined.pdf')
merger.close()
