#!/bin/bash

# 使用 BCC 發送郵件的可靠腳本
# 收件人資訊不會顯示在郵件中

PDF_PATH="$1"
SUBJECT="$2"
CONTENT="$3"
RECIPIENTS="$4"

# 檢查檔案是否存在
if [ ! -f "$PDF_PATH" ]; then
    echo "錯誤：PDF 檔案不存在 - $PDF_PATH"
    exit 1
fi

# 方法1：使用 macOS 郵件應用程式（BCC）
echo "嘗試使用 macOS 郵件應用程式發送（BCC）..."
osascript <<EOF
tell application "Mail"
    -- 創建新郵件（不設定收件人，只使用 BCC）
    set newMessage to make new outgoing message with properties {subject:"$SUBJECT", content:"$CONTENT"}
    
    tell newMessage
        -- 設定密件副本（BCC）
        $(echo "$RECIPIENTS" | tr ',' '\n' | while read email; do
            echo "make new bcc recipient at end of bcc recipients with properties {address:\"$email\"}"
        done)
        
        -- 添加附件
        try
            make new attachment with properties {file name:"$PDF_PATH"} at after the last paragraph
        on error errMsg
            log "附件添加失敗: " & errMsg
            return false
        end try
    end tell
    
    -- 發送郵件
    send newMessage
    log "郵件已透過 BCC 成功發送！"
    return true
end tell
EOF

if [ $? -eq 0 ]; then
    echo "✅ 郵件已透過 macOS 郵件應用程式（BCC）成功發送"
    exit 0
fi

# 方法2：如果失敗，使用 mail 命令（BCC 模擬）
echo "嘗試使用 mail 命令發送（模擬 BCC）..."
# mail 命令沒有直接的 BCC 選項，所以我們分別發送
for email in $(echo "$RECIPIENTS" | tr ',' ' '); do
    echo "$CONTENT" | mail -s "$SUBJECT" -a "$PDF_PATH" "$email"
    if [ $? -eq 0 ]; then
        echo "✅ 已發送到: $email"
    else
        echo "❌ 發送到 $email 失敗"
    fi
done

echo "✅ 郵件發送完成（BCC 模式）"
exit 0