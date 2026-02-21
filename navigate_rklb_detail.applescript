tell application "System Events"
    tell process "富途牛牛"
        set frontmost to true
        delay 1
        
        -- 先按Esc退出搜尋模式
        key code 53 -- Esc鍵
        delay 1
        
        -- 重新搜尋RKLB
        keystroke "f" using {command down}
        delay 0.5
        keystroke "RKLB"
        delay 0.5
        keystroke return
        delay 2
        
        -- 這次用滑鼠點擊的方式（假設第一個結果在特定位置）
        -- 先按Tab切換到結果列表
        keystroke tab
        delay 0.5
        
        -- 再按Enter選擇第一個結果
        keystroke return
        delay 3
        
        -- 現在應該在詳細頁面，嘗試獲取價格
        -- 按Tab多次切換到價格區域
        repeat 5 times
            keystroke tab
            delay 0.3
        end repeat
        
        -- 嘗試用快捷鍵查看頁面資訊
        keystroke "a" using {command down}
        delay 0.5
        keystroke "c" using {command down}
        delay 0.5
        
        -- 檢查剪貼簿
        set pageInfo to do shell script "pbpaste"
        
        if pageInfo is not "" then
            -- 只取前500字元避免太長
            if length of pageInfo > 500 then
                set pageInfo to text 1 thru 500 of pageInfo & "..."
            end if
            return "頁面資訊: " & pageInfo
        else
            -- 嘗試獲取視窗結構
            try
                set btnCount to count of buttons of window 1
                set txtCount to count of static texts of window 1
                return "無法複製內容，但視窗中有 " & btnCount & " 個按鈕和 " & txtCount & " 個文字元素。請手動查看RKLB詳細頁面。"
            on error
                return "已導航到RKLB頁面，請手動查看價格資訊。"
            end try
        end if
    end tell
end tell