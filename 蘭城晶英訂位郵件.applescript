tell application "Mail"
    -- 創建新郵件
    set newMessage to make new outgoing message with properties {subject:"紅樓中餐廳訂位 - 2026年1月19日", content:"您好，

我想預訂紅樓中餐廳：
- 日期：2026年1月19日（星期日）
- 人數：6位大人
- 時段：中午11:00-13:00（或其他可用時段）
- 菜單：櫻桃霸王鴨套餐（6人份）
- 聯絡人：蕭毓則
- 電話：0963676670

請協助安排訂位，謝謝！

蕭毓則"}
    
    -- 設定收件人
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"rlrs@silksplace-yilan.com.tw"}
    end tell
    
    -- 發送郵件
    send newMessage
    log "訂位郵件已成功發送！"
end tell