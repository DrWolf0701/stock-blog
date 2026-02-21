-- 控制瀏覽器完成 GitHub Pages 設定
tell application "Google Chrome"
    activate
    delay 1
    
    -- 檢查當前頁面
    set currentURL to URL of active tab of front window
    display dialog "當前頁面: " & currentURL
    
    -- 如果不在設定頁面，導航到設定頁面
    if currentURL does not contain "settings/pages" then
        display dialog "正在導航到 GitHub Pages 設定頁面..." buttons {"確定"} default button "確定"
        set URL of active tab of front window to "https://github.com/DrWolf0701/stock-blog/settings/pages"
        delay 3
    end if
    
    -- 執行 JavaScript 來設定 Pages
    tell active tab of front window
        -- 等待頁面載入
        delay 2
        
        -- 嘗試設定 Source 為 "Deploy from a branch"
        execute javascript "
            // 尋找 Source 選項
            const sourceRadios = document.querySelectorAll('input[name=\"pages[source]\"]');
            if (sourceRadios.length >= 2) {
                // 選擇第二個選項 (Deploy from a branch)
                sourceRadios[1].click();
                console.log('已選擇 Deploy from a branch');
                
                // 等待選項出現
                setTimeout(() => {
                    // 設定 Branch 為 main
                    const branchSelect = document.querySelector('select[name=\"pages[branch]\"]');
                    if (branchSelect) {
                        branchSelect.value = 'main';
                        console.log('已設定 Branch: main');
                    }
                    
                    // 設定 Folder 為 /
                    const folderSelect = document.querySelector('select[name=\"pages[path]\"]');
                    if (folderSelect) {
                        folderSelect.value = '/';
                        console.log('已設定 Folder: /');
                    }
                    
                    // 點擊 Save 按鈕
                    const saveButton = document.querySelector('button[type=\"submit\"]');
                    if (saveButton && saveButton.textContent.includes('Save')) {
                        saveButton.click();
                        console.log('已點擊 Save 按鈕');
                    }
                }, 1000);
            } else {
                console.log('找不到 Source 選項');
            }
        "
    end tell
    
    delay 2
    
    -- 檢查是否成功
    execute javascript "
        const successMsg = document.querySelector('.flash-message');
        if (successMsg && successMsg.textContent.includes('published')) {
            alert('✅ GitHub Pages 設定成功！');
        } else {
            alert('請手動檢查設定');
        }
    "
    
    display dialog "操作完成！請檢查瀏覽器中的結果。" buttons {"確定"} default button "確定"
end tell