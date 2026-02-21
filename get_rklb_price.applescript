tell application "System Events"
    tell process "富途牛牛"
        set frontmost to true
        delay 1
        
        -- 假設現在已經在RKLB頁面，嘗試獲取價格資訊
        -- 先按Tab切換到價格區域
        keystroke tab
        delay 0.5
        
        -- 嘗試用快捷鍵複製價格資訊
        keystroke "a" using {command down}
        delay 0.5
        keystroke "c" using {command down}
        delay 0.5
        
        -- 從剪貼簿獲取內容
        set priceInfo to do shell script "pbpaste"
        
        -- 如果剪貼簿是空的，嘗試其他方法
        if priceInfo is "" then
            -- 嘗試獲取視窗資訊
            try
                set windowInfo to entire contents of window 1
                return "無法複製價格，但視窗內容可訪問。建議手動查看RKLB頁面。"
            on error
                return "RKLB搜尋成功，請手動查看價格資訊。當前在'搜索'視窗。"
            end try
        else
            return "複製的價格資訊: " & priceInfo
        end if
    end tell
end tell