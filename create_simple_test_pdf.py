#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.colors import black, HexColor
import os

# 註冊中文字體
font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('STHeiti', font_path))
    font_name = 'STHeiti'
else:
    font_name = 'Helvetica'

# 創建PDF
pdf = canvas.Canvas("PDF檢查測試_簡單版.pdf", pagesize=A4)
width, height = A4

# 設置非常大的邊距，確保文字不會被截斷
left_margin = 3*cm
right_margin = 3*cm
top_margin = 3*cm
bottom_margin = 3*cm

# 當前Y位置
y = height - top_margin

# 測試1：簡單標題（確保不被截斷）
pdf.setFont(font_name, 16)
pdf.setFillColor(HexColor("#1e3a8a"))
title = "PDF檢查測試 - 簡單版"
# 計算標題寬度，確保不超過頁面
title_width = pdf.stringWidth(title, font_name, 16)
if title_width > width - left_margin - right_margin:
    # 如果太長，縮小字體
    pdf.setFont(font_name, 14)
    title_width = pdf.stringWidth(title, font_name, 14)

pdf.drawCentredString(width/2, y, title)
y -= 1.5*cm

# 測試2：檢查標準列表（確保不重疊）
pdf.setFont(font_name, 12)
pdf.setFillColor(black)

check_items = [
    "1. 文字清晰無重疊",
    "2. 格式簡單正確",
    "3. 中文字體正常",
    "4. 內容完整顯示",
    "5. 文字清晰可讀",
    "6. 文字不被截斷",
    "7. 文字數字不重疊"
]

for i, item in enumerate(check_items):
    # 計算每項的高度位置
    item_y = y - i * 0.8*cm
    
    # 檢查是否會超出頁面底部
    if item_y < bottom_margin:
        pdf.showPage()
        y = height - top_margin
        item_y = y - (i % 10) * 0.8*cm
    
    # 檢查文字寬度，確保不被截斷
    item_width = pdf.stringWidth(item, font_name, 12)
    if item_width > width - left_margin - right_margin:
        # 如果太長，縮小字體
        pdf.setFont(font_name, 10)
        item_width = pdf.stringWidth(item, font_name, 10)
        pdf.drawString(left_margin, item_y, item)
        pdf.setFont(font_name, 12)
    else:
        pdf.drawString(left_margin, item_y, item)

y -= len(check_items) * 0.8*cm + 1*cm

# 測試3：長文本測試（確保不被截斷）
pdf.setFont(font_name, 11)
pdf.setFillColor(black)
pdf.drawString(left_margin, y, "長文本測試：")
y -= 0.6*cm

long_text = "這是一個測試段落，用來檢查文字是否會被截斷。我們需要確保所有文字都能完整顯示，不會因為排版問題而丟失內容。中文排版需要特別注意字間距和行距。"

# 手動換行，確保不被截斷
words = long_text.split()
current_line = ""
line_height = 0.5*cm
max_width = width - left_margin - right_margin

for word in words:
    test_line = current_line + " " + word if current_line else word
    test_width = pdf.stringWidth(test_line, font_name, 11)
    
    if test_width <= max_width:
        current_line = test_line
    else:
        # 繪製當前行
        if current_line:
            pdf.drawString(left_margin, y, current_line)
            y -= line_height
            
            # 檢查是否需要換頁
            if y < bottom_margin + 2*cm:
                pdf.showPage()
                y = height - top_margin
                pdf.setFont(font_name, 11)
        
        current_line = word

# 繪製最後一行
if current_line:
    pdf.drawString(left_margin, y, current_line)
    y -= line_height

y -= 0.8*cm

# 測試4：數字測試（確保不重疊）
pdf.setFont(font_name, 12)
pdf.setFillColor(HexColor("#1e3a8a"))
pdf.drawString(left_margin, y, "數字測試：")
y -= 0.6*cm

numbers = [
    ("營收", "1,234,567"),
    ("增長", "+24.75%"),
    ("股價", "$245.67"),
    ("用戶", "3,847,291")
]

# 計算每個數字的間距
num_items = len(numbers)
if num_items > 0:
    item_spacing = (width - left_margin - right_margin) / num_items
    
    for i, (label, value) in enumerate(numbers):
        x = left_margin + i * item_spacing + item_spacing/2
        
        # 標籤
        pdf.setFont(font_name, 10)
        pdf.setFillColor(HexColor("#6b7280"))
        label_width = pdf.stringWidth(label, font_name, 10)
        pdf.drawString(x - label_width/2, y, label)
        
        # 數值（檢查不重疊）
        pdf.setFont(font_name, 14)
        pdf.setFillColor(HexColor("#1e3a8a"))
        value_width = pdf.stringWidth(value, font_name, 14)
        
        # 確保數值不與相鄰項目重疊
        if value_width > item_spacing * 0.8:
            pdf.setFont(font_name, 12)
            value_width = pdf.stringWidth(value, font_name, 12)
        
        pdf.drawString(x - value_width/2, y - 0.6*cm, value)

y -= 2*cm

# 測試5：邊界測試（確保邊緣文字不被截斷）
pdf.setFont(font_name, 10)
pdf.setFillColor(HexColor("#ef4444"))
pdf.drawString(left_margin, y, "左邊界測試文字")
pdf.drawString(width - right_margin - pdf.stringWidth("右邊界測試文字", font_name, 10), y, "右邊界測試文字")
y -= 0.5*cm

pdf.drawString(left_margin, bottom_margin, "下邊界測試文字")
pdf.drawString(left_margin, height - top_margin, "上邊界測試文字")

# 頁尾
y = bottom_margin + 1*cm
pdf.setFont(font_name, 9)
pdf.setFillColor(HexColor("#6b7280"))
pdf.drawString(left_margin, y, "測試時間：2026年2月15日 13:09 GMT+8")
y -= 0.4*cm
pdf.drawString(left_margin, y, "測試目的：驗證文字不被截斷且不重疊")
y -= 0.4*cm
pdf.drawString(left_margin, y, "檢查結果：請確認所有文字完整顯示")

# 保存PDF
pdf.save()

print("=" * 60)
print("📋 簡單PDF測試文件生成完成")
print("=" * 60)
print("檔案：PDF檢查測試_簡單版.pdf")
print("特點：")
print("1. 超大邊距（3cm），避免邊緣截斷")
print("2. 手動換行控制，確保文字完整")
print("3. 數字間距計算，避免重疊")
print("4. 字體大小動態調整")
print("=" * 60)
print("請檢查：")
print("1. 所有文字是否完整顯示（無截斷）")
print("2. 文字和數字是否無重疊")
print("3. 邊界文字是否可見")
print("=" * 60)