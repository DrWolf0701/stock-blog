#!/bin/bash

# 美股新聞部落格部署腳本
# 將每日報告部署到靜態網站託管服務

set -e

echo "🚀 開始部署美股新聞部落格..."

# 設定變數
BLOG_DIR="/Users/yu-tsehsiao/.openclaw/workspace"
REPORT_DATE="2026-02-17"
GITHUB_REPO="your-username/stock-blog"  # 請修改為你的 GitHub 倉庫
DEPLOY_DIR="/tmp/stock-blog-deploy"

# 創建部署目錄
echo "📁 創建部署目錄..."
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

# 複製部落格檔案
echo "📄 複製部落格檔案..."
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}_blog.html" "$DEPLOY_DIR/index.html"
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}_blog.md" "$DEPLOY_DIR/report.md"
cp "$BLOG_DIR/美股新聞彙整_${REPORT_DATE}.pdf" "$DEPLOY_DIR/report.pdf"

# 創建必要的目錄結構
mkdir -p "$DEPLOY_DIR/css"
mkdir -p "$DEPLOY_DIR/js"
mkdir -p "$DEPLOY_DIR/images"

# 創建 CSS 檔案（如果需要）
cat > "$DEPLOY_DIR/css/style.css" << 'EOF'
/* 額外的 CSS 樣式 */
.print-button {
    display: none;
}

@media print {
    .no-print {
        display: none !important;
    }
}
EOF

# 創建 JavaScript 檔案（如果需要）
cat > "$DEPLOY_DIR/js/main.js" << 'EOF'
// 部落格互動功能
document.addEventListener('DOMContentLoaded', function() {
    // 閱讀進度指示器
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #3182ce, #38a169);
        width: 0%;
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
    });
    
    // 回到頂部按鈕
    const backToTop = document.createElement('button');
    backToTop.textContent = '↑';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 80px;
        right: 20px;
        background: #3182ce;
        color: white;
        border: none;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        cursor: pointer;
        font-size: 24px;
        display: none;
        z-index: 1000;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    `;
    backToTop.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
    document.body.appendChild(backToTop);
    
    window.addEventListener('scroll', function() {
        backToTop.style.display = window.scrollY > 500 ? 'block' : 'none';
    });
});
EOF

# 創建 favicon（簡單版本）
echo '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📈</text></svg>">' > "$DEPLOY_DIR/favicon.html"

# 創建 README
cat > "$DEPLOY_DIR/README.md" << EOF
# 美股新聞部落格

每日美股市場分析報告，自動生成並部署。

## 今日報告
- **日期**: ${REPORT_DATE}
- **報告類型**: 每日市場彙整
- **分析時間**: 台北時間下午4點

## 檔案說明
- \`index.html\` - 部落格主頁面
- \`report.md\` - Markdown 格式報告
- \`report.pdf\` - PDF 格式完整報告

## 瀏覽報告
1. 直接打開 \`index.html\` 在瀏覽器中查看
2. 或部署到 GitHub Pages、Netlify、Vercel 等服務

## 自動化部署
此部落格可設定自動化部署，每日定時更新。

## 授權
報告內容僅供參考，不構成投資建議。
EOF

# 創建部署配置檔案（Netlify）
cat > "$DEPLOY_DIR/netlify.toml" << 'EOF'
[build]
  publish = "."
  command = "echo 'No build needed'"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "18"
EOF

# 創建部署配置檔案（Vercel）
cat > "$DEPLOY_DIR/vercel.json" << 'EOF'
{
  "version": 2,
  "builds": [
    {
      "src": "*.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
EOF

echo "✅ 部署檔案準備完成！"

# 顯示部署選項
echo ""
echo "📋 部署選項："
echo "1. GitHub Pages:"
echo "   cd $DEPLOY_DIR"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Deploy stock report ${REPORT_DATE}'"
echo "   git branch -M main"
echo "   git remote add origin https://github.com/${GITHUB_REPO}.git"
echo "   git push -u origin main"
echo ""
echo "2. Netlify:"
echo "   netlify deploy --dir=$DEPLOY_DIR --prod"
echo ""
echo "3. Vercel:"
echo "   vercel --cwd $DEPLOY_DIR --prod"
echo ""
echo "4. 本地預覽："
echo "   open $DEPLOY_DIR/index.html"
echo ""
echo "📁 部署目錄：$DEPLOY_DIR"
echo "📄 主要檔案："
ls -la "$DEPLOY_DIR/"

# 自動打開預覽
read -p "是否要打開本地預覽？(y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "$DEPLOY_DIR/index.html"
fi

echo "🎉 部落格部署準備完成！"