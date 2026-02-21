#!/usr/bin/env python3
"""
測試中央大學校友信箱連線
安全測試，不儲存任何資訊
"""

import poplib
import smtplib
import ssl
from email.mime.text import MIMEText
from datetime import datetime

def test_pop3_connection():
    """測試 POP3 收件連線"""
    print("🔍 測試 POP3 收件連線...")
    
    try:
        # 連線到 POP3 伺服器 (SSL)
        pop3_server = "pop3.alumni.ncu.edu.tw"
        port = 995
        
        print(f"  連線到: {pop3_server}:{port}")
        mail = poplib.POP3_SSL(pop3_server, port)
        print("  ✅ SSL 連線建立成功")
        
        # 嘗試登入
        email = "a102456014@alumni.ncu.edu.tw"
        password = "Penthouse0701"
        
        mail.user(email)
        mail.pass_(password)
        print("  ✅ POP3 登入成功")
        
        # 取得郵件統計
        num_messages = len(mail.list()[1])
        print(f"  📧 信箱中有 {num_messages} 封郵件")
        
        # 安全登出
        mail.quit()
        print("  ✅ POP3 連線測試完成")
        return True
        
    except Exception as e:
        print(f"  ❌ POP3 連線失敗: {type(e).__name__}: {e}")
        return False

def test_smtp_connection():
    """測試 SMTP 發件連線"""
    print("\n🔍 測試 SMTP 發件連線...")
    
    try:
        # 嘗試常見的 SMTP 連接埠
        smtp_server = "smtp.alumni.ncu.edu.tw"
        test_ports = [587, 465, 25]
        
        for port in test_ports:
            print(f"  嘗試連接埠 {port}...")
            try:
                if port == 465:
                    # SSL 連接
                    server = smtplib.SMTP_SSL(smtp_server, port, timeout=10)
                else:
                    # TLS 連接
                    server = smtplib.SMTP(smtp_server, port, timeout=10)
                    if port == 587:
                        server.starttls()
                
                print(f"    ✅ 連接埠 {port} 連線成功")
                
                # 測試登入
                email = "a102456014@alumni.ncu.edu.tw"
                password = "Penthouse0701"
                
                server.login(email, password)
                print(f"    ✅ 連接埠 {port} 登入成功")
                
                server.quit()
                print(f"  ✅ SMTP 連接埠 {port} 測試完成")
                return port
                
            except Exception as e:
                print(f"    ❌ 連接埠 {port} 失敗: {type(e).__name__}")
                continue
        
        print("  ❌ 所有 SMTP 連接埠測試失敗")
        return None
        
    except Exception as e:
        print(f"  ❌ SMTP 連線測試異常: {type(e).__name__}: {e}")
        return None

def main():
    """主測試程式"""
    print("=" * 60)
    print("📧 中央大學校友信箱連線測試")
    print("=" * 60)
    print(f"時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"帳號: a102456014@alumni.ncu.edu.tw")
    print()
    
    # 測試 POP3
    pop3_success = test_pop3_connection()
    
    # 測試 SMTP
    smtp_port = test_smtp_connection()
    
    print("\n" + "=" * 60)
    print("📊 測試結果總結:")
    
    if pop3_success:
        print("  ✅ POP3 收件: 連線正常 (連接埠 995)")
    else:
        print("  ❌ POP3 收件: 連線失敗")
    
    if smtp_port:
        print(f"  ✅ SMTP 發件: 連線正常 (連接埠 {smtp_port})")
    else:
        print("  ❌ SMTP 發件: 連線失敗")
    
    print("\n💡 建議:")
    if pop3_success and smtp_port:
        print("  所有連線正常，可以進行郵件 App 設定")
    elif pop3_success and not smtp_port:
        print("  收件正常，發件需要確認 SMTP 設定")
    else:
        print("  需要檢查網路或伺服器設定")
    
    print("=" * 60)
    
    # 安全提醒
    print("\n🔒 安全提醒:")
    print("  • 此測試程式不會儲存任何帳號資訊")
    print("  • 測試完成後所有連線都會關閉")
    print("  • 建議在正式設定後更改測試密碼")

if __name__ == "__main__":
    main()