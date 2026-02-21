tell application "System Events"
    tell process "富途牛牛"
        set frontmost to true
        delay 1
        
        -- 先確保在RKLB頁面，按F5重新整理
        key code 96 -- F5鍵
        delay 2
        
        -- 嘗試常用快捷鍵獲取資訊
        -- 按1切換到分時圖
        keystroke "1"
        delay 1
        
        -- 按5切換到日K線
        keystroke "5"
        delay 1
        
        -- 按F10查看公司資料
        key code 109 -- F10
        delay 2
        
        -- 按Esc返回
        key code 53 -- Esc
        delay 1
        
        -- 現在應該在技術分析頁面，嘗試獲取一些可見文字
        -- 按Tab多次嘗試找到價格顯示區域
        repeat 3 times
            keystroke tab
            delay 0.5
        end repeat
        
        -- 嘗試用AppleScript的UI瀏覽獲取可見文字
        try
            -- 獲取所有UI元素
            set uiElements to entire contents of window 1
            
            -- 尋找包含數字的文字（可能是價格）
            set priceTexts to {}
            repeat with elem in uiElements
                try
                    set elemClass to class of elem
                    if elemClass is static text then
                        set txtValue to value of elem
                        -- 檢查是否包含數字和點（價格格式）
                        if txtValue contains "." and (txtValue contains "0" or txtValue contains "1" or txtValue contains "2" or txtValue contains "3" or txtValue contains "4" or txtValue contains "5" or txtValue contains "6" or txtValue contains "7" or txtValue contains "8" or txtValue contains "9") then
                            set end of priceTexts to txtValue
                        end if
                    end if
                on error
                    -- 跳過無法訪問的元素
                end try
            end repeat
            
            if (count of priceTexts) > 0 then
                return "找到可能的價格資訊: " & (item 1 of priceTexts)
            else
                return "已操作富途牛牛查看RKLB，但無法自動讀取價格。請手動查看螢幕上的RKLB頁面。"
            end if
            
        on error errMsg
            return "UI訪問受限。已成功操作富途牛牛查看RKLB，請查看螢幕上的顯示。錯誤: " & errMsg
        end try
    end tell
end tell