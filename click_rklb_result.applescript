tell application "System Events"
    tell process "富途牛牛"
        set frontmost to true
        delay 1
        
        -- 假設現在在搜尋結果頁面，RKLB應該是第一個結果
        -- 按向下鍵選擇第一個結果
        key code 125 -- 向下鍵
        delay 0.5
        
        -- 按Enter進入詳細頁面
        keystroke return
        delay 2
        
        -- 等待頁面加載
        delay 2
        
        -- 嘗試獲取當前視窗標題
        try
            set windowTitle to name of window 1
            return "已點擊RKLB結果，進入詳細頁面。當前視窗標題: " & windowTitle
        on error
            return "已點擊RKLB結果，應該已進入股票詳細頁面。"
        end try
    end tell
end tell