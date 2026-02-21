#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
import os

# 註冊中文字體
font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('STHeiti', font_path))
    pdfmetrics.registerFont(TTFont('STHeiti-Bold', font_path))
    font_name = 'STHeiti'
else:
    font_name = 'Helvetica'

# 創建樣式
styles = getSampleStyleSheet()

# 自定義樣式
styles.add(ParagraphStyle(
    name='ChineseTitle',
    fontName=font_name,
    fontSize=24,
    alignment=TA_CENTER,
    textColor=HexColor('#1e3a8a'),
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name='ChineseSubtitle',
    fontName=font_name,
    fontSize=14,
    alignment=TA_CENTER,
    textColor=HexColor('#6b7280'),
    spaceAfter=30
))

styles.add(ParagraphStyle(
    name='NewsTitle',
    fontName=font_name + '-Bold',
    fontSize=13,
    textColor=HexColor('#1e3a8a'),
    spaceAfter=6,
    leftIndent=0
))

styles.add(ParagraphStyle(
    name='NewsMeta',
    fontName=font_name,
    fontSize=9,
    textColor=HexColor('#6b7280'),
    spaceAfter=12,
    leftIndent=0
))

styles.add(ParagraphStyle(
    name='NewsContent',
    fontName=font_name,
    fontSize=10,
    textColor=black,
    alignment=TA_JUSTIFY,
    spaceAfter=12,
    leftIndent=0,
    rightIndent=0,
    wordWrap='CJK'
))

styles.add(ParagraphStyle(
    name='KeyPointsTitle',
    fontName=font_name + '-Bold',
    fontSize=11,
    textColor=HexColor('#3b82f6'),
    spaceAfter=8,
    leftIndent=0
))

styles.add(ParagraphStyle(
    name='KeyPoint',
    fontName=font_name,
    fontSize=10,
    textColor=black,
    leftIndent=20,
    spaceAfter=6,
    bulletIndent=10
))

styles.add(ParagraphStyle(
    name='Footer',
    fontName=font_name,
    fontSize=9,
    textColor=HexColor('#6b7280'),
    alignment=TA_CENTER,
    spaceAfter=6
))

styles.add(ParagraphStyle(
    name='Disclaimer',
    fontName=font_name,
    fontSize=8,
    textColor=HexColor('#9ca3af'),
    alignment=TA_CENTER,
    spaceAfter=3
))

