#!/bin/bash

# 部署美股新聞HTML到GitHub Pages
# 使用方式：./deploy-to-github.sh [日期] [HTML檔案路徑]
# 例如：./deploy-to-github.sh 2026-02-17 /path/to/file.html

set -e

# 設定變數
REPO_DIR="/Users/yu-tsehsiao/.openclaw/workspace/stock-blog"
WORKSPACE_DIR="/Users/yu-tsehsiao/.openclaw/workspace"

# 如果沒有提供參數，使用今天的日期
if [ -z "$1" ]; then
    DATE=$(date +%Y-%m-%d)
else
    DATE="$1"
fi

# 如果沒有提供HTML檔案，尋找最新的HTML檔案
if [ -z "$2" ]; then
    HTML_FILE=$(find "$WORKSPACE_DIR" -name "美股新聞彙整_${DATE}_blog.html" -type f | head -1)
    if [ -z "$HTML_FILE" ]; then
        echo "❌ 找不到日期為 $DATE 的HTML檔案"
        exit 1
    fi
else
    HTML_FILE="$2"
fi

# 檢查檔案是否存在
if [ ! -f "$HTML_FILE" ]; then
    echo "❌ HTML檔案不存在: $HTML_FILE"
    exit 1
fi

echo "📦 開始部署..."
echo "📅 日期: $DATE"
echo "📄 HTML檔案: $HTML_FILE"
echo "📁 倉庫目錄: $REPO_DIR"

# 解析日期
YEAR=$(echo $DATE | cut -d'-' -f1)
MONTH=$(echo $DATE | cut -d'-' -f2)
DAY=$(echo $DATE | cut -d'-' -f3)

# 創建目標目錄
TARGET_DIR="$REPO_DIR/posts/$YEAR/$MONTH/$DAY"
mkdir -p "$TARGET_DIR"

echo "📂 創建目錄: $TARGET_DIR"

# 複製HTML檔案
cp "$HTML_FILE" "$TARGET_DIR/index.html"
echo "✅ 複製HTML檔案到: $TARGET_DIR/index.html"

# 進入倉庫目錄
cd "$REPO_DIR"

# 更新主頁index.html（如果存在）
if [ -f "index.html" ]; then
    echo "🔄 更新主頁index.html..."
    
    # 創建臨時檔案
    TEMP_INDEX=$(mktemp)
    
    # 讀取現有index.html，在post-list部分插入新文章
    awk -v year="$YEAR" -v month="$MONTH" -v day="$DAY" '
    /<div class="post-list">/ {
        print $0
        print "            <article class=\"post-item\">"
        print "                <div class=\"post-date\">📅 " year "年" month "月" day "日</div>"
        print "                <a href=\"posts/" year "/" month "/" day "/\" class=\"post-title\">📈 每日美股新聞彙整 - " year "年" month "月" day "日</a>"
        print "                <p class=\"post-excerpt\">美股市場重點新聞彙整與專業分析報告，包含市場概覽、重點新聞、投資建議與市場展望。</p>"
        print "                <a href=\"posts/" year "/" month "/" day "/\" class=\"read-more\">閱讀全文 →</a>"
        print "            </article>"
        next
    }
    { print }
    ' index.html > "$TEMP_INDEX"
    
    mv "$TEMP_INDEX" index.html
    echo "✅ 主頁已更新"
fi

# 提交更改
echo "📝 提交更改..."
git add .
git commit -m "新增${YEAR}年${MONTH}月${DAY}日美股新聞彙整文章" || echo "⚠️ 沒有新更改或提交失敗"

# 推送到GitHub
echo "🚀 推送到GitHub..."
git push origin main

echo "🎉 部署完成！"
echo "🌐 網站網址: https://drwolf0701.github.io/stock-blog/"
echo "📄 文章網址: https://drwolf0701.github.io/stock-blog/posts/$YEAR/$MONTH/$DAY/"