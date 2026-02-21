-- 使用鍵盤控制完成設定
tell application "System Events"
    tell application "Google Chrome" to activate
    delay 1
    
    -- 確保在正確的頁面
    tell application "Google Chrome"
        set currentURL to URL of active tab of front window
        if currentURL does not contain "settings/pages" then
            set URL of active tab of front window to "https://github.com/DrWolf0701/stock-blog/settings/pages"
            delay 3
        end if
    end tell
    
    -- 給予使用者指引
    display dialog "🎯 請按照以下鍵盤操作：" & return & return & "1. 按 Tab 鍵移動到 'Deploy from a branch'" & return & "2. 按 Space 鍵選擇" & return & "3. 按 Tab 鍵移動到 Branch 下拉選單" & return & "4. 按 ↓ 鍵選擇 'main'" & return & "5. 按 Tab 鍵移動到 Folder 下拉選單" & return & "6. 按 ↓ 鍵選擇 '/ (root)'" & return & "7. 按 Tab 鍵移動到 Save 按鈕" & return & "8. 按 Enter 鍵儲存" & return & return & "準備好後按「開始」" buttons {"開始", "取消"} default button "開始"
    
    if button returned of result is "開始" then
        -- 開始鍵盤指引
        display dialog "第一步：按 Tab 鍵移動到 'Deploy from a branch' 選項" buttons {"下一步"} default button "下一步"
        
        display dialog "第二步：按 Space 鍵選擇 'Deploy from a branch'" buttons {"下一步"} default button "下一步"
        
        display dialog "第三步：按 Tab 鍵移動到 Branch 下拉選單" buttons {"下一步"} default button "下一步"
        
        display dialog "第四步：按 ↓ 鍵選擇 'main'" buttons {"下一步"} default button "下一步"
        
        display dialog "第五步：按 Tab 鍵移動到 Folder 下拉選單" buttons {"下一步"} default button "下一步"
        
        display dialog "第六步：按 ↓ 鍵選擇 '/ (root)'" buttons {"下一步"} default button "下一步"
        
        display dialog "第七步：按 Tab 鍵移動到 Save 按鈕" buttons {"下一步"} default button "下一步"
        
        display dialog "第八步：按 Enter 鍵儲存設定" buttons {"完成"} default button "完成"
        
        -- 檢查結果
        delay 2
        tell application "Google Chrome"
            execute front window's active tab javascript "
                setTimeout(() => {
                    window.location.reload();
                }, 1000);
            "
        end tell
        
        delay 3
        
        display dialog "✅ 設定完成！" & return & return & "請檢查瀏覽器中是否顯示：" & return & "• Your site is published at..." & return & "• 或部署進行中的訊息" & return & return & "等待1-2分鐘後訪問：" & return & "https://drwolf0701.github.io/stock-blog/" buttons {"打開部落格", "完成"} default button "打開部落格"
        
        if button returned of result is "打開部落格" then
            tell application "Google Chrome"
                open location "https://drwolf0701.github.io/stock-blog/"
            end tell
        end if
    end if
end tell