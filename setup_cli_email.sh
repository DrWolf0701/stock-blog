#!/bin/bash
# 設定命令列郵件工具

echo "📧 設定命令列郵件工具..."
echo "========================================"

# 1. 安裝必要工具
echo "1. 安裝郵件工具..."
brew install mutt msmtp fetchmail

# 2. 建立設定目錄
echo "2. 建立設定目錄..."
mkdir -p ~/.mutt
mkdir -p ~/.msmtp

# 3. 設定 msmtp (發信)
echo "3. 設定 msmtp 發信..."
cat > ~/.msmtprc << EOF
# Central University Alumni Email
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/cert.pem
logfile        ~/.msmtp.log

# Account
account        ncu_alumni
host           smtp.alumni.ncu.edu.tw
port           587
from           a102456014@alumni.ncu.edu.tw
user           a102456014@alumni.ncu.edu.tw
password       Penthouse0701
tls_starttls   on

# Set default account
account default : ncu_alumni
EOF

chmod 600 ~/.msmtprc
echo "✅ msmtp 設定完成"

# 4. 設定 mutt (收發信)
echo "4. 設定 mutt 收發信..."
cat > ~/.muttrc << EOF
# Mutt configuration for NCU Alumni Email

# Basic settings
set edit_headers = yes
set envelope_from = yes
set copy = no
set move = no
set include = yes
set reply_to = yes
set fast_reply = yes

# Mailboxes
set mbox_type = Maildir
set folder = ~/Mail
set spoolfile = "+INBOX"
set record = "+Sent"
set postponed = "+Drafts"

# SMTP settings (using msmtp)
set sendmail = "/opt/homebrew/bin/msmtp"
set use_from = yes
set realname = "Your Name"
set from = "a102456014@alumni.ncu.edu.tw"

# IMAP/POP3 settings (收信)
set pop_host = "pop3.alumni.ncu.edu.tw"
set pop_user = "a102456014@alumni.ncu.edu.tw"
set pop_pass = "Penthouse0701"
set pop_ssl = yes
set pop_ssl_force = yes

# Display settings
set pager_index_lines = 10
set pager_context = 5
set pager_stop
set menu_scroll
set smart_wrap
set tilde

# Colors
color normal white black
color indicator black yellow
color attachment yellow black
color search white blue
color status yellow blue
color tree red black
color header red black
color error red white

# Key bindings
bind pager j next-line
bind pager k previous-line
bind pager \Cf next-page
bind pager \Cb previous-page
EOF

echo "✅ mutt 設定完成"

# 5. 建立測試腳本
echo "5. 建立測試腳本..."
cat > ~/test_email.sh << 'EOF'
#!/bin/bash
echo "📧 測試中央大學校友信箱"
echo "========================"

# 測試發信
echo "1. 測試發信功能..."
cat > /tmp/test_email.txt << MAIL
To: a102456014@alumni.ncu.edu.tw
From: a102456014@alumni.ncu.edu.tw
Subject: 測試郵件 $(date '+%Y-%m-%d %H:%M:%S')

這是一封測試郵件，確認郵件設定正常。

發送時間: $(date '+%Y-%m-%d %H:%M:%S')
發送者: a102456014@alumni.ncu.edu.tw

測試完成！
MAIL

echo "   發送測試郵件..."
cat /tmp/test_email.txt | msmtp a102456014@alumni.ncu.edu.tw
if [ $? -eq 0 ]; then
    echo "   ✅ 發信測試成功"
else
    echo "   ❌ 發信測試失敗"
fi

# 測試收信
echo ""
echo "2. 測試收信功能..."
echo "   使用 mutt 檢查郵件..."
echo "   按 'q' 退出 mutt"

# 建立臨時 muttrc 只收信
cat > /tmp/mutt_test.muttrc << MUTT
set pop_host = "pop3.alumni.ncu.edu.tw"
set pop_user = "a102456014@alumni.ncu.edu.tw"
set pop_pass = "Penthouse0701"
set pop_ssl = yes
set pop_ssl_force = yes
MUTT

echo ""
echo "💡 使用方式："
echo "   發信: echo '內容' | msmtp 收件人"
echo "   收信: mutt -F ~/.muttrc"
echo "   完整介面: mutt"
EOF

chmod +x ~/test_email.sh
echo "✅ 測試腳本建立完成"

echo ""
echo "========================================"
echo "🎉 命令列郵件工具設定完成！"
echo ""
echo "📋 可用指令："
echo "   1. 測試郵件: ~/test_email.sh"
echo "   2. 收發信: mutt"
echo "   3. 只發信: echo '內容' | msmtp 收件人"
echo ""
echo "🔧 設定檔案位置："
echo "   • 發信設定: ~/.msmtprc"
echo "   • 收發信設定: ~/.muttrc"
echo "   • 測試腳本: ~/test_email.sh"
echo "========================================"