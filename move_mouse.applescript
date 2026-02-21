-- 嘗試使用 AppleScript 移動滑鼠到畫面中央
tell application "System Events"
    -- 獲取螢幕尺寸
    set screenBounds to bounds of window of desktop
    set screenWidth to item 3 of screenBounds
    set screenHeight to item 4 of screenBounds
    
    -- 計算中央位置
    set centerX to screenWidth div 2
    set centerY to screenHeight div 2
    
    -- 嘗試移動滑鼠
    try
        set mouse position to {centerX, centerY}
        return "滑鼠已移動到 (" & centerX & ", " & centerY & ")"
    on error errMsg
        return "移動滑鼠失敗: " & errMsg
    end try
end tell