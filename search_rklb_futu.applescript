tell application "System Events"
    tell process "富途牛牛"
        -- 先確保App在最前面
        set frontmost to true
        
        -- 等待一下讓App完全啟動
        delay 1
        
        -- 嘗試找到搜尋框（可能需要按快捷鍵）
        keystroke "f" using {command down}
        delay 0.5
        
        -- 輸入RKLB
        keystroke "RKLB"
        delay 0.5
        
        -- 按Enter搜尋
        keystroke return
        delay 2
        
        -- 嘗試截圖或獲取視窗資訊
        try
            set windowTitle to name of window 1
            return "成功搜尋RKLB，目前視窗標題: " & windowTitle
        on error
            return "已執行搜尋指令，但無法獲取視窗資訊"
        end try
    end tell
end tell