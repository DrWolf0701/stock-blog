tell application "Mail"
    -- 創建新郵件
    set newMessage to make new outgoing message with properties {subject:"📈 美股新聞彙整報告 - 2026年2月16日（下午4點版）", content:"這是今天下午4點的美股新聞彙整報告。

包含最新的美股市場重點新聞和分析。

請查看附件中的 PDF 報告。"}
    
    -- 設定收件人
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
        make new to recipient at end of to recipients with properties {address:"Linbojing@hotmail.com"}
        
        -- 添加附件
        try
            make new attachment with properties {file name:"/Users/yu-tsehsiao/.openclaw/workspace/美股新聞彙整_20260216.pdf"} at after the last paragraph
        on error errMsg
            log "附件添加失敗: " & errMsg
        end try
    end tell
    
    -- 發送郵件
    send newMessage
    log "美股新聞報告郵件已成功發送！"
end tell