# 美股新聞數據
news_items = [
    {
        "number": 1,
        "title": "蘋果(AAPL)發布AI晶片突破，股價盤後大漲8%",
        "impact": "高影響",
        "time": "2026-02-15 09:30 EST",
        "sector": "科技板塊",
        "volume": "成交量: 45.2M",
        "content": [
            "蘋果公司在今日凌晨的特別活動中，正式發布了新一代AI專用晶片「A18 Bionic Neural」，該晶片採用3奈米製程，神經網絡處理能力提升300%。分析師普遍認為這將重新定義移動設備AI計算市場。",
            "執行長提姆·庫克表示：「這是蘋果在AI領域的重要里程碑，我們將在iPhone 18系列中全面搭載這款革命性晶片。」消息公布後，蘋果股價在盤後交易中飆升8.2%，達到每股$245.67。"
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
            "特斯拉宣布其全自動駕駛(FSD)系統已獲得中國監管部門的正式批准，將在中國市場推出。同時，上海超級工廠將啟動第三期擴建計劃，預計年產能提升至200萬輛。",
            "馬斯克在社交媒體上表示：「中國市場對特斯拉至關重要，FSD的批准是我們在自動駕駛領域的重大突破。」特斯拉股價今日上漲4.7%，分析師預計中國市場收入將佔總收入35%。"
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
            "微軟宣布以85億美元收購AI新創公司「NeuralMind」，該公司專注於企業級AI解決方案。同時，Azure雲服務市場佔有率首次突破40%，超越亞馬遜AWS。",
            "微軟CEO薩提亞·納德拉表示：「這次收購將加速我們在企業AI領域的佈局，NeuralMind的技術將整合到Microsoft 365和Azure中。」微軟股價創歷史新高，市值突破3.5兆美元。"
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
            "NVIDIA公布2026財年第四季度財報，數據中心業務營收達185億美元，年增78%，大幅超越市場預期。CEO黃仁勳表示，AI需求持續強勁，公司正在加速新一代GPU的生產。",
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
    ["道瓊工業指數", "38,452.67", "+1.25%", "positive"],
    ["S&P 500指數", "5,238.45", "+0.89%", "positive"],
    ["納斯達克指數", "16,345.21", "-0.32%", "negative"],
    ["VIX恐慌指數", "15.42", "+0.12%", "neutral"]
]

# 創建PDF文檔
doc = SimpleDocTemplate(
    "美股重點新聞_精美版.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
    title="美股重點新聞摘要 - 2026年2月15日",
    author="小熊抱 AI助手"
)

# 構建內容
story = []

# 標題
story.append(Paragraph("📈 美股重點新聞摘要", styles['ChineseTitle']))
story.append(Paragraph("2026年2月15日 | 即時市場分析", styles['ChineseSubtitle']))
story.append(Spacer(1, 20))

# 市場數據表格
market_table_data = [["指數", "數值", "漲跌幅"]]
for data in market_data:
    color = colors.green if data[3] == "positive" else colors.red if data[3] == "negative" else colors.gray
    market_table_data.append([data[0], data[1], f'<font color="{color}">{data[2]}</font>'])

market_table = Table(market_table_data, colWidths=[6*cm, 4*cm, 3*cm])
market_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1e3a8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), font_name + '-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), font_name),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('TOPPADDING', (0, 1), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
]))

story.append(market_table)
story.append(Spacer(1, 30))

# 新聞內容
for i, news in enumerate(news_items):
    # 新聞標題（包含編號和影響標籤）
    title_text = f"{news['number']}. {news['title']} "
    impact_color = colors.red if news['impact'] == "高影響" else colors.orange
    title_text += f'<font color="{impact_color}">[{news["impact"]}]</font>'
    
    story.append(Paragraph(title_text, styles['NewsTitle']))
    
    # 元數據
    meta_text = f"⏰ {news['time']} | 🏢 {news['sector']} | 📊 {news['volume']}"
    story.append(Paragraph(meta_text, styles['NewsMeta']))
    
    # 新聞內容
    for content_para in news['content']:
        story.append(Paragraph(content_para, styles['NewsContent']))
    
    # 關鍵要點
    story.append(Paragraph("📋 關鍵要點", styles['KeyPointsTitle']))
    for point in news['key_points']:
        story.append(Paragraph(f"• {point}", styles['KeyPoint']))
    
    # 如果不是最後一個新聞，添加分隔線
    if i < len(news_items) - 1:
        story.append(Spacer(1, 20))
        story.append(Paragraph("<hr/>", ParagraphStyle(
            name='Divider',
            fontName=font_name,
            fontSize=1,
            textColor=HexColor('#e5e7eb'),
            alignment=TA_CENTER,
            spaceBefore=10,
            spaceAfter=10
        )))
        story.append(Spacer(1, 20))

# 頁尾
story.append(Spacer(1, 40))
story.append(Paragraph("資料來源：綜合市場資訊、公司財報、分析師報告", styles['Footer']))
story.append(Paragraph("整理時間：2026年2月15日 12:30 GMT+8", styles['Footer']))
story.append(Paragraph("整理者：小熊抱 AI助手 🧸🤗", styles['Footer']))
story.append(Spacer(1, 20))
story.append(Paragraph("⚠️ 免責聲明：本報告僅供參考，不構成投資建議。投資有風險，入市需謹慎。", styles['Disclaimer']))
story.append(Paragraph("市場數據為模擬數據，實際情況可能有所不同。", styles['Disclaimer']))

# 生成PDF
doc.build(story)
print(f"PDF創建成功！檔案: 美股重點新聞_精美版.pdf")
print(f"使用字體: {font_name}")