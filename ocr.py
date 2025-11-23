#!/usr/bin/env python3
"""
Typhoon OCR - Optimized Version
สำหรับ OCR ไฟล์ PDF ของคุณ
"""

import os
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
import fitz
from typhoon_ocr import ocr_document
from dotenv import load_dotenv

load_dotenv()

def check_api():
    """ตรวจสอบ API key"""
    key = os.getenv('TYPHOON_OCR_API_KEY') or os.getenv('OPENAI_API_KEY')
    if not key:
        print("❌ No API key! Add to .env: TYPHOON_OCR_API_KEY=your_key")
        return False
    print("✅ API ready")
    return True

def ocr_pdf(pdf_path, pages=None):
    """OCR PDF file"""
    if not check_api():
        return
    
    with fitz.open(pdf_path) as doc:
        total = len(doc)
        target = pages if pages else list(range(1, total + 1))
        
        print(f"📄 Processing {len(target)}/{total} pages")
        results = []
        
        for page in tqdm(target):
            try:
                content = ocr_document(str(pdf_path))
                results.append({"page": page, "content": content, "ok": True})
            except Exception as e:
                print(f"❌ Page {page}: {e}")
                results.append({"page": page, "error": str(e), "ok": False})
        
        save_results(pdf_path, results)
        success = sum(1 for r in results if r['ok'])
        print(f"✅ Done: {success}/{len(target)} pages")

def save_results(pdf_path, results):
    """Save results"""
    Path("output").mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = Path(f"output/ocr_{timestamp}.md")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(f"# OCR Results\n\n**File:** {Path(pdf_path).name}\n**Date:** {datetime.now()}\n\n---\n\n")
        
        for r in results:
            if r['ok']:
                f.write(f"## Page {r['page']}\n\n{r['content']}\n\n---\n\n")
            else:
                f.write(f"## Page {r['page']} - ERROR\n\n```\n{r['error']}\n```\n\n")
    
    print(f"💾 Saved: {file}")

def main():
    import sys
    
    # Find PDF
    pdf = Path("pdf_corpus/สิ่งที่ส่งมาด้วย-2-เอกสารแนบท้ายประกาศ-3.1-Final-DQAF-v1.0.pdf")
    if not pdf.exists():
        print("❌ PDF not found")
        return
    
    print(f"🎯 PDF: {pdf.name}")
    
    # Parse args
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python ocr.py 1     # Page 1 only")
        print("  python ocr.py 3     # First 3 pages")
        print("  python ocr.py all   # All pages")
        return
    
    arg = sys.argv[1]
    if arg == "1":
        pages = [1]
    elif arg == "3":
        pages = [1, 2, 3]
    elif arg == "all":
        pages = None
    else:
        print("❌ Invalid argument")
        return
    
    ocr_pdf(pdf, pages)

if __name__ == "__main__":
    main()
