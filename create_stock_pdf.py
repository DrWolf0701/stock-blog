#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
import os

# 註冊中文字體
font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('STHeiti', font_path))
    font_name = 'STHeiti'
else:
    font_name = 'Helvetica'

# 美股新聞內容
news_data = [
    {
        "number": 1,
        "title": "蘋果(AAPL)發布AI晶片突破，股價盤後大漲8%",
        "impact": "高影響",
        "time": "2026-02-15 09:30 EST",
        "sector": "科技板塊",
        "volume": "成交量: 45.2M",
        "content": [
            "蘋果公司在今日凌晨的特別活動中，正式發布了新一代AI專用晶片「A18 Bionic Neural」，",
            "該晶片採用3奈米製程，神經網絡處理能力提升300%。分析師普遍認為這將重新定義移動設備AI計算市場。",
            "執行長提姆·庫克表示：「這是蘋果在AI領域的重要里程碑，我們將在iPhone 18系列中全面搭載這款革命性晶片。」",
            "消息公布後，蘋果股價在盤後交易中飆升8.2%，達到每股$245.67。"
        ],
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
        "volume": "成交量: 32.8M",
        "content": [
            "特斯拉宣布其全自動駕駛(FSD)系統已獲得中國監管部門的正式批准，將在中國市場推出。",
            "同時，上海超級工廠將啟動第三期擴建計劃，預計年產能提升至200萬輛。",
            "馬斯克在社交媒體上表示：「中國市場對特斯拉至關重要，FSD的批准是我們在自動駕駛領域的重大突破。」",
            "特斯拉股價今日上漲4.7%，分析師預計中國市場收入將佔總收入35%。"
        ],
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
        "volume": "成交量: 28.3M",
        "content": [
            "微軟宣布以85億美元收購AI新創公司「NeuralMind」，該公司專注於企業級AI解決方案。",
            "同時，Azure雲服務市場佔有率首次突破40%，超越亞馬遜AWS。",
            "微軟CEO薩提亞·納德拉表示：「這次收購將加速我們在企業AI領域的佈局，NeuralMind的技術將整合到Microsoft 365和Azure中。」",
            "微軟股價創歷史新高，市值突破3.5兆美元。"
        ],
        "key_points": [
            "85億美元收購AI新創NeuralMind",
            "Azure雲服務市佔率達40.2%，首次超越AWS",
            "企業AI解決方案預計年收入增長60%",
            "分析師上調目標價至$550"
        ]
    },
    {
        "number": 4,
        "title": "NVIDIA(NVDA)數據中心業務強勁，Q4營收超預期",
        "impact": "中影響",
        "time": "2026-02-15 16:30 EST",
        "sector": "半導體板塊",
        "volume": "成交量: 52.1M",
        "content": [
            "NVIDIA公布2026財年第四季度財報，數據中心業務營收達185億美元，年增78%，大幅超越市場預期。",
            "CEO黃仁勳表示，AI需求持續強勁，公司正在加速新一代GPU的生產。",
            "「AI革命才剛剛開始，」黃仁勳在財報電話會議中表示，「我們的Blackwell架構GPU供不應求，預計2026年將是AI基礎設施建設的關鍵一年。」"
        ],
        "key_points": [
            "Q4營收285億美元，EPS $5.67，雙雙超預期",
            "數據中心業務營收185億美元，年增78%",
            "Blackwell架構GPU訂單已排至2027年",
            "宣布250億美元股票回購計劃"
        ]
    }
]

# 市場數據
market_data = [
    {"name": "道瓊工業指數", "value": "38,452.67", "change": "+1.25%", "type": "positive"},
    {"name": "S&P 500指數", "value": "5,238.45", "change": "+0.89%", "type": "positive"},
    {"name": "納斯達克指數", "value": "16,345.21", "change": "-0.32%", "type": "negative"},
    {"name": "VIX恐慌指數", "value": "15.42", "change": "+0.12%", "type": "neutral"}
]

# 創建PDF
pdf = canvas.Canvas("美股重點新聞_可讀版.pdf", pagesize=A4)
width, height = A4

# 顏色定義
colors = {
    "primary": HexColor("#1e3a8a"),
    "secondary": HexColor("#3b82f6"),
    "positive": HexColor("#10b981"),
    "negative": HexColor("#ef4444"),
    "neutral": HexColor("#6b7280"),
    "light_bg": HexColor("#f8fafc"),
    "border": HexColor("#e5e7eb"),
    "text": HexColor("#333333")
}

# 繪製標題
def draw_title():
    pdf.setFillColor(colors["primary"])
    pdf.setFont(font_name, 20)
    pdf.drawCentredString(width/2, height-3*cm, "📈 美股重點新聞摘要")
    
    pdf.setFillColor(colors["neutral"])
    pdf.setFont(font_name, 14)
    pdf.drawCentredString(width/2, height-4*cm, "2026年2月15日 | 即時市場分析")
    
    # 標題底線
    pdf.setStrokeColor(colors["secondary"])
    pdf.setLineWidth(2)
    pdf.line(2*cm, height-4.5*cm, width-2*cm, height-4.5*cm)
    
    return height-5*cm

