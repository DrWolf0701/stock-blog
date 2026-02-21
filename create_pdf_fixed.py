#!/usr/bin/env python3
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm

# 註冊中文字體（使用系統中的中文字體）
try:
    # 嘗試使用蘋方字體
    font_path = "/System/Library/Fonts/PingFang.ttc"
    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont('PingFang', font_path))
        font_name = 'PingFang'
    else:
        # 嘗試其他中文字體
        font_path = "/System/Library/Fonts/STHeiti Light.ttc"
        if os.path.exists(font_path):
            pdfmetrics.registerFont(TTFont('STHeiti', font_path))
            font_name = 'STHeiti'
        else:
            font_name = 'Helvetica'
except:
    font_name = 'Helvetica'

# 讀取Markdown內容
with open('國際重點新聞_2026-02-15.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 創建PDF
pdf = canvas.Canvas('國際重點新聞_2026-02-15_fixed.pdf', pagesize=A4)
width, height = A4

# 設置字體
pdf.setFont(font_name, 12)

# 寫入內容
y = height - 2*cm
line_height = 14

lines = content.split('\n')
for line in lines:
    if y < 2*cm:
        pdf.showPage()
        pdf.setFont(font_name, 12)
        y = height - 2*cm
    
    # 簡單處理Markdown格式
    if line.startswith('# '):
        pdf.setFont(font_name, 16)
        pdf.drawString(2*cm, y, line[2:])
        pdf.setFont(font_name, 12)
        y -= line_height * 1.5
    elif line.startswith('## '):
        pdf.setFont(font_name, 14)
        pdf.drawString(2*cm, y, line[3:])
        pdf.setFont(font_name, 12)
        y -= line_height * 1.3
    elif line.startswith('### '):
        pdf.setFont(font_name, 13)
        pdf.drawString(2*cm, y, line[4:])
        pdf.setFont(font_name, 12)
        y -= line_height * 1.2
    elif line.strip() == '---':
        y -= line_height
        pdf.line(2*cm, y, width-2*cm, y)
        y -= line_height
    elif line.strip().startswith('**'):
        # 粗體處理（使用相同字體但加粗效果）
        pdf.setFont(font_name, 12)
        clean_line = line.replace('**', '')
        pdf.drawString(2*cm, y, clean_line)
        y -= line_height
    elif line.strip().startswith('-'):
        pdf.drawString(2.5*cm, y, '• ' + line.strip()[1:].strip())
        y -= line_height
    elif line.strip():
        # 處理長文本換行
        text = line.strip()
        max_width = width - 4*cm
        words = text.split()
        current_line = []
        current_width = 0
        
        for word in words:
            word_width = pdf.stringWidth(word + ' ', font_name, 12)
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width
            else:
                if current_line:
                    pdf.drawString(2*cm, y, ' '.join(current_line))
                    y -= line_height
                    if y < 2*cm:
                        pdf.showPage()
                        pdf.setFont(font_name, 12)
                        y = height - 2*cm
                current_line = [word]
                current_width = word_width
        
        if current_line:
            pdf.drawString(2*cm, y, ' '.join(current_line))
            y -= line_height
    else:
        y -= line_height * 0.5

# 添加頁尾
pdf.setFont(font_name, 10)
pdf.drawString(2*cm, 1*cm, "資料來源：中央社 CNA 國際新聞")
pdf.drawString(2*cm, 0.7*cm, "整理時間：2026年2月15日")
pdf.drawString(2*cm, 0.4*cm, "整理者：小熊抱 AI助手 🧸🤗")

pdf.save()
print("PDF created successfully with font:", font_name)