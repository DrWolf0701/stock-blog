#!/bin/bash

# 完整的 GitHub Pages 部署腳本
# 包含倉庫創建、推送、啟用 Pages

set -e

echo "🚀 開始完整的 GitHub Pages 部署流程..."
echo "🔑 使用 GitHub 帳號: DrWolf0701"

# 設定變數
DEPLOY_DIR="/tmp/stock-blog-gh-pages"
GITHUB_USER="DrWolf0701"
GITHUB_REPO="stock-blog"
GITHUB_PASSWORD="s8824415"  # 注意：使用 token 更安全

# 檢查部署目錄
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "❌ 部署目錄不存在: $DEPLOY_DIR"
    echo "請先執行 deploy_to_github.sh"
    exit 1
fi

cd "$DEPLOY_DIR"

# 方法1：使用 GitHub CLI（如果已登入）
echo "🔄 嘗試使用 GitHub CLI..."
if command -v gh &> /dev/null; then
    echo "📦 創建 GitHub 倉庫..."
    
    # 檢查是否已登入
    if ! gh auth status &> /dev/null; then
        echo "🔐 GitHub CLI 未登入，嘗試使用 API..."
    else
        # 創建倉庫
        gh repo create "$GITHUB_REPO" --public --description "美股新聞每日分析報告" --disable-wiki --disable-issues --confirm
        
        # 推送到 GitHub
        echo "📤 推送到 GitHub..."
        git push -u origin main
        
        # 啟用 GitHub Pages
        echo "🌐 啟用 GitHub Pages..."
        gh repo view --web
        
        echo "✅ 請在網頁中啟用 GitHub Pages："
        echo "   設定 → Pages → Source → main → / (root) → Save"
        exit 0
    fi
fi

# 方法2：使用 GitHub API（需要 token）
echo "🔄 嘗試使用 GitHub API..."
echo "📝 請手動創建 GitHub 倉庫："
echo ""
echo "1. 訪問 https://github.com/new"
echo "2. 填寫以下資訊："
echo "   - Repository name: $GITHUB_REPO"
echo "   - Description: 美股新聞每日分析報告"
echo "   - Public (公開)"
echo "   - 不要初始化 README、.gitignore、license"
echo "3. 點擊 'Create repository'"
echo ""
read -p "按 Enter 繼續當倉庫創建完成後..." -n 1 -r

# 推送到 GitHub
echo ""
echo "📤 開始推送到 GitHub..."
echo ""

# 設置遠端倉庫
if ! git remote | grep -q origin; then
    git remote add origin "https://github.com/$GITHUB_USER/$GITHUB_REPO.git"
fi

# 重新命名分支（如果需要的話）
git branch -M main 2>/dev/null || true

# 推送到 GitHub（使用憑證）
echo "🔐 推送到 GitHub（需要輸入密碼）..."
echo "使用者名稱: $GITHUB_USER"
echo "密碼: $GITHUB_PASSWORD"
echo ""

# 嘗試推送
set +e  # 暫時關閉錯誤檢查
git push -u origin main
PUSH_RESULT=$?
set -e  # 重新開啟錯誤檢查

if [ $PUSH_RESULT -eq 0 ]; then
    echo "✅ 推送成功！"
else
    echo "⚠️  推送可能遇到問題，嘗試其他方法..."
    echo ""
    echo "替代方案：使用 SSH 金鑰或 Personal Access Token"
    echo ""
    echo "方法 A：使用 Personal Access Token"
    echo "1. 訪問 https://github.com/settings/tokens"
    echo "2. 生成新的 token（權限：repo）"
    echo "3. 使用以下指令："
    echo "   git remote set-url origin https://<TOKEN>@github.com/$GITHUB_USER/$GITHUB_REPO.git"
    echo "   git push -u origin main"
    echo ""
    echo "方法 B：使用 SSH"
    echo "1. 設定 SSH 金鑰：https://docs.github.com/authentication/connecting-to-github-with-ssh"
    echo "2. 使用 SSH URL："
    echo "   git remote set-url origin git@github.com:$GITHUB_USER/$GITHUB_REPO.git"
    echo "   git push -u origin main"
fi

# 顯示後續步驟
echo ""
echo "📋 後續步驟："
echo ""
echo "1. 啟用 GitHub Pages："
echo "   訪問 https://github.com/$GITHUB_USER/$GITHUB_REPO/settings/pages"
echo "   Source → Deploy from a branch → main → / (root) → Save"
echo ""
echo "2. 等待部署完成（約1-2分鐘）"
echo ""
echo "3. 訪問你的部落格："
echo "   https://$GITHUB_USER.github.io/$GITHUB_REPO/"
echo ""
echo "4. 設定自訂網域（可選）："
echo "   在 Pages 設定中輸入你的網域"
echo ""
echo "🎉 部署流程完成！"

# 打開本地預覽
read -p "是否要打開本地預覽？(y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open index.html 2>/dev/null || echo "無法自動打開，請手動開啟 index.html"
fi