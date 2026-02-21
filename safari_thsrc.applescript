tell application "Safari"
    activate
    delay 1
    
    -- 打開高鐵訂票網站
    make new document
    set URL of document 1 to "https://irs.thsrc.com.tw/IMINT/"
    
    delay 3
    
    -- 嘗試填寫表單（這部分可能無法自動化，因為網站有防機器人機制）
    tell document 1
        -- 這裡只能提供指引，實際操作需要手動
        display dialog "請手動操作高鐵訂票網站：
        
        步驟：
        1. 選擇「板橋→田中」
        2. 選擇日期：2026-02-19
        3. 選擇時間：10:00左右
        4. 輸入乘客：蕭毓則 (A120872165)
        5. 選擇「車站窗口取票」
        
        完成後請告訴我訂位代碼。" buttons {"確定"} default button 1
    end tell
end tell