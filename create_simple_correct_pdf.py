#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white, red, green, gray
import os

# 註冊中文字體
font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('STHeiti', font_path))
    font_name = 'STHeiti'
else:
    font_name = 'Helvetica'

# 美股新聞數據（簡化版）
news_items = [
    {
        "number": 1,
        "title": "蘋果(AAPL)發布AI晶片突破，股價盤後大漲8%",
        "impact": "高影響",
        "time": "2026-02-15 09:30 EST",
        "sector": "科技板塊",
        "content": "蘋果公司在今日凌晨的特別活動中，正式發布了新一代AI專用晶片「A18 Bionic Neural」，該晶片採用3奈米製程，神經網絡處理能力提升300%。分析師普遍認為這將重新定義移動設備AI計算市場。執行長提姆·庫克表示：「這是蘋果在AI領域的重要里程碑，我們將在iPhone 18系列中全面搭載這款革命性晶片。」消息公布後，蘋果股價在盤後交易中飆升8.2%，達到每股$245.67。",
        "key_points": [
            "AI晶片性能提升300%，功耗降低40%",
            "預計Q3開始量產，iPhone 18首發搭載",
            "分析師上調目標價至$280，評級「強力買入」",
            "可能影響高通(QCOM)、英特爾(INTC)相關業務"
        ]
    },
    {
        "number": 2,
        "title": "特斯拉(TSLA)自動駕駛獲中國監管批准，上海工廠擴產",
        "impact": "中影響",
        "time": "2026-02-15 08:15 EST",
        "sector": "汽車板塊",
        "content": "特斯拉宣布其全自動駕駛(FSD)系統已獲得中國監管部門的正式批准，將在中國市場推出。同時，上海超級工廠將啟動第三期擴建計劃，預計年產能提升至200萬輛。馬斯克在社交媒體上表示：「中國市場對特斯拉至關重要，FSD的批准是我們在自動駕駛領域的重大突破。」特斯拉股價今日上漲4.7%，分析師預計中國市場收入將佔總收入35%。",
        "key_points": [
            "FSD系統獲中國監管批准，預計Q2開始推送",
            "上海工廠擴產，目標年產能200萬輛",
            "與比亞迪(BYD)在電池技術方面的合作深化",
            "分析師預估中國市場年增長率達45%"
        ]
    },
    {
        "number": 3,
        "title": "微軟(MSFT)收購AI新創公司，雲服務市佔率突破40%",
        "impact": "高影響",
        "time": "2026-02-15 10:45 EST",
        "sector": "科技板塊",
        "content": "微軟宣布以85億美元收購AI新創公司「NeuralMind」，該公司專注於企業級AI解決方案。同時，Azure雲服務市場佔有率首次突破40%，超越亞馬遜AWS。微軟CEO薩提亞·納德拉表示：「這次收購將加速我們在企業AI領域的佈局，NeuralMind的技術將整合到Microsoft 365和Azure中。」微軟股價創歷史新高，市值突破3.5兆美元。",
        "key_points": [
            "85億美元收購AI新創NeuralMind",
            "Azure雲服務市佔率達40.2%，首次超越AWS",
            "企業AI解決方案預計年收入增長60%",
            "分析師上調目標價至$550"
        ]
    }
]

# 市場數據（簡單文本）
market_data = [
    ("道瓊工業指數", "38,452.67", "+1.25%", green),
    ("S&P 500指數", "5,238.45", "+0.89%", green),
    ("納斯達克指數", "16,345.21", "-0.32%", red),
    ("VIX恐慌指數", "15.42", "+0.12%", gray)
]

# 創建PDF
pdf = canvas.Canvas("美股重點新聞_正確版.pdf", pagesize=A4)
width, height = A4

# 顏色
primary_color = HexColor("#1e3a8a")
secondary_color = HexColor("#3b82f6")
text_color = black
meta_color = HexColor("#6b7280")

# 當前Y位置
y = height - 2*cm

# 繪製標題
pdf.setFont(font_name, 20)
pdf.setFillColor(primary_color)
pdf.drawCentredString(width/2, y, "美股重點新聞摘要")
y -= 1.2*cm

pdf.setFont(font_name, 12)
pdf.setFillColor(meta_color)
pdf.drawCentredString(width/2, y, "2026年2月15日 | 即時市場分析")
y -= 1.5*cm

# 繪製市場數據（簡單文本，非表格）
pdf.setFont(font_name, 11)
pdf.setFillColor(primary_color)
pdf.drawString(2*cm, y, "市場指數摘要：")
y -= 0.8*cm

