#!/usr/bin/env python3
"""
簡單記憶清理工具
由 OpenClaw 建立 🐻
"""

import os
from datetime import datetime
from pathlib import Path

def create_quick_reference():
    """建立快速參考指南"""
    print("📋 建立快速參考指南...")
    
    quick_ref = f"""# 🐻 OpenClaw 快速參考指南

## 核心身份
- 名稱：OpenClaw (熊抱哥風格)
- 使用者：Chris
- 風格：可愛、直接、朋友模式

## 已建立能力
### ✅ 影片處理
- 工具：FFmpeg, OpenCV, PIL, moviepy
- 功能：影片生成、剪輯、文字顯示
- 範例：熊抱哥賀歲影片

### ✅ 文件生成
- PDF：reportlab
- Excel：pandas, openpyxl  
- PPT：python-pptx

### ✅ 開發環境
- Python 虛擬環境
- VS Code 完整設定
- 常用套件安裝

### ✅ 模型管理
- 當前：deepseek/deepseek-chat
- 備用：GPT (openai/gpt-5.1-codex)
- 模式：建議切換，使用者決定

## 重要設定
- 溝通：直接指出錯誤
- 權限：詢問外部操作
- 成本：關注 API 費用
- 記憶：定期優化整理

## 聯絡資訊
- Telegram：DrWolf (8591494215)
- WhatsApp：+886963676670

---
*最後更新：{datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    
    ref_path = Path("/Users/yu-tsehsiao/.openclaw/workspace/QUICK_REFERENCE.md")
    with open(ref_path, 'w', encoding='utf-8') as f:
        f.write(quick_ref)
    
    print(f"  ✅ 快速參考指南已建立: {ref_path}")
    return ref_path

def optimize_memory_files():
    """優化記憶檔案"""
    print("🗑️  優化記憶檔案...")
    
    workspace = Path("/Users/yu-tsehsiao/.openclaw/workspace")
    memory_dir = workspace / "memory"
    
    # 檢查檔案
    total_size = 0
    files_info = []
    
    # MEMORY.md
    memory_file = workspace / "MEMORY.md"
    if memory_file.exists():
        size = os.path.getsize(memory_file)
        total_size += size
        files_info.append(("MEMORY.md", size))
    
    # 每日記憶
    if memory_dir.exists():
        for file in memory_dir.glob("*.md"):
            size = os.path.getsize(file)
            total_size += size
            files_info.append((file.name, size))
    
    print(f"  目前記憶檔案總大小: {total_size:,} bytes")
    print(f"  檔案數量: {len(files_info)}")
    
    # 建議
    print("\n💡 節省 API 費用建議:")
    print("  1. 使用 QUICK_REFERENCE.md 快速查閱")
    print("  2. 定期清理舊的每日記憶")
    print("  3. 保持 MEMORY.md 精簡")
    print("  4. 使用 memory_search 時指定明確查詢")
    print("  5. 避免載入不必要的大檔案")

def main():
    """主程式"""
    print("=" * 60)
    print("🐻 記憶優化建議")
    print("=" * 60)
    
    # 建立快速參考
    create_quick_reference()
    
    # 分析記憶檔案
    optimize_memory_files()
    
    print("\n" + "=" * 60)
    print("🎯 具體執行建議:")
    print("=" * 60)
    
    print("""
1. **精簡 MEMORY.md**
   - 只保留重要決策和核心偏好
   - 移除過時和已完成任務
   - 使用簡潔的摘要格式

2. **管理每日記憶**
   - 只保留最近7-14天的記憶
   - 壓縮舊記憶為摘要
   - 使用標準化格式

3. **優化搜尋習慣**
   - 使用 memory_search 前先思考關鍵字
   - 只讀取需要的部分 (memory_get with lines)
   - 避免重複搜尋相同內容

4. **建立索引系統**
   - 使用 QUICK_REFERENCE.md 快速查閱
   - 建立技能索引檔案
   - 分類儲存不同類型記憶

5. **定期維護**
   - 每週清理一次記憶
   - 更新快速參考指南
   - 檢查並移除冗餘資訊
""")
    
    print("=" * 60)
    print("💸 API 費用節省估計:")
    print("=" * 60)
    
    print("""
假設每次會話：
- 載入身份檔案：~500 tokens
- 載入今日記憶：~300 tokens  
- 載入長期記憶：~200 tokens
- 搜尋操作：~100 tokens
- 總計：~1,100 tokens

優化後可能節省：
- 精簡記憶：減少 30% → 770 tokens
- 智慧載入：減少 20% → 616 tokens
- 避免冗餘：減少 10% → 554 tokens

總節省：約 50% 的 token 使用量！
""")
    
    print("=" * 60)
    print("🚀 立即行動:")
    print("=" * 60)
    
    print("""
1. 我已經建立了 QUICK_REFERENCE.md
2. 建議你檢視並精簡 MEMORY.md
3. 我可以幫你清理舊的每日記憶
4. 我們可以建立更系統化的記憶結構
""")
    
    print("=" * 60)
    print("🎉 記憶優化建議完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()