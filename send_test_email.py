#!/usr/bin/env python3
"""
寄送測試信到 s8824415@gmail.com
使用中央大學校友信箱
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time

def send_test_email():
    """寄送測試郵件"""
    
    # 郵件設定
    sender_email = "a102456014@alumni.ncu.edu.tw"
    receiver_email = "s8824415@gmail.com"
    password = "Penthouse0701"
    
    # 建立郵件內容
    message = MIMEMultipart("alternative")
    message["Subject"] = f"測試郵件 - 熊抱哥助手 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # 純文字版本
    text = f"""熊抱哥助手測試郵件

這是一封來自中央大學校友信箱的測試郵件。

發送時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
發送者: {sender_email}
收件者: {receiver_email}

測試目的: 確認郵件設定正常，可用於自動化通知。

🐻 熊抱哥助手功能測試完成！

如有任何問題，請回覆此郵件。
"""
    
    # HTML 版本
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background-color: #4CAF50; color: white; padding: 10px; text-align: center; border-radius: 5px; }}
        .content {{ padding: 20px; background-color: #f9f9f9; border-radius: 5px; margin-top: 20px; }}
        .footer {{ margin-top: 20px; text-align: center; color: #666; font-size: 12px; }}
        .bear {{ font-size: 24px; text-align: center; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐻 熊抱哥助手測試郵件</h1>
        </div>
        
        <div class="content">
            <p>這是一封來自中央大學校友信箱的測試郵件。</p>
            
            <div class="bear">
                🐻📧✨
            </div>
            
            <h3>📋 郵件資訊</h3>
            <ul>
                <li><strong>發送時間:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
                <li><strong>發送者:</strong> {sender_email}</li>
                <li><strong>收件者:</strong> {receiver_email}</li>
            </ul>
            
            <h3>🎯 測試目的</h3>
            <p>確認郵件設定正常，可用於自動化通知系統。</p>
            
            <h3>✅ 測試項目</h3>
            <ul>
                <li>SMTP 伺服器連線</li>
                <li>郵件發送功能</li>
                <li>HTML 格式支援</li>
                <li>中文編碼正確性</li>
            </ul>
            
            <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <h4 style="margin-top: 0; color: #2e7d32;">📬 郵件發送狀態</h4>
                <p>如果收到此郵件，表示設定成功！</p>
            </div>
        </div>
        
        <div class="footer">
            <p>此為自動化測試郵件，由熊抱哥助手發送</p>
            <p>如有任何問題，請回覆此郵件</p>
            <p>發送時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
    
    # 加入郵件內容
    part1 = MIMEText(text, "plain", "utf-8")
    part2 = MIMEText(html, "html", "utf-8")
    
    message.attach(part1)
    message.attach(part2)
    
    # 嘗試不同的 SMTP 設定
    smtp_configs = [
        {"host": "smtp.alumni.ncu.edu.tw", "port": 587, "tls": True},
        {"host": "smtp.alumni.ncu.edu.tw", "port": 465, "ssl": True},
        {"host": "smtp.alumni.ncu.edu.tw", "port": 25, "tls": False},
    ]
    
    print("📧 開始寄送測試郵件...")
    print(f"發送者: {sender_email}")
    print(f"收件者: {receiver_email}")
    print()
    
    for i, config in enumerate(smtp_configs, 1):
        print(f"嘗試設定 {i}/{len(smtp_configs)}:")
        print(f"  伺服器: {config['host']}:{config['port']}")
        
        try:
            if config.get('ssl'):
                # SSL 連線
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(config['host'], config['port'], context=context, timeout=30)
                print("  連線方式: SSL")
            else:
                # 普通連線 + 可能 TLS
                server = smtplib.SMTP(config['host'], config['port'], timeout=30)
                if config.get('tls'):
                    server.starttls()
                    print("  連線方式: STARTTLS")
                else:
                    print("  連線方式: 普通")
            
            # 登入
            print("  嘗試登入...")
            server.login(sender_email, password)
            print("  ✅ 登入成功")
            
            # 發送郵件
            print("  發送郵件中...")
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("  ✅ 郵件發送成功！")
            
            # 關閉連線
            server.quit()
            print(f"  🎉 使用設定 {i} 發送成功！")
            
            # 記錄成功設定
            with open("email_success_config.txt", "w") as f:
                f.write(f"成功設定: {config}\n")
                f.write(f"時間: {datetime.now()}\n")
                f.write(f"發送者: {sender_email}\n")
                f.write(f"收件者: {receiver_email}\n")
            
            return True, config
            
        except Exception as e:
            print(f"  ❌ 失敗: {type(e).__name__}: {str(e)[:100]}")
            time.sleep(2)  # 等待一下再試下一個
    
    print("\n❌ 所有設定嘗試都失敗")
    return False, None

def main():
    """主程式"""
    print("=" * 60)
    print("🐻 熊抱哥助手 - 郵件測試系統")
    print("=" * 60)
    print(f"測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    success, config = send_test_email()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 測試郵件已成功寄出！")
        print(f"使用設定: {config}")
        print()
        print("📬 請檢查 s8824415@gmail.com 的收件匣：")
        print("   1. 主要收件匣")
        print("   2. 垃圾郵件匣（有可能被誤判）")
        print("   3. 促銷內容或其他分類")
        print()
        print("⏰ 郵件可能需要幾分鐘才會送達")
    else:
        print("❌ 郵件發送失敗")
        print()
        print("🔧 可能原因：")
        print("   1. SMTP 伺服器設定不正確")
        print("   2. 需要學校 VPN 連線")
        print("   3. 帳號密碼錯誤")
        print("   4. 伺服器暫時不可用")
        print()
        print("💡 建議：")
        print("   1. 確認網路連線正常")
        print("   2. 嘗試使用學校 VPN")
        print("   3. 聯繫學校計資中心確認設定")
    
    print("=" * 60)
    
    # 安全提醒
    print("\n🔒 安全提醒：")
    print("   • 此程式不會儲存密碼")
    print("   • 建議定期更改密碼")
    print("   • 避免在公開場合顯示密碼")

if __name__ == "__main__":
    main()