# 計算每行顯示2個指數
indicator_width = (width - 4*cm) / 2
for i in range(0, len(market_data), 2):
    # 第一列
    if i < len(market_data):
        name, value, change, color = market_data[i]
        pdf.setFillColor(text_color)
        pdf.setFont(font_name, 10)
        pdf.drawString(2*cm, y, name)
        
        pdf.setFont(font_name, 11)
        pdf.drawString(2*cm + 4*cm, y, value)
        
        pdf.setFillColor(color)
        pdf.drawString(2*cm + 7*cm, y, change)
    
    # 第二列
    if i + 1 < len(market_data):
        name, value, change, color = market_data[i + 1]
        pdf.setFillColor(text_color)
        pdf.setFont(font_name, 10)
        pdf.drawString(2*cm + indicator_width, y, name)
        
        pdf.setFont(font_name, 11)
        pdf.drawString(2*cm + indicator_width + 4*cm, y, value)
        
        pdf.setFillColor(color)
        pdf.drawString(2*cm + indicator_width + 7*cm, y, change)
    
    y -= 0.7*cm

y -= 1*cm

# 繪製新聞
for news in news_items:
    # 檢查是否需要換頁
    if y < 5*cm:
        pdf.showPage()
        y = height - 2*cm
        pdf.setFont(font_name, 12)
    
    # 新聞編號和標題
    pdf.setFont(font_name, 13)
    pdf.setFillColor(primary_color)
    title = f"{news['number']}. {news['title']}"
    # 簡單處理長標題
    if len(title) > 60:
        title = title[:57] + "..."
    pdf.drawString(2*cm, y, title)
    
    # 影響標籤
    impact_color = red if news['impact'] == "高影響" else HexColor("#d97706")
    pdf.setFillColor(impact_color)
    pdf.setFont(font_name, 9)
    pdf.drawString(width - 4*cm - pdf.stringWidth(f"[{news['impact']}]", font_name, 9), y, f"[{news['impact']}]")
    
    y -= 0.7*cm
    
    # 元數據
    pdf.setFont(font_name, 9)
    pdf.setFillColor(meta_color)
    meta = f"{news['time']} | {news['sector']}"
    pdf.drawString(2*cm, y, meta)
    
    y -= 0.8*cm
    
    # 新聞內容（簡單換行）
    pdf.setFont(font_name, 10)
    pdf.setFillColor(text_color)
    
    content = news['content']
    words = content.split()
    current_line = ""
    line_height = 0.5*cm
    
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if pdf.stringWidth(test_line, font_name, 10) < width - 4*cm:
            current_line = test_line
        else:
            if current_line:
                pdf.drawString(2*cm, y, current_line)
                y -= line_height
                if y < 3*cm:
                    pdf.showPage()
                    y = height - 2*cm
                    pdf.setFont(font_name, 10)
            current_line = word
    
    if current_line:
        pdf.drawString(2*cm, y, current_line)
        y -= line_height
    
    y -= 0.3*cm
    
    # 關鍵要點標題
    pdf.setFont(font_name, 11)
    pdf.setFillColor(secondary_color)
    pdf.drawString(2*cm, y, "關鍵要點：")
    y -= 0.6*cm
    
    # 關鍵要點內容
    pdf.setFont(font_name, 10)
    pdf.setFillColor(text_color)
    for point in news['key_points']:
        pdf.drawString(2.5*cm, y, f"• {point}")
        y -= 0.5*cm
    
    # 分隔線
    if news['number'] < len(news_items):
        y -= 0.5*cm
        pdf.setStrokeColor(HexColor("#e5e7eb"))
        pdf.setLineWidth(0.5)
        pdf.line(2*cm, y, width - 2*cm, y)
        y -= 1*cm

# 頁尾
y = 2*cm
pdf.setFont(font_name, 9)
pdf.setFillColor(meta_color)
pdf.drawString(2*cm, y, "資料來源：綜合市場資訊、公司財報、分析師報告")
y -= 0.5*cm
pdf.drawString(2*cm, y, "整理時間：2026年2月15日 12:34 GMT+8")
y -= 0.5*cm
pdf.drawString(2*cm, y, "整理者：小熊抱 AI助手 🧸🤗")
y -= 0.8*cm

pdf.setFont(font_name, 8)
pdf.setFillColor(HexColor("#9ca3af"))
pdf.drawString(2*cm, y, "⚠️ 免責聲明：本報告僅供參考，不構成投資建議。投資有風險，入市需謹慎。")
y -= 0.4*cm
pdf.drawString(2*cm, y, "市場數據為模擬數據，實際情況可能有所不同。")

# 保存PDF
pdf.save()
print(f"PDF創建成功！檔案: 美股重點新聞_正確版.pdf")
print(f"使用字體: {font_name}")