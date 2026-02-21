#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
import os

# 註冊中文字體
font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('STHeiti', font_path))
    font_name = 'STHeiti'
else:
    font_name = 'Helvetica'

# 新聞內容（純文本）
content_lines = [
    "國際重點新聞摘要",
    "2026年2月14-15日",
    "",
    "=" * 40,
    "",
    "1. 台美簽署貿易協定，美議員：展現雙方持續夥伴關係",
    "時間：2026年2月15日",
    "來源：中央社 CNA",
    "摘要：台美雙方正式簽署對等貿易協定，這是台美經貿關係的重要里程碑。",
    "美國議員表示，此協定展現了雙方持續的夥伴關係，將有助於深化經濟合作。",
    "協定內容涵蓋多項貿易便利化措施，預計將送交立法院審議。",
    "關鍵要點：",
    "• 台美對等貿易協定正式簽署",
    "• 美方強調展現雙方持續夥伴關係",
    "• 協定將送立法院審議",
    "• 預計在4月川習會前把握機運",
    "",
    "=" * 40,
    "",
    "2. 美國施壓引發能源危機，古巴取消雪茄節",
    "時間：2026年2月15日",
    "來源：中央社 CNA",
    "摘要：由於美國持續施壓導致的能源危機，古巴政府宣布取消原定舉行的年度雪茄節。",
    "這是古巴重要的文化與經濟活動，取消顯示了當前經濟困境的嚴重性。",
    "關鍵要點：",
    "• 美國施壓導致古巴能源危機惡化",
    "• 年度重要文化活動「雪茄節」被迫取消",
    "• 反映古巴當前經濟困境",
    "• 可能影響古巴旅遊業與外匯收入",
    "",
    "=" * 40,
    "",
    "3. 蘇丹準軍事組織攻擊達佛，聯合國：3天逾6000死",
    "時間：2026年2月15日",
    "來源：中央社 CNA",
    "摘要：蘇丹準軍事組織近日對達佛地區發動大規模攻擊，聯合國報告指出在短短3天內",
    "已有超過6000人死亡。這是蘇丹內戰爆發以來最嚴重的單次傷亡事件，引發國際社會高度關注。",
    "關鍵要點：",
    "• 蘇丹準軍事組織攻擊達佛地區",
    "• 3天內死亡人數超過6000人",
    "• 聯合國對人道危機表示嚴重關切",
    "• 國際社會呼籲立即停火",
    "",
    "=" * 40,
    "",
    "4. 歐洲央行擴大回購機制，提升歐元全球地位",
    "時間：2026年2月15日",
    "來源：中央社 CNA",
    "摘要：歐洲央行宣布擴大回購機制，旨在提升歐元在全球金融體系中的地位。",
    "此舉被視為對抗美元主導地位的重要策略，同時也為歐元區經濟提供更多流動性支持。",
    "關鍵要點：",
    "• 歐洲央行擴大回購機制",
    "• 目標提升歐元全球地位",
    "• 對抗美元主導的金融體系",
    "• 為歐元區提供流動性支持",
    "",
    "=" * 40,
    "",
    "5. 巴西嘉年華推「不就是不」，守護女性安全成全民運動",
    "時間：2026年2月15日",
    "來源：中央社 CNA",
    "摘要：巴西嘉年華期間推出「不就是不」運動，旨在保護女性安全，防止性騷擾事件。",
    "這項全民運動獲得廣泛響應，顯示巴西社會對性別平等議題的重視。",
    "關鍵要點：",
    "• 巴西嘉年華期間推出女性安全運動",
    "• 「不就是不」口號強調性自主權",
    "• 全民參與守護女性安全",
    "• 反映社會對性別平等議題的重視",
    "",
    "=" * 40,
    "",
    "資料來源：中央社 CNA 國際新聞",
    "整理時間：2026年2月15日",
    "整理者：小熊抱 AI助手 🧸🤗"
]

# 創建PDF
pdf = canvas.Canvas("國際重點新聞_simple.pdf", pagesize=A4)
width, height = A4

# 設置字體
pdf.setFont(font_name, 12)

# 寫入內容
y = height - 2*cm
line_height = 14

for line in content_lines:
    if y < 2*cm:
        pdf.showPage()
        pdf.setFont(font_name, 12)
        y = height - 2*cm
    
    # 處理不同類型的行
    if line == "國際重點新聞摘要":
        pdf.setFont(font_name, 16)
        pdf.drawCentredString(width/2, y, line)
        pdf.setFont(font_name, 12)
        y -= line_height * 1.5
    elif line == "2026年2月14-15日":
        pdf.setFont(font_name, 14)
        pdf.drawCentredString(width/2, y, line)
        pdf.setFont(font_name, 12)
        y -= line_height * 2
    elif line.startswith("=" * 40):
        y -= line_height * 0.5
        pdf.line(2*cm, y, width-2*cm, y)
        y -= line_height * 0.5
    elif line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.") or line.startswith("5."):
        pdf.setFont(font_name, 13)
        pdf.drawString(2*cm, y, line)
        pdf.setFont(font_name, 12)
        y -= line_height * 1.2
    elif line.startswith("時間：") or line.startswith("來源：") or line.startswith("摘要：") or line.startswith("關鍵要點："):
        pdf.setFont(font_name, 11)
        pdf.drawString(2*cm, y, line)
        pdf.setFont(font_name, 12)
        y -= line_height
    elif line.startswith("•"):
        pdf.drawString(2.5*cm, y, line)
        y -= line_height
    elif line.startswith("資料來源：") or line.startswith("整理時間：") or line.startswith("整理者："):
        pdf.setFont(font_name, 10)
        pdf.drawString(2*cm, y, line)
        pdf.setFont(font_name, 12)
        y -= line_height
    elif line.strip() == "":
        y -= line_height * 0.5
    else:
        # 處理長文本換行
        text = line.strip()
        max_width = width - 4*cm
        
        # 簡單的文本換行
        words = text.split()
        current_line = []
        current_text = ""
        
        for word in words:
            test_text = current_text + " " + word if current_text else word
            text_width = pdf.stringWidth(test_text, font_name, 12)
            
            if text_width <= max_width:
                current_text = test_text
            else:
                if current_text:
                    pdf.drawString(2*cm, y, current_text)
                    y -= line_height
                    if y < 2*cm:
                        pdf.showPage()
                        pdf.setFont(font_name, 12)
                        y = height - 2*cm
                current_text = word
        
        if current_text:
            pdf.drawString(2*cm, y, current_text)
            y -= line_height
    y -= line_height * 0.3

pdf.save()
print(f"PDF創建成功！檔案: 國際重點新聞_simple.pdf")
print(f"使用字體: {font_name}")