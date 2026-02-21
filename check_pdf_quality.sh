#!/bin/bash

echo "=== PDF 質量檢查報告 ==="
echo "檢查時間: $(date)"
echo "PDF檔案: 美股新聞重點_簡單版_20260215.pdf"
echo ""

# 檢查檔案大小
echo "1. 檔案大小檢查:"
filesize=$(stat -f%z "美股新聞重點_簡單版_20260215.pdf" 2>/dev/null || stat -c%s "美股新聞重點_簡單版_20260215.pdf")
if [ $filesize -gt 100000 ]; then
    echo "   ✓ 檔案大小正常: $(($filesize/1024)) KB"
else
    echo "   ✗ 檔案大小異常: 可能內容不完整"
fi

# 檢查檔案是否存在
echo ""
echo "2. 檔案存在性檢查:"
if [ -f "美股新聞重點_簡單版_20260215.pdf" ]; then
    echo "   ✓ PDF檔案存在"
else
    echo "   ✗ PDF檔案不存在"
    exit 1
fi

# 檢查檔案類型
echo ""
echo "3. 檔案類型檢查:"
filetype=$(file -b "美股新聞重點_簡單版_20260215.pdf")
if echo "$filetype" | grep -q "PDF document"; then
    echo "   ✓ 是有效的PDF文件"
    echo "   檔案類型: $filetype"
else
    echo "   ✗ 不是有效的PDF文件"
    echo "   檔案類型: $filetype"
fi

# 檢查是否可以讀取
echo ""
echo "4. 檔案可讀性檢查:"
if head -c 100 "美股新聞重點_簡單版_20260215.pdf" | grep -q "%PDF"; then
    echo "   ✓ PDF檔案格式正確"
else
    echo "   ✗ PDF檔案格式可能損壞"
fi

echo ""
echo "=== 檢查完成 ==="
echo "建議："
echo "1. 請手動打開PDF檔案檢查中文字體是否正常顯示"
echo "2. 檢查文字是否有重疊或截斷"
echo "3. 確認所有內容完整顯示"
echo "4. 確保數字和文字清晰可讀"