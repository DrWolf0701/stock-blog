-- AppleScript to send email with PDF attachment
tell application "Mail"
    set newMessage to make new outgoing message with properties {subject:"每日美股新聞彙整 - 2026年2月15日 🧸🤗", content:"親愛的Chris先生：

這是您的每日美股新聞彙整報告！

📅 日期：2026年2月15日
⚠️ 重要說明：因目前系統缺少 Brave Search API Key，本次報告為市場概況整理，非即時新聞詳情。

報告內容包含：
✓ 美股市場周末休市說明
✓ FED政策動向分析
✓ 科技股波動概況
✓ 加密貨幣市場連動性
✓ 國際地緣政治與貿易政策
✓ 能源與商品價格波動

敬請查收PDF附件。

祝您投資順利！

小熊抱 BearHug 🧸🤗
"}
    
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
        
        -- Attach PDF file
        tell content
            make new attachment with properties {file name:"/Users/yu-tsehsiao/.openclaw/workspace/us_stock_news_2026-02-15.pdf"} at after last paragraph
        end tell
        
        -- Send the message
        send
    end tell
end tell

return "Email sent successfully to s8824415@hotmail.com"