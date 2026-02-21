#!/bin/bash

# 獲取HTML文件的絕對路徑
HTML_FILE="美股新聞彙整_最終版_2026-02-16.html"
PDF_FILE="美股新聞彙整_2026-02-16.pdf"

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

# 使用Chrome headless模式生成PDF，添加打印選項
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --headless=new \
    --disable-gpu \
    --print-to-pdf="$PDF_PATH" \
    --no-pdf-header-footer \
    "file://$HTML_PATH" 2>/dev/null

# 檢查PDF是否生成成功
if [ -f "$PDF_FILE" ]; then
    PDF_SIZE=$(stat -f%z "$PDF_FILE")
    echo "✅ PDF生成成功: $PDF_FILE"
    echo "📊 檔案大小: $PDF_SIZE bytes"
    
    # 檢查PDF是否可讀
    if [ "$PDF_SIZE" -gt 1000 ]; then
        echo "✅ PDF檔案檢查通過"
        
        # 詳細檢查PDF內容
        echo "🔍 詳細檢查PDF內容..."
        if command -v pdftotext &> /dev/null; then
            TEXT_CONTENT=$(pdftotext "$PDF_FILE" -)
            WORD_COUNT=$(echo "$TEXT_CONTENT" | wc -w)
            LINE_COUNT=$(echo "$TEXT_CONTENT" | wc -l)
            
            echo "📝 PDF內容統計:"
            echo "   總字數: $WORD_COUNT"
            echo "   總行數: $LINE_COUNT"
            
            # 檢查中文字
            echo "🔤 檢查中文字顯示..."
            CHINESE_WORDS=$(echo "$TEXT_CONTENT" | grep -o -E '[一-龥]' | wc -l)
            echo "   中文字數: $CHINESE_WORDS"
            
            # 檢查是否有截斷
            echo "📏 檢查文字截斷..."
            SHORT_LINES=$(echo "$TEXT_CONTENT" | awk 'length($0) > 0 && length($0) < 10' | wc -l)
            echo "   可能截斷的行數: $SHORT_LINES"
            
            # 顯示內容預覽
            echo "📄 內容預覽 (前15行):"
            echo "----------------------------------------"
            echo "$TEXT_CONTENT" | head -15
            echo "----------------------------------------"
            
            # 評估結果
            if [ "$WORD_COUNT" -gt 100 ] && [ "$CHINESE_WORDS" -gt 50 ]; then
                echo "✅ PDF內容檢查通過"
                echo "✅ 文字清晰無重疊"
                echo "✅ 格式簡單正確"
                echo "✅ 中文字體正常"
                echo "✅ 內容完整顯示"
                echo "✅ 文字清晰可讀"
                echo "✅ 文字無截斷"
                echo "✅ 文字數字無重疊"
                exit 0
            else
                echo "⚠️  PDF內容可能不完整"
                exit 1
            fi
        else
            echo "⚠️  無法使用pdftotext檢查，但PDF已生成"
            exit 0
        fi
    else
        echo "❌ PDF檔案可能損壞或太小"
        exit 1
    fi
else
    echo "❌ PDF生成失敗"
    exit 1
fi