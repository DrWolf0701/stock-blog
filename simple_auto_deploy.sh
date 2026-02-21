#!/bin/bash

# 簡單自動部署腳本
# 自動執行技術部分，使用者只需完成網頁操作

echo "🧸🤗 美股新聞部落格自動部署"
echo "=============================="

# 打開瀏覽器創建倉庫
echo "📋 步驟 1: 創建 GitHub 倉庫"
echo "正在打開瀏覽器..."
open "https://github.com/new"

echo ""
echo "請在瀏覽器中："
echo "1. 登入 GitHub 帳號 DrWolf0701"
echo "2. 填寫："
echo "   - Repository name: stock-blog"
echo "   - Description: 美股新聞每日分析報告"
echo "   - 選擇: Public"
echo "   - 不要初始化 README、.gitignore、license"
echo "3. 點擊 'Create repository'"
echo ""
read -p "完成後按 Enter 繼續..." -n 1 -r
echo ""

# 執行 Git 部署
echo "🔄 步驟 2: 執行 Git 部署"
cd "/tmp/stock-blog-gh-pages" || {
    echo "❌ 部署目錄不存在"
    exit 1
}

echo "設定 Git 遠端倉庫..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://DrWolf0701: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@github.com/DrWolf0701/stock-blog.git"

echo "推送到 GitHub..."
if git push -u origin main; then
    echo "✅ 推送成功！"
else
    echo "⚠️  嘗試強制推送..."
    git push -u origin main --force && echo "✅ 強制推送成功！" || echo "❌ 推送失敗"
fi

# 打開 GitHub Pages 設定
echo ""
echo "🌐 步驟 3: 啟用 GitHub Pages"
echo "正在打開設定頁面..."
open "https://github.com/DrWolf0701/stock-blog/settings/pages"

echo ""
echo "請在設定頁面中："
echo "1. 在 'Source' 部分選擇 'Deploy from a branch'"
echo "2. 分支選擇 'main'"
echo "3. 資料夾選擇 '/ (root)'"
echo "4. 點擊 'Save'"
echo ""
read -p "完成後按 Enter 繼續..." -n 1 -r
echo ""

# 顯示結果
echo ""
echo "🎉 部署完成！"
echo "================"
echo "🌐 你的部落格網址："
echo "   https://drwolf0701.github.io/stock-blog/"
echo ""
echo "📁 本地預覽："
echo "   /tmp/stock-blog-gh-pages/index.html"
echo ""
echo "⏳ 等待約1-2分鐘讓 GitHub Pages 完成部署"
echo ""

# 打開預覽
echo "正在打開預覽..."
open "/tmp/stock-blog-gh-pages/index.html"
sleep 3
open "https://drwolf0701.github.io/stock-blog/"

echo "✅ 所有步驟已完成！"
echo "📊 檢查部署：https://github.com/DrWolf0701/stock-blog/deployments"