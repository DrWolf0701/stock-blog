#!/bin/bash

# 部署美股新聞部落格到 GitHub Pages
# GitHub 帳號: DrWolf0701

set -e

echo "🚀 開始部署到 GitHub Pages..."
echo "📋 GitHub 帳號: DrWolf0701"
echo "📅 報告日期: 2026-02-17"

# 設定變數
BLOG_DIR="/Users/yu-tsehsiao/.openclaw/workspace"
REPORT_DATE="2026-02-17"
GITHUB_USER="DrWolf0701"
GITHUB_REPO="stock-blog"
GITHUB_TOKEN=""  # 如果需要使用 token
DEPLOY_DIR="/tmp/stock-blog-gh-pages"

# 創建部署目錄
echo "📁 創建部署目錄..."
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

# 複製部落格檔案
echo "📄 複製部落格檔案..."
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}_blog.html" "$DEPLOY_DIR/index.html"
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}_blog.md" "$DEPLOY_DIR/report.md"
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}.pdf" "$DEPLOY_DIR/report.pdf"

# 創建 GitHub Pages 必要的檔案
echo "🔧 創建 GitHub Pages 配置..."

# 創建 CNAME（如果需要自訂網域）
# echo "your-domain.com" > "$DEPLOY_DIR/CNAME"

# 創建 .nojekyll 檔案（禁用 Jekyll）
touch "$DEPLOY_DIR/.nojekyll"

# 創建 favicon
cat > "$DEPLOY_DIR/favicon.ico.html" << 'EOF'
<!-- Favicon placeholder -->
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📈</text></svg>">
EOF

# 創建 404 頁面
cat > "$DEPLOY_DIR/404.html" << 'EOF'
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>頁面未找到 - 美股新聞部落格</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            margin: 0;
            padding: 20px;
        }
        
        .error-container {
            text-align: center;
            background: white;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            max-width: 600px;
        }
        
        h1 {
            font-size: 4rem;
            color: #3182ce;
            margin: 0;
        }
        
        h2 {
            color: #2d3748;
            margin: 20px 0;
        }
        
        p {
            color: #718096;
            line-height: 1.6;
            margin-bottom: 30px;
        }
        
        .home-link {
            display: inline-block;
            background: #3182ce;
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .home-link:hover {
            background: #2c5282;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>404</h1>
        <h2>頁面未找到</h2>
        <p>抱歉，您尋找的頁面不存在。可能已被移動或刪除。</p>
        <a href="/" class="home-link">返回首頁</a>
    </div>
</body>
</html>
EOF

# 創建 README
cat > "$DEPLOY_DIR/README.md" << EOF
# 📈 美股新聞部落格

每日美股市場分析報告，自動生成並部署到 GitHub Pages。

## 今日報告
- **日期**: ${REPORT_DATE}
- **報告類型**: 每日市場彙整
- **分析時間**: 台北時間下午4點
- **瀏覽網址**: https://${GITHUB_USER}.github.io/${GITHUB_REPO}/

## 檔案說明
- \`index.html\` - 部落格主頁面
- \`report.md\` - Markdown 格式報告
- \`report.pdf\` - PDF 格式完整報告
- \`404.html\` - 自訂404錯誤頁面

## 自動化部署
此部落格每日自動更新，透過 GitHub Actions 定時生成最新報告。

## 技術架構
- 靜態 HTML/CSS/JavaScript
- 響應式設計
- GitHub Pages 託管
- 自動化部署流程

## 授權
報告內容僅供參考，不構成投資建議。投資有風險，入市需謹慎。

---

*最後更新: $(date)*
EOF

# 初始化 Git 倉庫
echo "🔄 初始化 Git 倉庫..."
cd "$DEPLOY_DIR"
git init
git config user.name "DrWolf0701"
git config user.email "s8824415@hotmail.com"

# 添加檔案
git add .

# 提交
git commit -m "Deploy stock report ${REPORT_DATE} to GitHub Pages

- 美股新聞彙整報告
- 日期: ${REPORT_DATE}
- 時間: 台北時間下午4點
- 包含: HTML網頁、Markdown報告、PDF檔案"

echo "✅ 本地 Git 倉庫準備完成！"
echo ""
echo "📋 下一步操作："
echo ""
echo "1. 在 GitHub 上創建新倉庫："
echo "   網址: https://github.com/new"
echo "   倉庫名稱: ${GITHUB_REPO}"
echo "   描述: 美股新聞每日分析報告"
echo "   選擇: Public (公開)"
echo "   不要初始化 README、.gitignore、license"
echo ""
echo "2. 將本地倉庫推送到 GitHub："
echo "   cd $DEPLOY_DIR"
echo "   git remote add origin https://github.com/${GITHUB_USER}/${GITHUB_REPO}.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 啟用 GitHub Pages："
echo "   到倉庫設定 → Pages → Source"
echo "   選擇: Deploy from a branch"
echo "   分支: main"
echo "   資料夾: / (root)"
echo ""
echo "4. 等待部署完成："
echo "   幾分鐘後即可訪問："
echo "   https://${GITHUB_USER}.github.io/${GITHUB_REPO}/"
echo ""
echo "📁 部署目錄：$DEPLOY_DIR"
echo "📄 檔案列表："
ls -la "$DEPLOY_DIR/"

# 顯示 Git 狀態
echo ""
echo "🔍 Git 狀態："
git status

# 提供完整的推送到 GitHub 的指令
cat > "$DEPLOY_DIR/PUSH_TO_GITHUB.md" << EOF
# 推送到 GitHub 的完整指令

請在終端機中執行以下指令：

## 1. 進入部署目錄
\`\`\`bash
cd $DEPLOY_DIR
\`\`\`

## 2. 添加遠端倉庫
\`\`\`bash
git remote add origin https://github.com/DrWolf0701/stock-blog.git
\`\`\`

## 3. 重新命名分支
\`\`\`bash
git branch -M main
\`\`\`

## 4. 推送到 GitHub
\`\`\`bash
git push -u origin main
\`\`\`

## 5. 輸入 GitHub 憑證
當提示輸入使用者名稱時：DrWolf0701
當提示輸入密碼時：s8824415

## 6. 啟用 GitHub Pages
1. 訪問 https://github.com/DrWolf0701/stock-blog/settings/pages
2. 在 "Source" 部分選擇 "Deploy from a branch"
3. 分支選擇 "main"，資料夾選擇 "/ (root)"
4. 點擊 "Save"

## 7. 訪問你的部落格
幾分鐘後訪問：https://drwolf0701.github.io/stock-blog/
EOF

echo ""
echo "📝 詳細推送到 GitHub 的指令已儲存到：$DEPLOY_DIR/PUSH_TO_GITHUB.md"
echo ""
echo "🎉 部署準備完成！請按照上述步驟操作。"