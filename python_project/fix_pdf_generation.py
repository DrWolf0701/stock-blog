#!/usr/bin/env python3
"""修正 PDF 生成問題"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_tiny_pdf():
    """建立超小 PDF"""
    filename = "minimal_output/tiny_report.pdf"
    
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        
        # 極簡內容
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, "簡報")
        c.drawString(100, 680, datetime.now().strftime("%Y-%m-%d"))
        c.drawString(100, 660, "狀態: 正常")
        c.drawString(100, 640, "OpenClaw 🐻")
        
        c.save()
        
        size = os.path.getsize(filename)
        print(f"✅ 超小 PDF 建立完成: {size:,} bytes")
        return True
        
    except Exception as e:
        print(f"❌ PDF 建立失敗: {e}")
        return False


# 執行
create_tiny_pdf()