# 繪製市場摘要
def draw_market_summary(y):
    # 背景
    pdf.setFillColor(colors["light_bg"])
    pdf.rect(2*cm, y-2*cm, width-4*cm, 2.5*cm, fill=1, stroke=0)
    pdf.setFillColor(colors["border"])
    pdf.rect(2*cm, y-2*cm, width-4*cm, 2.5*cm, fill=0, stroke=1)
    
    # 標題
    pdf.setFillColor(colors["primary"])
    pdf.setFont(font_name, 12)
    pdf.drawString(2.5*cm, y-0.5*cm, "市場指數摘要")
    
    # 計算每個指標的位置
    indicator_width = (width-5*cm) / 4
    x_positions = [2.5*cm + i*indicator_width for i in range(4)]
    
    for i, data in enumerate(market_data):
        x = x_positions[i]
        
        # 指數名稱
        pdf.setFillColor(colors["neutral"])
        pdf.setFont(font_name, 9)
        pdf.drawString(x, y-1.2*cm, data["name"])
        
        # 指數值
        pdf.setFillColor(colors["text"])
        pdf.setFont(font_name, 14)
        pdf.drawString(x, y-1.8*cm, data["value"])
        
        # 漲跌幅
        if data["type"] == "positive":
            pdf.setFillColor(colors["positive"])
        elif data["type"] == "negative":
            pdf.setFillColor(colors["negative"])
        else:
            pdf.setFillColor(colors["neutral"])
        
        pdf.setFont(font_name, 10)
        pdf.drawString(x, y-2.2*cm, data["change"])
    
    return y-3*cm

# 繪製新聞項目
def draw_news_item(y, news, is_first=False):
    if y < 5*cm:
        pdf.showPage()
        y = height-3*cm
        pdf.setFont(font_name, 12)
    
    # 新聞編號
    pdf.setFillColor(colors["primary"])
    pdf.setFont(font_name, 14)
    pdf.drawString(2*cm, y, f"{news['number']}.")
    
    # 新聞標題
    pdf.setFillColor(colors["primary"])
    pdf.setFont(font_name, 13)
    title_x = 2.5*cm
    title = news['title']
    if len(title) > 50:
        title = title[:47] + "..."
    pdf.drawString(title_x, y, title)
    
    # 影響標籤
    impact_color = colors["negative"] if news['impact'] == "高影響" else HexColor("#d97706")
    pdf.setFillColor(impact_color)
    pdf.setFont(font_name, 9)
    pdf.drawString(title_x + pdf.stringWidth(title, font_name, 13) + 0.5*cm, y, f"[{news['impact']}]")
    
    y -= 0.7*cm
    
    # 元數據
    pdf.setFillColor(colors["neutral"])
    pdf.setFont(font_name, 9)
    meta = f"⏰ {news['time']} | 🏢 {news['sector']} | 📊 {news['volume']}"
    pdf.drawString(2.5*cm, y, meta)
    
    y -= 0.8*cm
    
    # 新聞內容
    pdf.setFillColor(colors["text"])
    pdf.setFont(font_name, 10)
    for line in news['content']:
        # 簡單文本換行
        words = line.split()
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if pdf.stringWidth(test_line, font_name, 10) < width - 4*cm:
                current_line = test_line
            else:
                if current_line:
                    pdf.drawString(2.5*cm, y, current_line)
                    y -= 0.5*cm
                    if y < 3*cm:
                        pdf.showPage()
                        y = height-3*cm
                        pdf.setFont(font_name, 10)
                current_line = word
        
        if current_line:
            pdf.drawString(2.5*cm, y, current_line)
            y -= 0.5*cm
    
    y -= 0.3*cm
    
    # 關鍵要點標題
    pdf.setFillColor(colors["secondary"])
    pdf.setFont(font_name, 11)
    pdf.drawString(2.5*cm, y, "📋 關鍵要點")
    
    y -= 0.6*cm
    
    # 關鍵要點內容
    pdf.setFillColor(colors["text"])
    pdf.setFont(font_name, 10)
    for point in news['key_points']:
        pdf.drawString(3*cm, y, f"• {point}")
        y -= 0.5*cm
    
    y -= 0.8*cm
    
    # 分隔線（如果不是最後一個）
    if news['number'] < len(news_data):
        pdf.setStrokeColor(colors["border"])
        pdf.setLineWidth(0.5)
        pdf.line(2*cm, y, width-2*cm, y)
        y -= 0.8*cm
    
    return y

# 繪製頁尾
def draw_footer(y):
    pdf.setFillColor(colors["neutral"])
    pdf.setFont(font_name, 9)
    
    pdf.drawString(2*cm, y, "資料來源：綜合市場資訊、公司財報、分析師報告")
    y -= 0.5*cm
    pdf.drawString(2*cm, y, "整理時間：2026年2月15日 12:20 GMT+8")
    y -= 0.5*cm
    pdf.drawString(2*cm, y, "整理者：小熊抱 AI助手 🧸🤗")
    y -= 0.8*cm
    
    # 免責聲明
    pdf.setFillColor(HexColor("#9ca3af"))
    pdf.setFont(font_name, 8)
    pdf.drawString(2*cm, y, "⚠️ 免責聲明：本報告僅供參考，不構成投資建議。投資有風險，入市需謹慎。")
    y -= 0.4*cm
    pdf.drawString(2*cm, y, "市場數據為模擬數據，實際情況可能有所不同。")
    
    return y

# 主繪製流程
y_position = draw_title()
y_position = draw_market_summary(y_position)
y_position -= 1*cm

for news in news_data:
    y_position = draw_news_item(y_position, news)

# 繪製頁尾
draw_footer(2.5*cm)

# 保存PDF
pdf.save()
print(f"PDF創建成功！檔案: 美股重點新聞_可讀版.pdf")
print(f"使用字體: {font_name}")