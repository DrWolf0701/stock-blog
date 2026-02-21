-- 自動化部署腳本 - 控制瀏覽器完成 GitHub Pages 部署
-- 請按照提示操作

tell application "Google Chrome"
    activate
    delay 1
    
    -- 步驟 1: 創建 GitHub 倉庫
    display dialog "🚀 開始部署美股新聞部落格到 GitHub Pages" & return & return & "第一步：創建 GitHub 倉庫" & return & "請確保已登入 GitHub 帳號 DrWolf0701" buttons {"繼續", "取消"} default button "繼續"
    
    if button returned of result is "繼續" then
        -- 打開 GitHub 創建倉庫頁面
        open location "https://github.com/new"
        delay 3
        
        display dialog "📋 請在瀏覽器中填寫：" & return & return & "1. Repository name: stock-blog" & return & "2. Description: 美股新聞每日分析報告" & return & "3. 選擇: Public" & return & "4. 不要初始化 README、.gitignore、license" & return & return & "填寫完成後點擊 'Create repository'" buttons {"已創建", "取消"} default button "已創建"
        
        if button returned of result is "已創建" then
            -- 步驟 2: 執行終端機指令
            display dialog "第二步：執行部署指令" & return & return & "將自動在終端機中執行部署指令" buttons {"執行", "取消"} default button "執行"
            
            if button returned of result is "執行" then
                -- 在終端機中執行部署指令
                tell application "Terminal"
                    activate
                    delay 1
                    do script "echo '🚀 開始部署美股新聞部落格...'"
                    delay 1
                    do script "cd /tmp/stock-blog-gh-pages" in front window
                    delay 1
                    do script "echo '🔄 設定 Git 遠端倉庫...'" in front window
                    delay 1
                    do script "git remote remove origin 2>/dev/null || true" in front window
                    delay 1
                    do script "git remote add origin https://DrWolf0701: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@github.com/DrWolf0701/stock-blog.git" in front window
                    delay 1
                    do script "echo '📤 推送到 GitHub...'" in front window
                    delay 1
                    do script "git push -u origin main" in front window
                    delay 2
                    do script "echo '✅ 推送完成！'" in front window
                end tell
                
                -- 步驟 3: 啟用 GitHub Pages
                display dialog "第三步：啟用 GitHub Pages" & return & return & "將打開 GitHub Pages 設定頁面" buttons {"打開設定", "取消"} default button "打開設定"
                
                if button returned of result is "打開設定" then
                    tell application "Google Chrome"
                        open location "https://github.com/DrWolf0701/stock-blog/settings/pages"
                        delay 3
                        
                        display dialog "🌐 請在 GitHub Pages 設定中：" & return & return & "1. 在 'Source' 部分選擇 'Deploy from a branch'" & return & "2. 分支選擇 'main'" & return & "3. 資料夾選擇 '/ (root)'" & return & "4. 點擊 'Save'" & return & return & "完成後等待約1-2分鐘" buttons {"已完成", "取消"} default button "已完成"
                        
                        if button returned of result is "已完成" then
                            -- 步驟 4: 打開部落格預覽
                            display dialog "🎉 部署完成！" & return & return & "你的部落格網址：" & return & "https://drwolf0701.github.io/stock-blog/" & return & return & "將打開本地預覽和網頁版" buttons {"打開預覽", "完成"} default button "打開預覽"
                            
                            if button returned of result is "打開預覽" then
                                -- 打開本地預覽
                                do shell script "open /tmp/stock-blog-gh-pages/index.html"
                                delay 1
                                
                                -- 打開網頁版
                                tell application "Google Chrome"
                                    open location "https://drwolf0701.github.io/stock-blog/"
                                end tell
                                
                                display dialog "✅ 所有步驟完成！" & return & return & "本地預覽和網頁版已打開" & return & "網址: https://drwolf0701.github.io/stock-blog/" buttons {"完成"} default button "完成"
                            end if
                        end if
                    end tell
                end if
            end if
        end if
    end if
end tell