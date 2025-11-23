#!/usr/bin/env python3
"""PDF Page Splitter - Simple Version"""

import sys
from pathlib import Path
import fitz

def split_pdf(pdf_path, pages=None):
    """Split PDF pages to images"""
    output_dir = Path("temp_pages")
    output_dir.mkdir(exist_ok=True)
    
    with fitz.open(pdf_path) as doc:
        total = len(doc)
        target = pages if pages else list(range(1, total + 1))
        
        print(f"Splitting {len(target)}/{total} pages...")
        
        for page_num in target:
            page = doc[page_num - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            output = output_dir / f"page_{page_num:03d}.png"
            pix.save(str(output))
            print(f"Saved: {output}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_splitter.py <pdf_file> [pages]")
        print("Example: python pdf_splitter.py file.pdf 1,2,3")
        return
    
    pdf_file = sys.argv[1]
    pages = None
    
    if len(sys.argv) > 2:
        try:
            pages = [int(p.strip()) for p in sys.argv[2].split(',')]
        except:
            print("Invalid page numbers")
            return
    
    split_pdf(pdf_file, pages)

if __name__ == "__main__":
    main()
