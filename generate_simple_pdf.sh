#!/bin/bash

# 獲取HTML文件的絕對路徑
HTML_FILE="美股新聞彙整_簡單版_2026-02-16.html"
PDF_FILE="美股新聞彙整_簡單版_2026-02-16.pdf"

# 檢查HTML文件是否存在
if [ ! -f "$HTML_FILE" ]; then
    echo "錯誤: HTML文件 $HTML_FILE 不存在"
    exit 1
fi

# 獲取絕對路徑
HTML_PATH="$(pwd)/$HTML_FILE"
PDF_PATH="$(pwd)/$PDF_FILE"

echo "HTML文件路徑: $HTML_PATH"
echo "PDF輸出路徑: $PDF_PATH"

# 使用Chrome headless模式生成PDF，添加更多選項確保質量
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --headless=new \
    --disable-gpu \
    --no-margins \
    --print-to-pdf-no-header \
    --print-to-pdf="$PDF_PATH" \
    "file://$HTML_PATH" 2>/dev/null

# 檢查PDF是否生成成功
if [ -f "$PDF_FILE" ]; then
    PDF_SIZE=$(stat -f%z "$PDF_FILE")
    echo "✅ PDF生成成功: $PDF_FILE"
    echo "📊 檔案大小: $PDF_SIZE bytes"
    
    # 檢查PDF是否可讀
    if [ "$PDF_SIZE" -gt 1000 ]; then
        echo "✅ PDF檔案檢查通過"
        
        # 檢查PDF內容
        echo "🔍 檢查PDF文字內容..."
        if command -v pdftotext &> /dev/null; then
            TEXT_CONTENT=$(pdftotext "$PDF_FILE" -)
            WORD_COUNT=$(echo "$TEXT_CONTENT" | wc -w)
            CHAR_COUNT=$(echo "$TEXT_CONTENT" | wc -c)
            CHINESE_COUNT=$(echo "$TEXT_CONTENT" | grep -o -P '[\p{Han}]' | wc -l)
            
            echo "📝 PDF文字統計:"
            echo "   字數: $WORD_COUNT"
            echo "   字元數: $CHAR_COUNT"
            echo "   中文字數: $CHINESE_COUNT"
            
            # 檢查是否有明顯問題
            if [ "$WORD_COUNT" -lt 50 ]; then
                echo "⚠️  警告: 文字字數較少，可能內容未完全渲染"
            fi
            
            if [ "$CHINESE_COUNT" -lt 20 ]; then
                echo "⚠️  警告: 中文字數較少，可能字體問題"
            fi
            
            # 顯示前10行內容檢查
            echo "📄 前10行內容預覽:"
            echo "$TEXT_CONTENT" | head -10
        fi
        
        exit 0
    else
        echo "❌ PDF檔案可能損壞或太小"
        exit 1
    fi
else
    echo "❌ PDF生成失敗"
    exit 1
fi