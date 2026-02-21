#!/usr/bin/env python3
from fpdf import FPDF
import markdown

# 讀取Markdown內容
with open('國際重點新聞_2026-02-15.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# 將Markdown轉換為HTML
html_content = markdown.markdown(md_content)

# 創建PDF
pdf = FPDF()
pdf.add_page()
pdf.add_font('NotoSansTC', '', '/System/Library/Fonts/PingFang.ttc', uni=True)
pdf.set_font('NotoSansTC', '', 12)

# 簡單的HTML到文本轉換（簡化版）
lines = md_content.split('\n')
for line in lines:
    # 移除Markdown標記
    line = line.replace('#', '').replace('**', '').replace('---', '')
    if line.strip():
        # 處理標題
        if line.startswith('##'):
            pdf.set_font('NotoSansTC', 'B', 14)
            pdf.cell(0, 10, line.replace('##', '').strip(), ln=True)
            pdf.set_font('NotoSansTC', '', 12)
        elif line.startswith('###'):
            pdf.set_font('NotoSansTC', 'B', 12)
            pdf.cell(0, 8, line.replace('###', '').strip(), ln=True)
            pdf.set_font('NotoSansTC', '', 12)
        else:
            # 處理列表項目
            if line.strip().startswith('-'):
                pdf.cell(10)
                pdf.cell(0, 6, '• ' + line.strip()[1:].strip(), ln=True)
            else:
                pdf.multi_cell(0, 6, line.strip())
        pdf.ln(2)

pdf.output('國際重點新聞_2026-02-15.pdf')
print("PDF created successfully!")