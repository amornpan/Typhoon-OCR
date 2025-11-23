# Typhoon OCR

Simple OCR for your PDF using Typhoon OCR API.

## Setup
```bash
conda activate typhoon-ocr
echo "TYPHOON_OCR_API_KEY=your_key" > .env
```

## Usage
```bash
python ocr.py 1     # Test page 1
python ocr.py 3     # Process 3 pages  
python ocr.py all   # Process all 25 pages
```

## Output
Results saved in `output/ocr_TIMESTAMP.md`

## Your PDF
- File: สิ่งที่ส่งมาด้วย-2-เอกสารแนบท้ายประกาศ-3.1-Final-DQAF-v1.0.pdf
- Pages: 25
- Type: Thai government document (perfect for Typhoon OCR!)

Simple and clean! 🚀
