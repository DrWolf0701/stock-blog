#!/usr/bin/env python3
"""
簡單 PDF 生成器 - 修正版本
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def create_simple_pdf(filename="simple_news.pdf"):
    """建立簡單的 PDF 檔案"""
    print(f"📄 建立簡單 PDF: {filename}")
    
    try:
        # 建立 PDF
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        
        # 標題
        c.setFont("Helvetica-Bold", 20)
        c.drawString(100, height - 100, "美股盤前重點新聞彙整")
        
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 130, f"生成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 新聞項目
        y_position = height - 180
        news_items = [
            ("美國1月就業報告超預期", "經濟數據", "高", "可能推遲降息"),
            ("台積電ADR勁揚3-4%", "個股表現", "高", "半導體類股走強"),
            ("AI投資熱潮持續", "產業趨勢", "中", "估值受關注"),
            ("企業財報季進行中", "財報", "中", "關注企業展望"),
            ("資金流向防禦型股票", "資金流向", "中", "策略趨保守")
        ]
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_position, "重點新聞摘要:")
        y_position -= 30
        
        c.setFont("Helvetica", 10)
        for i, (title, category, importance, impact) in enumerate(news_items, 1):
            # 設定重要性顏色
            if importance == '高':
                c.setFillColor(colors.red)
            else:
                c.setFillColor(colors.black)
            
            c.drawString(120, y_position, f"{i}. {title}")
            c.setFillColor(colors.black)
            
            c.setFont("Helvetica-Oblique", 9)
            c.drawString(140, y_position - 15, f"分類: {category} | 重要性: {importance} | 影響: {impact}")
            c.setFont("Helvetica", 10)
            
            y_position -= 40
            
            # 檢查是否需要換頁
            if y_position < 100:
                c.showPage()
                y_position = height - 100
                c.setFont("Helvetica", 10)
        
        # 風險提示
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "風險提示:")
        y_position -= 20
        
        c.setFont("Helvetica", 10)
        risks = [
            "• 強勁就業可能延後降息時程",
            "• AI股估值偏高需留意回調風險",
            "• 市場波動可能加大，建議控制部位"
        ]
        
        for risk in risks:
            c.drawString(120, y_position, risk)
            y_position -= 20
        
        # 頁尾
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(100, 50, f"由 OpenClaw 生成 🐻 | 頁面 1")
        
        # 儲存 PDF
        c.save()
        print(f"✅ PDF 建立完成: {os.path.getsize(filename):,} bytes")
        return True
        
    except Exception as e:
        print(f"❌ PDF 建立失敗: {e}")
        return False


def main():
    """主程式"""
    print("=" * 60)
    print("🐻 簡單 PDF 生成器")
    print("=" * 60)
    
    # 建立 PDF
    pdf_success = create_simple_pdf("output/美股新聞簡報.pdf")
    
    # 檢查結果
    if pdf_success:
        print(f"\n✅ PDF 檔案已建立: output/美股新聞簡報.pdf")
        print(f"   檔案大小: {os.path.getsize('output/美股新聞簡報.pdf'):,} bytes")
    else:
        print("\n❌ PDF 建立失敗")
    
    print("\n" + "=" * 60)
    print("🎉 程式執行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()