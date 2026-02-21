#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

# 註冊中文字體
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
except Exception as e:
    print(f"字體註冊錯誤: {e}")
    font_name = 'Helvetica'

# 讀取新聞內容
news_content = """
國際重點新聞摘要
2026年2月14-15日

1. 台美簽署貿易協定，美議員：展現雙方持續夥伴關係
時間：2026年2月15日
來源：中央社 CNA
摘要：台美雙方正式簽署對等貿易協定，這是台美經貿關係的重要里程碑。美國議員表示，此協定展現了雙方持續的夥伴關係，將有助於深化經濟合作。協定內容涵蓋多項貿易便利化措施，預計將送交立法院審議。
關鍵要點：
• 台美對等貿易協定正式簽署
• 美方強調展現雙方持續夥伴關係
• 協定將送立法院審議
• 預計在4月川習會前把握機運

2. 美國施壓引發能源危機，古巴取消雪茄節
時間：2026年2月15日
來源：中央社 CNA
摘要：由於美國持續施壓導致的能源危機，古巴政府宣布取消原定舉行的年度雪茄節。這是古巴重要的文化與經濟活動，取消顯示了當前經濟困境的嚴重性。
關鍵要點：
• 美國施壓導致古巴能源危機惡化
• 年度重要文化活動「雪茄節」被迫取消
• 反映古巴當前經濟困境
• 可能影響古巴旅遊業與外匯收入

3. 蘇丹準軍事組織攻擊達佛，聯合國：3天逾6000死
時間：2026年2月15日
來源：中央社 CNA
摘要：蘇丹準軍事組織近日對達佛地區發動大規模攻擊，聯合國報告指出在短短3天內已有超過6000人死亡。這是蘇丹內戰爆發以來最嚴重的單次傷亡事件，引發國際社會高度關注。
關鍵要點：
• 蘇丹準軍事組織攻擊達佛地區
• 3天內死亡人數超過6000人
• 聯合國對人道危機表示嚴重關切
• 國際社會呼籲立即停火

4. 歐洲央行擴大回購機制，提升歐元全球地位
時間：2026年2月15日
來源：中央社 CNA
摘要：歐洲央行宣布擴大回購機制，旨在提升歐元在全球金融體系中的地位。此舉被視為對抗美元主導地位的重要策略，同時也為歐元區經濟提供更多流動性支持。
關鍵要點：
• 歐洲央行擴大回購機制
• 目標提升歐元全球地位
• 對抗美元主導的金融體系
• 為歐元區提供流動性支持

5. 巴西嘉年華推「不就是不」，守護女性安全成全民運動
時間：2026年2月15日
來源：中央社 CNA
摘要：巴西嘉年華期間推出「不就是不」運動，旨在保護女性安全，防止性騷擾事件。這項全民運動獲得廣泛響應，顯示巴西社會對性別平等議題的重視。
關鍵要點：
• 巴西嘉年華期間推出女性安全運動
• 「不就是不」口號強調性自主權
• 全民參與守護女性安全
• 反映社會對性別平等議題的重視

資料來源：中央社 CNA 國際新聞
整理時間：2026年2月15日
整理者：小熊抱 AI助手 🧸🤗
"""

# 創建PDF
doc = SimpleDocTemplate(
    "國際重點新聞_text.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# 創建樣式
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='ChineseTitle',
    fontName=font_name,
    fontSize=16,
    alignment=TA_CENTER,
    spaceAfter=12
))
styles.add(ParagraphStyle(
    name='ChineseSubtitle',
    fontName=font_name,
    fontSize=14,
    alignment=TA_CENTER,
    spaceAfter=20
))
styles.add(ParagraphStyle(
    name='ChineseHeading',
    fontName=font_name,
    fontSize=12,
    spaceBefore=12,
    spaceAfter=6
))
styles.add(ParagraphStyle(
    name='ChineseNormal',
    fontName=font_name,
    fontSize=10,
    alignment=TA_LEFT,
    spaceAfter=6
))
styles.add(ParagraphStyle(
    name='ChineseSmall',
    fontName=font_name,
    fontSize=9,
    alignment=TA_LEFT,
    spaceAfter=3
))

# 構建內容
story = []

# 標題
story.append(Paragraph("國際重點新聞摘要", styles['ChineseTitle']))
story.append(Paragraph("2026年2月14-15日", styles['ChineseSubtitle']))
story.append(Spacer(1, 20))

# 分割內容
sections = news_content.strip().split('\n\n')
for section in sections:
    if section.strip():
        # 簡單判斷段落類型
        if '國際重點新聞摘要' in section:
            continue  # 已經處理過標題
        elif '時間：' in section and '來源：' in section:
            # 新聞項目
            lines = section.split('\n')
            for line in lines:
                if line.strip():
                    if line.startswith(tuple('12345.')):
                        story.append(Paragraph(line, styles['ChineseHeading']))
                    elif line.startswith('時間：') or line.startswith('來源：') or line.startswith('摘要：'):
                        story.append(Paragraph(line, styles['ChineseNormal']))
                    elif line.startswith('•'):
                        story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;" + line, styles['ChineseNormal']))
                    elif '關鍵要點：' in line:
                        story.append(Paragraph(line, styles['ChineseNormal']))
                    else:
                        story.append(Paragraph(line, styles['ChineseNormal']))
            story.append(Spacer(1, 12))
        else:
            # 其他內容（如資料來源）
            story.append(Paragraph(section, styles['ChineseSmall']))

# 生成PDF
doc.build(story)
print(f"PDF創建成功！使用字體: {font_name}")
print(f"檔案: 國際重點新聞_text.pdf")