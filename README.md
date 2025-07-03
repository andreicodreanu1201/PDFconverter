# PDFconverter
A Python script that combines multiple PDF files into a single document with natural sorting (human-friendly numbered order).

# Features
- Merges all PDF files in the current directory

- Natural sorting of filenames (e.g., "page1.pdf, page2.pdf, page10.pdf" instead of alphabetical "page1.pdf, page10.pdf, page2.pdf")

- Simple error handling for problematic PDF files

- Preserves the content of all PDFs in the output

- Lightweight with minimal dependencies

# Requirements

- Python 3.x

- PyPDF2 library

# Installation

Clone this repository:

bash
git clone https://github.com/andreicodreanu1201/PDFconverter.git  

Install the required dependency:

bash
pip install PyPDF2  

# Usage

Place all PDF files you want to merge in the same directory as the script

Run the script:

bash
python PDFconverter.py  

The merged PDF will be saved as combined.pdf in the same directory

Example
Before:

text
document1.pdf  
document2.pdf  
document10.pdf  
page1.pdf  
page2.pdf  
page10.pdf  
After running:

text
combined.pdf (contains all files in natural order)  
Notes

The script will process all files with .pdf extension in the current directory

Output order: Files are sorted by natural number order in their filenames

The script skips (with error message) any PDF files that can't be read

License
MIT

