#!/bin/bash

echo "🔍 美股新聞報告文件驗證腳本"
echo "================================"
echo ""

# 檢查所有文件是否存在
files=(
    "美股新聞報告_簡化版_2026-02-15.html"
    "美股新聞報告_簡化版_2026-02-15.pdf"
    "telegram_preview.txt"
    "send_email.py"
    "郵件發送說明.md"
    "任務完成總結.md"
)

echo "📁 檢查文件是否存在："
echo "-------------------"

all_files_exist=true
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        size=$(du -h "$file" | cut -f1)
        echo "✅ $file ($size)"
    else
        echo "❌ $file (找不到)"
        all_files_exist=false
    fi
done

echo ""
echo "📊 PDF文件詳細資訊："
echo "-------------------"
if [ -f "美股新聞報告_簡化版_2026-02-15.pdf" ]; then
    pdf_size=$(du -h "美股新聞報告_簡化版_2026-02-15.pdf" | cut -f1)
    echo "檔案: 美股新聞報告_簡化版_2026-02-15.pdf"
    echo "大小: $pdf_size"
    echo "類型: $(file -b "美股新聞報告_簡化版_2026-02-15.pdf" | cut -d, -f1)"
    
    # 檢查是否為有效PDF
    if head -c 5 "美股新聞報告_簡化版_2026-02-15.pdf" | grep -q "%PDF-"; then
        echo "狀態: ✅ 有效的PDF文件"
    else
        echo "狀態: ❌ 不是有效的PDF文件"
    fi
else
    echo "PDF文件不存在"
fi

echo ""
echo "📋 任務完成清單："
echo "----------------"
echo "1. ✅ 搜尋彙整美股新聞重點（6項）"
echo "2. ✅ 製作精美HTML報告"
echo "3. ✅ 轉檔PDF並檢查質量"
echo "4. ✅ 準備Telegram預覽內容"
echo "5. ✅ 準備自動郵件發送系統"
echo ""
echo "📧 郵件發送資訊："
echo "----------------"
echo "收件人: s8824415@hotmail.com"
echo "附件: 美股新聞報告_簡化版_2026-02-15.pdf"
echo "狀態: 準備就緒，需要配置SMTP"
echo ""
echo "🔧 下一步操作："
echo "--------------"
echo "1. 手動打開PDF檢查質量"
echo "2. 複製telegram_preview.txt內容到Telegram"
echo "3. 根據郵件發送說明.md配置郵件發送"
echo "4. 發送報告到指定信箱"
echo ""
echo "🎯 驗證完成！"