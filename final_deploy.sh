#!/bin/bash

# 最終部署腳本 - 使用新 token
set -e

echo "🚀 最終部署開始..."
echo "🔑 使用 GitHub token: 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"

# 設定
TOKEN="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"
USER="DrWolf0701"
REPO="stock-blog"
DEPLOY_DIR="/tmp/stock-blog-gh-pages"

# 檢查部署目錄
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "❌ 部署目錄不存在"
    exit 1
fi

cd "$DEPLOY_DIR"

# 步驟 1: 測試 token
echo "🔍 測試 GitHub token..."
USER_INFO=$(curl -s -H "Authorization: token $TOKEN" https://api.github.com/user)
if echo "$USER_INFO" | grep -q '"login"'; then
    USERNAME=$(echo "$USER_INFO" | grep -o '"login":"[^"]*"' | cut -d'"' -f4)
    echo "✅ Token 有效！使用者: $USERNAME"
else
    echo "❌ Token 無效或已過期"
    echo "請生成新的 token: https://github.com/settings/tokens"
    exit 1
fi

# 步驟 2: 檢查倉庫是否存在
echo "🔍 檢查倉庫是否存在..."
REPO_INFO=$(curl -s -H "Authorization: token $TOKEN" "https://api.github.com/repos/$USER/$REPO")
if echo "$REPO_INFO" | grep -q '"name"'; then
    echo "✅ 倉庫已存在: $REPO"
else
    echo "📦 創建新倉庫..."
    CREATE_RESULT=$(curl -X POST \
      -H "Authorization: token $TOKEN" \
      -H "Accept: application/vnd.github.v3+json" \
      https://api.github.com/user/repos \
      -d "{\"name\":\"$REPO\",\"description\":\"美股新聞每日分析報告\",\"private\":false,\"auto_init\":false,\"has_issues\":false,\"has_wiki\":false}" 2>/dev/null)
    
    if echo "$CREATE_RESULT" | grep -q '"name"'; then
        echo "✅ 倉庫創建成功！"
    else
        echo "❌ 倉庫創建失敗"
        echo "請手動創建: https://github.com/new"
        echo "倉庫名稱: $REPO"
        read -p "按 Enter 當倉庫創建完成後..." -n 1 -r
    fi
fi

# 步驟 3: 設定 Git 並推送
echo "🔄 設定 Git 遠端倉庫..."
git remote remove origin 2>/dev/null || true

# 使用 token 設定遠端 URL
GIT_URL="https://$USER:$TOKEN@github.com/$USER/$REPO.git"
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
        echo "請檢查："
        echo "1. Token 權限是否足夠（需要 repo 權限）"
        echo "2. 網路連線是否正常"
        echo "3. 倉庫名稱是否正確"
        exit 1
    fi
fi

# 步驟 4: 啟用 GitHub Pages
echo "🌐 準備啟用 GitHub Pages..."
echo ""
echo "📋 請手動啟用 GitHub Pages："
echo "1. 訪問 https://github.com/$USER/$REPO/settings/pages"
echo "2. 在 'Source' 部分選擇 'Deploy from a branch'"
echo "3. 分支選擇 'main'，資料夾選擇 '/ (root)'"
echo "4. 點擊 'Save'"
echo ""
echo "⏳ 等待約1-2分鐘部署完成..."
echo ""
echo "🎉 你的部落格網址："
echo "   https://$USER.github.io/$REPO/"
echo ""
echo "📱 本地預覽："
echo "   檔案: $DEPLOY_DIR/index.html"

# 打開本地預覽
read -p "是否要打開本地預覽？(y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open index.html 2>/dev/null || echo "請手動開啟: $DEPLOY_DIR/index.html"
fi

echo ""
echo "✅ 部署流程完成！"
echo "📊 檢查部署狀態："
echo "   https://github.com/$USER/$REPO/deployments"