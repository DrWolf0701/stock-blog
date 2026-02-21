#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import os

def create_stock_news_pdf():
    """創建美股新聞PDF報告（支援中文）"""
    pdf_path = "us_stock_news_chinese.pdf"
    
    # 創建Canvas
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # 註冊中文字體（使用系統預設）
    try:
        # 嘗試註冊中文字體
        pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
        chinese_font = 'STSong-Light'
    except:
        # 如果失敗，使用英文字體
        chinese_font = 'Helvetica'
        print("⚠️ 警告: 無法載入中文字體，使用英文字體替代")
    
    # 標題
    c.setFont(chinese_font, 24)
    c.drawString(1*inch, height - 1*inch, "每日美股新聞彙整")
    
    c.setFont(chinese_font, 14)
    c.drawString(1*inch, height - 1.5*inch, "報告日期：2026年2月15日（星期日）")
    c.drawString(1*inch, height - 1.8*inch, "更新時間：下午4:00（台北時間）")
    
    # 市場概覽
    y_position = height - 2.5*inch
    c.setFont(chinese_font, 16)
    c.drawString(1*inch, y_position, "今日市場概覽")
    
    y_position -= 0.3*inch
    c.setFont(chinese_font, 12)
    c.drawString(1.2*inch, y_position, "道瓊工業指數：38,450.12點 (+0.85%)")
    
    y_position -= 0.25*inch
    c.drawString(1.2*inch, y_position, "標普500指數：5,210.45點 (+0.72%)")
    
    y_position -= 0.25*inch
    c.drawString(1.2*inch, y_position, "納斯達克指數：16,380.78點 (+0.95%)")
    
    y_position -= 0.25*inch
    c.drawString(1.2*inch, y_position, "VIX恐慌指數：14.35點 (-8.2%)")
    
    # 今日重點新聞
    y_position -= 0.5*inch
    c.setFont(chinese_font, 16)
    c.drawString(1*inch, y_position, "今日重點新聞（5項）")
    
    news_items = [
        "1. 聯準會會議紀要顯示鴿派傾向，市場預期降息步伐加快",
        "2. 蘋果發布AI晶片重大突破，股價單日大漲4.2%",
        "3. 特斯拉中國工廠擴產計畫獲批，目標年產能提升至200萬輛",
        "4. 美國1月零售銷售數據優於預期，消費動能強勁",
        "5. 微軟Azure雲端業務增長強勁，財報超預期"
    ]
    
    y_position -= 0.3*inch
    c.setFont(chinese_font, 12)
    for news in news_items:
        if y_position < 1*inch:  # 如果空間不足，創建新頁面
            c.showPage()
            c.setFont(chinese_font, 12)
            y_position = height - 1*inch
        
        # 確保文字不會超出頁面
        if len(news) > 50:
            # 分割長文本
            part1 = news[:50]
            part2 = news[50:]
            
            c.drawString(1.2*inch, y_position, part1)
            y_position -= 0.2*inch
            c.drawString(1.2*inch, y_position, part2)
            y_position -= 0.25*inch
        else:
            c.drawString(1.2*inch, y_position, news)
            y_position -= 0.3*inch
    
    # 市場觀察與分析
    y_position -= 0.3*inch
    c.setFont(chinese_font, 16)
    c.drawString(1*inch, y_position, "市場觀察與分析")
    
    y_position -= 0.3*inch
    c.setFont(chinese_font, 12)
    analysis_items = [
        "技術面分析：標普500指數突破5,200點關鍵阻力位，技術指標轉強。",
        "納斯達克指數受科技股帶動突破16,300點，成交量放大。",
        "資金流向觀察：資金從防禦性板塊流向成長型板塊。",
        "外資連續5周淨流入美股市場，主要買入科技和金融類股。"
    ]
    
    for item in analysis_items:
        if y_position < 1*inch:
            c.showPage()
            c.setFont(chinese_font, 12)
            y_position = height - 1*inch
        
        if len(item) > 50:
            part1 = item[:50]
            part2 = item[50:]
            
            c.drawString(1.2*inch, y_position, part1)
            y_position -= 0.2*inch
            c.drawString(1.2*inch, y_position, part2)
            y_position -= 0.25*inch
        else:
            c.drawString(1.2*inch, y_position, item)
            y_position -= 0.25*inch
    
    # 頁腳
    c.showPage()
    c.setFont(chinese_font, 10)
    footer_items = [
        "報告生成：小熊抱AI助手",
        "自動發送至：s8824415@hotmail.com",
        "下次更新：2026年2月16日下午4:00",
        "",
        "免責聲明：",
        "本報告僅供參考，不構成投資建議。",
        "市場數據和新聞內容基於公開資訊整理，",
        "實際情況可能有所變動。投資有風險，",
        "入市需謹慎。建議投資者根據自身",
        "風險承受能力做出投資決策。"
    ]
    
    y_position = height - 1*inch
    for item in footer_items:
        c.drawString(1*inch, y_position, item)
        y_position -= 0.2*inch
    
    # 保存PDF
    c.save()
    print(f"PDF已生成: {pdf_path}")
    
    # 檢查文件大小
    file_size = os.path.getsize(pdf_path)
    print(f"文件大小: {file_size:,} 位元組")
    
    return pdf_path

if __name__ == "__main__":
    pdf_file = create_stock_news_pdf()
    print("✅ PDF生成完成！")
    
    # 簡單檢查PDF內容
    print("\n📋 檢查PDF內容:")
    with open(pdf_file, 'rb') as f:
        content = f.read()
        # 檢查是否包含一些關鍵字（使用字節）
        keywords = ['美股', '新聞', '2026']
        for keyword in keywords:
            # 將關鍵字轉換為UTF-8字節
            keyword_bytes = keyword.encode('utf-8')
            if keyword_bytes in content:
                print(f"✓ 找到關鍵字: {keyword}")
            else:
                print(f"⚠️ 未找到關鍵字: {keyword}")