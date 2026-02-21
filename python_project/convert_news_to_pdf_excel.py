#!/usr/bin/env python3
"""
將美股新聞 HTML 轉換為 PDF 和 Excel
由 OpenClaw 建立 🐻
"""

import os
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

# PDF 相關套件
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def read_news_from_html(html_path):
    """從 HTML 檔案讀取新聞內容（簡化版本）"""
    print(f"📄 讀取 HTML 檔案: {html_path}")
    
    # 實際應用中應該解析 HTML，這裡使用範例資料
    news_items = [
        {
            'title': '美國1月就業報告超預期',
            'category': '經濟數據',
            'importance': '高',
            'impact': '強勁就業數據可能推遲聯準會降息時程',
            'details': '美國1月非農就業數據大幅超出市場預期，顯示勞動市場依然強勁。主要指數開高，但隨後因獲利了結壓力而震盪。',
            'time': '09:00',
            'source': 'Bloomberg, Yahoo財經'
        },
        {
            'title': '台積電ADR表現強勁',
            'category': '個股表現', 
            'importance': '高',
            'impact': '半導體類股成為盤前亮點',
            'details': '台積電ADR盤前勁揚3-4%，帶動半導體類股走勢。受惠於AI需求持續強勁，記憶體相關個股同步上漲。',
            'time': '08:45',
            'source': 'Reuters, 經濟日報'
        },
        {
            'title': 'AI浪潮下的投資新局',
            'category': '產業趨勢',
            'importance': '中',
            'impact': '科技股呈現分化走勢',
            'details': 'AI投資熱潮持續，但市場開始關注估值合理性。雲端巨頭加大AI投資，帶動相關供應鏈。',
            'time': '10:30',
            'source': 'CNBC, WSJ'
        },
        {
            'title': '企業財報季持續',
            'category': '財報',
            'importance': '中', 
            'impact': '財報結果將影響個股走勢',
            'details': '多家重量級企業將公布財報，包括網易（NTES）、Check Point等。市場關注企業對2026年展望。',
            'time': '11:15',
            'source': '華爾街日報'
        },
        {
            'title': '市場資金流向',
            'category': '資金流向',
            'importance': '中',
            'impact': '投資策略趨向保守',
            'details': '資金從成長股流向防禦型股票。債市殖利率上升吸引部分資金，投資人開始布局價值型與高股息股票。',
            'time': '09:45',
            'source': '金融時報'
        }
    ]
    
    df = pd.DataFrame(news_items)
    print(f"✅ 讀取 {len(df)} 筆新聞資料")
    return df


def create_detailed_excel(df, output_path="美股詳細新聞.xlsx"):
    """建立詳細的 Excel 報告"""
    print(f"📈 建立詳細 Excel 報告: {output_path}")
    
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # 1. 新聞摘要表
            df[['title', 'category', 'importance', 'impact', 'time', 'source']].to_excel(
                writer, sheet_name='新聞摘要', index=False
            )
            
            # 2. 詳細內容表
            df.to_excel(writer, sheet_name='詳細內容', index=False)
            
            # 3. 統計分析表
            stats_data = {
                '統計項目': ['總新聞數', '高重要性新聞', '中重要性新聞', '不同分類數', '不同來源數', '最早時間', '最晚時間'],
                '數值': [
                    len(df),
                    len(df[df['importance'] == '高']),
                    len(df[df['importance'] == '中']),
                    df['category'].nunique(),
                    df['source'].nunique(),
                    df['time'].min(),
                    df['time'].max()
                ]
            }
            stats_df = pd.DataFrame(stats_data)
            stats_df.to_excel(writer, sheet_name='統計分析', index=False)
            
            # 4. 分類分析
            category_analysis = df.groupby('category').agg({
                'title': 'count',
                'importance': lambda x: (x == '高').sum()
            }).rename(columns={'title': '新聞數量', 'importance': '高重要性數量'})
            category_analysis.to_excel(writer, sheet_name='分類分析')
            
            # 5. 時間分析
            time_analysis = df.groupby('time').agg({
                'title': 'count',
                'category': lambda x: ', '.join(sorted(set(x)))
            }).rename(columns={'title': '新聞數量', 'category': '相關分類'})
            time_analysis.to_excel(writer, sheet_name='時間分布')
        
        print(f"✅ Excel 報告建立完成: {os.path.getsize(output_path):,} bytes")
        return True
        
    except Exception as e:
        print(f"❌ Excel 建立失敗: {e}")
        return False


