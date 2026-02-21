#!/bin/bash

# 獲取HTML文件的絕對路徑
HTML_FILE="daily_us_stock_report_20260215.html"
PDF_FILE="daily_us_stock_report_20260215.pdf"

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

# 使用Chrome headless模式生成PDF
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --headless=new \
    --disable-gpu \
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
        
        # 簡單檢查PDF內容
        echo "🔍 檢查PDF基本資訊..."
        if command -v pdftotext &> /dev/null; then
            TEXT_COUNT=$(pdftotext "$PDF_FILE" - | wc -w)
            echo "📝 PDF文字字數: $TEXT_COUNT"
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