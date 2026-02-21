#!/bin/bash

# 互動式部署腳本
# 將逐步指導你完成部署

echo "🧸🤗 互動式 GitHub Pages 部署"
echo "=============================="

# 檢查 GitHub CLI 登入狀態
echo "🔍 檢查 GitHub 登入狀態..."
if gh auth status &>/dev/null; then
    echo "✅ 已登入 GitHub"
    USERNAME=$(gh api user | jq -r .login 2>/dev/null || echo "未知")
    echo "   使用者: $USERNAME"
else
    echo "❌ 未登入 GitHub"
    echo ""
    echo "📋 請先登入 GitHub："
    echo "1. 打開終端機"
    echo "2. 執行: gh auth login"
    echo "3. 選擇: GitHub.com"
    echo "4. 選擇: HTTPS"
    echo "5. 選擇: Y (是) 使用 GitHub CLI 登入"
    echo "6. 在瀏覽器中完成授權"
    echo ""
    read -p "完成登入後按 Enter 繼續..." -n 1 -r
    echo ""
fi

# 步驟 1: 創建倉庫
echo ""
echo "📦 步驟 1: 創建 GitHub 倉庫"
echo "------------------------------"

# 檢查倉庫是否已存在
if gh repo view "DrWolf0701/stock-blog" &>/dev/null; then
    echo "✅ 倉庫已存在: stock-blog"
else
    echo "創建新倉庫..."
    echo "執行: gh repo create stock-blog --public --description \"美股新聞每日分析報告\""
    
    if gh repo create "stock-blog" --public --description "美股新聞每日分析報告" --disable-wiki --disable-issues; then
        echo "✅ 倉庫創建成功！"
    else
        echo "❌ 倉庫創建失敗"
        echo "請手動創建: https://github.com/new"
        echo "倉庫名稱: stock-blog"
        read -p "創建完成後按 Enter 繼續..." -n 1 -r
        echo ""
    fi
fi

# 步驟 2: 推送到 GitHub
echo ""
echo "📤 步驟 2: 推送到 GitHub"
echo "------------------------------"
cd "/tmp/stock-blog-gh-pages" || {
    echo "❌ 部署目錄不存在"
    exit 1
}

echo "當前目錄: $(pwd)"
echo "檔案清單:"
ls -la

echo ""
echo "設定 Git 遠端倉庫..."
git remote remove origin 2>/dev/null || true

# 使用 GitHub CLI 獲取遠端 URL
REMOTE_URL=$(gh repo view "DrWolf0701/stock-blog" --json url -q '.url' 2>/dev/null || echo "https://github.com/DrWolf0701/stock-blog.git")

echo "遠端 URL: $REMOTE_URL"
git remote add origin "$REMOTE_URL"

echo ""
echo "推送到 GitHub..."
if git push -u origin main; then
    echo "✅ 推送成功！"
else
    echo "❌ 推送失敗，嘗試強制推送..."
    if git push -u origin main --force; then
        echo "✅ 強制推送成功！"
    else
        echo "❌ 推送仍然失敗"
        echo "請檢查："
        echo "1. 是否有寫入權限"
        echo "2. 網路連線"
        exit 1
    fi
fi

# 步驟 3: 啟用 GitHub Pages
echo ""
echo "🌐 步驟 3: 啟用 GitHub Pages"
echo "------------------------------"

# 嘗試使用 GitHub CLI 啟用 Pages
echo "嘗試啟用 GitHub Pages..."
if gh api -X POST "/repos/DrWolf0701/stock-blog/pages" -f "source={\"branch\":\"main\",\"path\":\"/\"}" &>/dev/null; then
    echo "✅ GitHub Pages 已啟用"
else
    echo "⚠️  無法自動啟用，請手動設定："
    echo ""
    echo "1. 訪問: https://github.com/DrWolf0701/stock-blog/settings/pages"
    echo "2. 在 'Source' 部分選擇 'Deploy from a branch'"
    echo "3. 分支選擇 'main'，資料夾選擇 '/ (root)'"
    echo "4. 點擊 'Save'"
    echo ""
    read -p "完成後按 Enter 繼續..." -n 1 -r
    echo ""
fi

# 步驟 4: 顯示結果
echo ""
echo "🎉 部署完成！"
echo "=============="
echo ""
echo "🌐 你的部落格網址："
echo "   https://drwolf0701.github.io/stock-blog/"
echo ""
echo "📊 檢查部署狀態："
echo "   https://github.com/DrWolf0701/stock-blog/deployments"
echo ""
echo "⚙️  Pages 設定："
echo "   https://github.com/DrWolf0701/stock-blog/settings/pages"
echo ""
echo "📁 本地預覽："
echo "   /tmp/stock-blog-gh-pages/index.html"
echo ""

# 打開預覽
read -p "是否要打開預覽？(y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "正在打開預覽..."
    open "/tmp/stock-blog-gh-pages/index.html"
    sleep 2
    open "https://drwolf0701.github.io/stock-blog/"
fi

echo ""
echo "✅ 所有步驟已完成！"
echo "⏳ 請等待1-2分鐘讓 GitHub Pages 完成部署"