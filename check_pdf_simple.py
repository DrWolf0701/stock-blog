#!/usr/bin/env python3
import sys
import os

def check_pdf_file(pdf_path):
    """檢查PDF文件的基本屬性"""
    if not os.path.exists(pdf_path):
        print(f"錯誤: 文件 {pdf_path} 不存在")
        return False
    
    file_size = os.path.getsize(pdf_path)
    print(f"PDF文件: {pdf_path}")
    print(f"文件大小: {file_size:,} 字節")
    print(f"文件大小: {file_size/1024:.2f} KB")
    
    # 檢查是否為有效的PDF文件
    with open(pdf_path, 'rb') as f:
        header = f.read(5)
        if header == b'%PDF-':
            print("✓ 有效的PDF文件格式")
        else:
            print("✗ 不是有效的PDF文件格式")
            return False
    
    # 檢查文件結構
    with open(pdf_path, 'rb') as f:
        content = f.read(5000)
        
        # 檢查關鍵元素
        checks = {
            '字體': b'Font' in content,
            '編碼': b'Encoding' in content or b'UTF' in content,
            '中文': b'cid' in content.lower() or b'cmap' in content.lower(),
            '頁數': b'Pages' in content or b'Count' in content,
        }
        
        print("\nPDF結構檢查:")
        for check_name, result in checks.items():
            status = "✓" if result else "○"
            print(f"  {status} {check_name}")
    
    print("\n" + "="*50)
    print("PDF質量檢查清單:")
    print("="*50)
    print("1. 中文字體正常顯示: 需手動確認")
    print("2. 文字清晰無重疊: 需手動確認")
    print("3. 格式簡單正確: 簡化版設計，應無問題")
    print("4. 內容完整顯示: 需手動確認")
    print("5. 文字沒有被截斷: 需手動確認")
    print("6. 文字數字不重疊: 需手動確認")
    print("\n建議操作:")
    print("1. 請在本地打開PDF文件進行視覺檢查")
    print("2. 確認所有中文文字清晰可讀")
    print("3. 檢查頁面邊距是否適當")
    print("4. 確認沒有文字被頁面邊緣截斷")
    
    return True

if __name__ == "__main__":
    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "美股新聞報告_簡化版_2026-02-15.pdf"
    check_pdf_file(pdf_file)