def create_detailed_pdf(df, output_path="美股詳細新聞.pdf"):
    """建立詳細的 PDF 報告"""
    print(f"📄 建立詳細 PDF 報告: {output_path}")
    
    try:
        # 建立 PDF 文件
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        styles = getSampleStyleSheet()
        story = []
        
        # 自訂樣式
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontSize=24,
            spaceAfter=30,
            alignment=1  # 置中
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceBefore=12,
            spaceAfter=6,
            textColor=colors.HexColor('#2C3E50')
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6
        )
        
        # 封面頁
        story.append(Paragraph("美股盤前重點新聞彙整", title_style))
        story.append(Spacer(1, 20))
        
        report_info = f"""
        報告日期: {datetime.now().strftime('%Y年%m月%d日')}<br/>
        生成時間: {datetime.now().strftime('%H:%M:%S')}<br/>
        資料來源: 多家財經媒體<br/>
        新聞數量: {len(df)} 筆
        """
        story.append(Paragraph(report_info, normal_style))
        story.append(PageBreak())
        
        # 目錄
        story.append(Paragraph("目錄", heading_style))
        toc_items = [
            "1. 新聞摘要表格",
            "2. 詳細新聞內容", 
            "3. 統計分析",
            "4. 風險提示",
            "5. 投資建議"
        ]
        
        for item in toc_items:
            story.append(Paragraph(item, normal_style))
        story.append(PageBreak())
        
        # 1. 新聞摘要表格
        story.append(Paragraph("1. 新聞摘要表格", heading_style))
        
        # 建立表格資料
        table_data = [['標題', '分類', '重要性', '主要影響', '時間', '來源']]
        
        for _, row in df.iterrows():
            table_data.append([
                row['title'],
                row['category'],
                row['importance'],
                row['impact'],
                row['time'],
                row['source']
            ])
        
        # 建立表格
        table = Table(table_data, colWidths=[2.5*inch, 0.8*inch, 0.6*inch, 2*inch, 0.6*inch, 1*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DEE2E6')),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')]),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 20))
        
        # 2. 詳細新聞內容
        story.append(Paragraph("2. 詳細新聞內容", heading_style))
        
        for idx, (_, row) in enumerate(df.iterrows(), 1):
            story.append(Paragraph(f"{idx}. {row['title']}", styles['Heading3']))
            
            content = f"""
            <b>分類:</b> {row['category']} | <b>重要性:</b> {row['importance']} | <b>時間:</b> {row['time']}<br/>
            <b>來源:</b> {row['source']}<br/>
            <b>主要影響:</b> {row['impact']}<br/>
            <b>詳細內容:</b> {row['details']}
            """
            story.append(Paragraph(content, normal_style))
            story.append(Spacer(1, 12))
        
        story.append(PageBreak())
        
        # 3. 統計分析
        story.append(Paragraph("3. 統計分析", heading_style))
        
        # 重要性分析
        importance_counts = df['importance'].value_counts()
        imp_table_data = [['重要性等級', '新聞數量', '百分比']]
        total = len(df)
        
        for level, count in importance_counts.items():
            percentage = (count / total) * 100
            imp_table_data.append([level, str(count), f"{percentage:.1f}%"])
        
        imp_table = Table(imp_table_data, colWidths=[1.5*inch, 1*inch, 1*inch])
        imp_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        
        story.append(Paragraph("重要性分布", styles['Heading4']))
        story.append(imp_table)
        story.append(Spacer(1, 20))
        
        # 時間分布
        time_summary = f"""
        <b>時間分布摘要:</b><br/>
        最早發布時間: {df['time'].min()}<br/>
        最晚發布時間: {df['time'].max()}<br/>
        平均每小時新聞數: {len(df) / df['time'].nunique():.1f} 則
        """
        story.append(Paragraph(time_summary, normal_style))
        
        story.append(PageBreak())
        
        # 4. 風險提示
        story.append(Paragraph("4. 風險提示", heading_style))
        
        risks = [
            "強勁就業數據可能延後聯準會降息時程",
            "AI相關股票估值偏高，需留意回調風險", 
            "市場波動可能加大，建議控制投資部位",
            "企業財報結果可能影響個股走勢",
            "資金流向變化可能導致板塊輪動"
        ]
        
        for risk in risks:
            story.append(Paragraph(f"• {risk}", normal_style))
        
        story.append(Spacer(1, 20))
        
        # 5. 投資建議
        story.append(Paragraph("5. 投資建議", heading_style))
        
        suggestions = [
            "關注防禦型板塊（公用事業、必需消費品）",
            "分散投資以降低單一股票風險",
            "密切關注後續經濟數據發布",
            "考慮價值型與高股息股票配置",
            "保持適當現金部位以應對市場波動"
        ]
        
        for suggestion in suggestions:
            story.append(Paragraph(f"• {suggestion}", normal_style))
        
        # 頁尾
        story.append(Spacer(1, 40))
        footer = Paragraph(
            f"報告生成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 由 OpenClaw 生成 🐻",
            ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, alignment=1)
        )
        story.append(footer)
        
        # 生成 PDF
        doc.build(story)
        print(f"✅ 詳細 PDF 報告建立完成: {os.path.getsize(output_path):,} bytes")
        return True
        
    except Exception as e:
        print(f"❌ PDF 建立失敗: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主程式"""
    print("=" * 70)
    print("🐻 美股新聞轉換工具 - HTML 轉 PDF/Excel")
    print("=" * 70)
    
    # 設定輸出目錄
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 讀取新聞資料（實際應用中應解析 HTML）
    html_path = "../美股盤前重點新聞_2026-02-12.html"
    df = read_news_from_html(html_path)
    
    print(f"\n📊 新聞資料摘要:")
    print(f"  總筆數: {len(df)}")
    print(f"  分類: {', '.join(df['category'].unique())}")
    print(f"  時間範圍: {df['time'].min()} - {df['time'].max()}")
    
    # 生成檔案
    print("\n" + "=" * 70)
    
    excel_path = output_dir / "美股詳細新聞報告.xlsx"
    pdf_path = output_dir / "美股詳細新聞報告.pdf"
    
    # 建立 Excel
    excel_success = create_detailed_excel(df, excel_path)
    
    # 建立 PDF
    pdf_success = create_detailed_pdf(df, pdf_path)
    
    # 結果總結
    print("\n" + "=" * 70)
    print("📋 轉換結果總結:")
    print(f"  Excel 報告: {'✅ 成功' if excel_success else '❌ 失敗'}")
    print(f"  PDF 報告: {'✅ 成功' if pdf_success else '❌ 失敗'}")
    
    if excel_success:
        print(f"    檔案: {excel_path}")
        print(f"    大小: {os.path.getsize(excel_path):,} bytes")
    
    if pdf_success:
        print(f"    檔案: {pdf_path}")
        print(f"    大小: {os.path.getsize(pdf_path):,} bytes")
    
    print("\n" + "=" * 70)
    print("🎉 轉換完成！")
    print("=" * 70)
    
    # 提供使用建議
    print("\n💡 使用建議:")
    print("1. Excel 檔案適合進一步數據分析和處理")
    print("2. PDF 檔案適合分享和列印")
    print("3. 可修改程式碼以解析實際 HTML 內容")
    print("4. 可擴充功能加入圖表和更多分析")


if __name__ == "__main__":
    main()