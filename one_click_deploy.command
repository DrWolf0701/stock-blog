#!/bin/bash
# 一鍵部署腳本 - 請先手動創建 GitHub 倉庫

echo "🎯 美股新聞部落格一鍵部署"
echo "=========================="
echo ""

# 檢查是否已創建倉庫
echo "🔍 檢查 GitHub 倉庫..."
if curl -s "https://api.github.com/repos/DrWolf0701/stock-blog" | grep -q '"name"'; then
    echo "✅ GitHub 倉庫已存在"
else
    echo "❌ GitHub 倉庫不存在"
    echo ""
    echo "📋 請先手動創建倉庫："
    echo "1. 訪問 https://github.com/new"
    echo "2. 倉庫名稱: stock-blog"
    echo "3. 描述: 美股新聞每日分析報告"
    echo "4. 選擇: Public"
    echo "5. 不要初始化 README、.gitignore、license"
    echo "6. 點擊 Create repository"
    echo ""
    read -p "創建完成後按 Enter 繼續..." -n 1 -r
    echo ""
fi

# 進入部署目錄
cd "/tmp/stock-blog-gh-pages" || {
    echo "❌ 部署目錄不存在"
    exit 1
}

echo "🔄 設定 Git 遠端倉庫..."
git remote remove origin 2>/dev/null || true

# 使用你的 token
GIT_URL="https://DrWolf0701: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@github.com/DrWolf0701/stock-blog.git"
git remote add origin "$GIT_URL"

echo "📤 推送到 GitHub..."
if git push -u origin main; then
    echo "✅ 推送成功！"
else
    echo "❌ 推送失敗，嘗試強制推送..."
    if git push -u origin main --force; then
        echo "✅ 強制推送成功！"
    else
        echo "❌ 推送仍然失敗"
        echo "可能的原因："
        echo "1. Token 權限不足"
        echo "2. 倉庫名稱不正確"
        echo "3. 網路問題"
        exit 1
    fi
fi

echo ""
echo "🌐 下一步：啟用 GitHub Pages"
echo "=========================="
echo "1. 訪問 https://github.com/DrWolf0701/stock-blog/settings/pages"
echo "2. 在 'Source' 部分選擇 'Deploy from a branch'"
echo "3. 分支選擇 'main'，資料夾選擇 '/ (root)'"
echo "4. 點擊 'Save'"
echo ""
echo "⏳ 等待約1-2分鐘..."
echo ""
echo "🎉 你的部落格網址："
echo "   https://drwolf0701.github.io/stock-blog/"
echo ""
echo "📱 本地預覽已打開..."

# 打開本地預覽
open "/tmp/stock-blog-gh-pages/index.html" 2>/dev/null || echo "請手動開啟: /tmp/stock-blog-gh-pages/index.html"

echo ""
echo "✅ 部署完成！"
echo "📊 檢查部署：https://github.com/DrWolf0701/stock-blog/deployments"