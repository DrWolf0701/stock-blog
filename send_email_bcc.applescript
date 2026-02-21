-- 使用 BCC 發送郵件的 AppleScript
-- 收件人資訊不會顯示在郵件中

on run argv
    set pdfPath to item 1 of argv
    set emailSubject to item 2 of argv
    set emailContent to item 3 of argv
    set recipientList to items 4 thru -1 of argv
    
    tell application "Mail"
        -- 創建新郵件
        set newMessage to make new outgoing message with properties {subject:emailSubject, content:emailContent}
        
        -- 設定密件副本（BCC）
        tell newMessage
            repeat with recipientEmail in recipientList
                make new bcc recipient at end of bcc recipients with properties {address:recipientEmail}
            end repeat
            
            -- 添加附件
            try
                make new attachment with properties {file name:pdfPath} at after the last paragraph
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
end run