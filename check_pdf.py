#!/usr/bin/env python3
import subprocess
import sys

def check_pdf_file(pdf_path):
    """檢查PDF文件的基本屬性"""
    print(f"檢查PDF文件: {pdf_path}")
    
    # 檢查文件大小
    import os
    file_size = os.path.getsize(pdf_path)
    print(f"文件大小: {file_size:,} 位元組 ({file_size/1024:.1f} KB)")
    
    if file_size < 1000:
        print("⚠️ 警告: PDF文件太小，可能內容有問題")
        return False
    
    # 使用file命令檢查文件類型
    result = subprocess.run(['file', pdf_path], capture_output=True, text=True)
    if 'PDF document' in result.stdout:
        print("✓ 文件類型: 有效的PDF文件")
    else:
        print("❌ 文件類型: 不是有效的PDF文件")
        return False
    
    # 嘗試使用strings檢查是否包含預期的文字
    result = subprocess.run(['strings', pdf_path], capture_output=True, text=True)
    content = result.stdout
    
    # 檢查關鍵字
    keywords = ['美股', '新聞', '彙整', '2026', '道瓊', '標普', '納斯達克']
    found_keywords = []
    
    for keyword in keywords:
        if keyword in content:
            found_keywords.append(keyword)
    
    if len(found_keywords) >= 3:
        print(f"✓ 找到關鍵字: {', '.join(found_keywords)}")
    else:
        print(f"⚠️ 警告: 只找到 {len(found_keywords)} 個關鍵字")
        print(f"找到的關鍵字: {found_keywords}")
    
    # 檢查中文字符
    chinese_chars = ['美', '股', '新', '聞', '彙', '整', '中', '文']
    chinese_found = any(char in content for char in chinese_chars)
    
    if chinese_found:
        print("✓ 檢測到中文字符")
    else:
        print("⚠️ 警告: 未檢測到中文字符")
    
    print("\n📋 PDF檢查完成")
    return True

if __name__ == "__main__":
    pdf_file = "us_stock_news_20260215.pdf"
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]
    
    success = check_pdf_file(pdf_file)
    sys.exit(0 if success else 1)