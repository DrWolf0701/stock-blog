#!/bin/bash

# 可靠的郵件發送腳本
# 用於發送美股新聞報告

PDF_PATH="$1"
SUBJECT="$2"
CONTENT="$3"
RECIPIENTS="$4"

# 檢查檔案是否存在
if [ ! -f "$PDF_PATH" ]; then
    echo "錯誤：PDF 檔案不存在 - $PDF_PATH"
    exit 1
fi

# 方法1：嘗試使用 macOS 郵件應用程式
echo "嘗試使用 macOS 郵件應用程式發送..."
osascript <<EOF
tell application "Mail"
    set newMessage to make new outgoing message with properties {subject:"$SUBJECT", content:"$CONTENT"}
    
    tell newMessage
        -- 設定收件人
        $(echo "$RECIPIENTS" | tr ',' '\n' | while read email; do
            echo "make new to recipient at end of to recipients with properties {address:\"$email\"}"
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
    log "郵件已成功發送！"
    return true
end tell
EOF

if [ $? -eq 0 ]; then
    echo "✅ 郵件已透過 macOS 郵件應用程式成功發送"
    exit 0
fi

# 方法2：如果失敗，使用 mail 命令
echo "嘗試使用 mail 命令發送..."
echo "$CONTENT" | mail -s "$SUBJECT" -a "$PDF_PATH" $(echo "$RECIPIENTS" | tr ',' ' ')

if [ $? -eq 0 ]; then
    echo "✅ 郵件已透過 mail 命令成功發送"
    exit 0
fi

echo "❌ 所有郵件發送方法都失敗了"
exit 1