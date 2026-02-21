tell application "System Events"
    tell process "富途牛牛"
        set frontmost to true
        delay 1
        
        -- 獲取當前視窗的所有UI元素資訊
        set output to "=== 富途牛牛視窗分析 ===\n"
        
        try
            -- 獲取視窗標題
            set winTitle to name of window 1
            set output to output & "視窗標題: " & winTitle & "\n\n"
            
            -- 獲取所有靜態文字（可能是價格資訊）
            set textsList to static texts of window 1
            set textCount to count of textsList
            
            set output to output & "找到 " & textCount & " 個文字元素:\n"
            
            -- 只顯示前10個文字元素避免太多
            set limit to 10
            if textCount < limit then
                set limit to textCount
            end if
            
            repeat with i from 1 to limit
                try
                    set txtValue to value of item i of textsList
                    set output to output & i & ". " & txtValue & "\n"
                on error
                    set output to output & i & ". [無法讀取值]\n"
                end try
            end repeat
            
            if textCount > limit then
                set output to output & "... 還有 " & (textCount - limit) & " 個文字元素\n"
            end if
            
        on error errMsg
            set output to output & "錯誤: " & errMsg & "\n"
        end try
        
        return output
    end tell
end tell