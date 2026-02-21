#!/bin/bash

# 全自動部署腳本
# 將自動完成所有部署步驟

set -e

echo "🧸🤗 開始全自動部署美股新聞部落格..."
echo "======================================"

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 函數：顯示步驟
show_step() {
    echo -e "\n${BLUE}▶ $1${NC}"
}

# 函數：顯示成功
show_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# 函數：顯示警告
show_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# 函數：顯示錯誤
show_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 函數：等待使用者確認
wait_for_user() {
    echo -e "\n${YELLOW}⏳ $1${NC}"
    read -p "按 Enter 繼續..." -n 1 -r
    echo
}

# 設定
TOKEN="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"
USER="DrWolf0701"
REPO="stock-blog"
DEPLOY_DIR="/tmp/stock-blog-gh-pages"

# 檢查部署目錄
if [ ! -d "$DEPLOY_DIR" ]; then
    show_error "部署目錄不存在: $DEPLOY_DIR"
    exit 1
fi

cd "$DEPLOY_DIR"

# 步驟 1: 打開瀏覽器創建倉庫
show_step "步驟 1: 創建 GitHub 倉庫"
echo "將打開瀏覽器到 GitHub 創建頁面"
echo "請手動操作："
echo "1. 登入 GitHub 帳號 DrWolf0701"
echo "2. 填寫倉庫資訊："
echo "   - Repository name: stock-blog"
echo "   - Description: 美股新聞每日分析報告"
echo "   - 選擇: Public"
echo "   - 不要初始化 README、.gitignore、license"
echo "3. 點擊 'Create repository'"

# 打開瀏覽器
open "https://github.com/new"

wait_for_user "請在瀏覽器中完成倉庫創建，完成後按 Enter"

# 步驟 2: 測試倉庫是否已創建
show_step "步驟 2: 檢查倉庫狀態"
if curl -s "https://api.github.com/repos/$USER/$REPO" | grep -q '"name"'; then
    show_success "倉庫已存在: $REPO"
else
    show_warning "無法偵測到倉庫，請確認已創建"
    wait_for_user "請確認已創建倉庫，然後按 Enter"
fi

# 步驟 3: 執行 Git 部署
show_step "步驟 3: 執行 Git 部署"
echo "將執行以下指令："
echo "1. 設定 Git 遠端倉庫"
echo "2. 推送到 GitHub"

# 設定 Git 遠端
echo -e "\n${YELLOW}設定 Git 遠端倉庫...${NC}"
git remote remove origin 2>/dev/null || true
GIT_URL="https://$USER:$TOKEN@github.com/$USER/$REPO.git"
git remote add origin "$GIT_URL"

if [ $? -eq 0 ]; then
    show_success "Git 遠端設定成功"
else
    show_error "Git 遠端設定失敗"
    exit 1
fi

# 推送到 GitHub
echo -e "\n${YELLOW}推送到 GitHub...${NC}"
if git push -u origin main; then
    show_success "推送成功！"
else
    show_warning "普通推送失敗，嘗試強制推送..."
    if git push -u origin main --force; then
        show_success "強制推送成功！"
    else
        show_error "推送失敗"
        echo "可能原因："
        echo "1. Token 權限不足"
        echo "2. 倉庫名稱不正確"
        echo "3. 網路問題"
        exit 1
    fi
fi

# 步驟 4: 打開 GitHub Pages 設定
show_step "步驟 4: 啟用 GitHub Pages"
echo "將打開瀏覽器到 GitHub Pages 設定頁面"
echo "請手動操作："
echo "1. 在 'Source' 部分選擇 'Deploy from a branch'"
echo "2. 分支選擇 'main'"
echo "3. 資料夾選擇 '/ (root)'"
echo "4. 點擊 'Save'"

# 打開 GitHub Pages 設定
open "https://github.com/DrWolf0701/stock-blog/settings/pages"

# 步驟 5: 顯示結果
show_step "步驟 5: 部署完成"
show_success "🎉 部署流程完成！"

echo -e "\n${GREEN}📊 部署摘要：${NC}"
echo "────────────────────"
echo "📍 部落格網址: https://drwolf0701.github.io/stock-blog/"
echo "📁 本地檔案: $DEPLOY_DIR"
echo "🔗 GitHub 倉庫: https://github.com/DrWolf0701/stock-blog"
echo "⚙️  Pages 設定: https://github.com/DrWolf0701/stock-blog/settings/pages"
echo "📈 部署狀態: https://github.com/DrWolf0701/stock-blog/deployments"

# 步驟 6: 打開預覽
show_step "步驟 6: 打開預覽"
echo "將打開本地預覽和網頁版"

# 打開本地預覽
open "$DEPLOY_DIR/index.html"

# 等待一下然後打開網頁版
sleep 2
open "https://drwolf0701.github.io/stock-blog/"

show_success "✅ 所有步驟已完成！"
echo -e "\n${YELLOW}⏳ 請等待約1-2分鐘讓 GitHub Pages 完成部署${NC}"
echo -e "${GREEN}🌐 然後訪問: https://drwolf0701.github.io/stock-blog/${NC}"

# 顯示檔案清單
echo -e "\n${BLUE}📁 部署檔案清單：${NC}"
ls -la "$DEPLOY_DIR/"

echo -e "\n${GREEN}✨ 部署完成！你的美股新聞部落格已準備就緒。${NC}"