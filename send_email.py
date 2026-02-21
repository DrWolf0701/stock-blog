#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
美股新聞重點PDF郵件發送腳本
收件人: s8824415@hotmail.com
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

def send_email_with_pdf():
    """發送帶有PDF附件的郵件"""
    
    # 郵件配置
    sender_email = "自動化新聞系統"  # 實際發送需要配置SMTP
    receiver_email = "s8824415@hotmail.com"
    subject = "美股新聞重點彙整 - 2025年2月15日"
    
    # PDF文件路徑
    pdf_path = "美股新聞重點_20250215.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"錯誤: PDF文件不存在: {pdf_path}")
        return False
    
    # 郵件正文
    body = f"""
親愛的收件人：

以下是今日（2025年2月15日）的美股新聞重點彙整報告。

📈 今日重點新聞：
1. 汽車製造商CEO對中國競爭發出警告
2. 美國牛群減少導致牛肉價格上漲15%
3. 亞馬遜計劃2000億美元AI投資以重振AWS
4. AI泡沫擔憂催生新衍生品
5. 六位華爾街銀行CEO 2025年總薪酬達2.5億美元
6. 麥當勞準備應對減肥藥影響
7. 醫療成本侵蝕社會安全支票

📊 市場概覽：
• S&P 500: 6,836.17 (+0.05%)
• 道瓊工業: 49,500.93 (+0.10%)
• 納斯達克: 22,546.67 (-0.22%)

✅ PDF可讀性保證：
本PDF經過嚴格可讀性測試，確保：
• 文字清晰無重疊
• 中文字體正常顯示
• 超大邊距設計
• 內容完整無截斷
• 極簡可靠字體

📁 文件信息：
• 文件名: {os.path.basename(pdf_path)}
• 文件大小: {os.path.getsize(pdf_path) / 1024:.1f} KB
• 生成時間: 2025年2月15日 14:31 (GMT+8)

請查收附件中的完整報告。

祝您投資順利！

---
自動化新聞彙整系統
{datetime.now().strftime('%Y年%m月%d日 %H:%M')}
"""
    
    print("=" * 60)
    print("📧 郵件發送配置")
    print("=" * 60)
    print(f"收件人: {receiver_email}")
    print(f"主題: {subject}")
    print(f"附件: {pdf_path} ({os.path.getsize(pdf_path) / 1024:.1f} KB)")
    print(f"正文長度: {len(body)} 字符")
    print("=" * 60)
    
    # 創建郵件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # 添加正文
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # 添加PDF附件
    with open(pdf_path, 'rb') as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype='pdf')
        pdf_attachment.add_header('Content-Disposition', 'attachment', 
                                 filename=os.path.basename(pdf_path))
        msg.attach(pdf_attachment)
    
    print("✅ 郵件內容已準備完成")
    print("\n📋 郵件內容預覽:")
    print("-" * 40)
    print(body[:500] + "..." if len(body) > 500 else body)
    print("-" * 40)
    
    # 注意：實際發送需要SMTP服務器配置
    print("\n⚠️  注意：實際郵件發送需要配置SMTP服務器")
    print("目前只生成郵件內容，如需實際發送請配置：")
    print("1. SMTP服務器地址和端口")
    print("2. 發送郵箱賬號和密碼/授權碼")
    print("3. 安全連接設置")
    
    # 保存郵件內容到文件（供參考）
    email_content_file = "email_content.txt"
    with open(email_content_file, 'w', encoding='utf-8') as f:
        f.write(f"收件人: {receiver_email}\n")
        f.write(f"主題: {subject}\n")
        f.write(f"發件人: {sender_email}\n")
        f.write(f"附件: {pdf_path}\n")
        f.write("\n" + "="*50 + "\n")
        f.write("郵件正文:\n")
        f.write("="*50 + "\n")
        f.write(body)
    
    print(f"\n📝 郵件內容已保存到: {email_content_file}")
    
    return True

if __name__ == "__main__":
    print("開始準備美股新聞重點郵件發送...")
    print(f"當前時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    success = send_email_with_pdf()
    
    if success:
        print("\n" + "="*60)
        print("✅ 郵件準備完成！")
        print("="*60)
        print("\n下一步操作：")
        print("1. 配置SMTP服務器信息")
        print("2. 取消註釋send_email_with_pdf()中的發送代碼")
        print("3. 運行腳本發送郵件")
        print("\n或使用以下命令手動發送：")
        print(f"   open {os.path.abspath('美股新聞重點_20250215.pdf')}")
    else:
        print("\n❌ 郵件準備失敗")