#!/usr/bin/env python3
"""
記憶優化工具
幫助節省 API 費用
由 OpenClaw 建立 🐻
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
import json

class MemoryOptimizer:
    def __init__(self, workspace_path):
        self.workspace = Path(workspace_path)
        self.memory_dir = self.workspace / "memory"
        self.memory_file = self.workspace / "MEMORY.md"
        
    def analyze_memory_usage(self):
        """分析記憶使用狀況"""
        print("🔍 分析記憶使用狀況...")
        
        stats = {
            "total_files": 0,
            "total_size_bytes": 0,
            "total_lines": 0,
            "files": []
        }
        
        # 分析 MEMORY.md
        if self.memory_file.exists():
            size = os.path.getsize(self.memory_file)
            lines = self.count_lines(self.memory_file)
            stats["total_files"] += 1
            stats["total_size_bytes"] += size
            stats["total_lines"] += lines
            stats["files"].append({
                "name": "MEMORY.md",
                "size": size,
                "lines": lines,
                "type": "long_term"
            })
            print(f"  📄 MEMORY.md: {size:,} bytes, {lines} 行")
        
        # 分析每日記憶
        if self.memory_dir.exists():
            for file in self.memory_dir.glob("*.md"):
                size = os.path.getsize(file)
                lines = self.count_lines(file)
                stats["total_files"] += 1
                stats["total_size_bytes"] += size
                stats["total_lines"] += lines
                stats["files"].append({
                    "name": file.name,
                    "size": size,
                    "lines": lines,
                    "type": "daily"
                })
        
        # 計算估計 token 數（粗略估計）
        estimated_tokens = stats["total_lines"] * 20  # 每行約20個token
        
        print(f"\n📊 統計結果:")
        print(f"  檔案數量: {stats['total_files']}")
        print(f"  總大小: {stats['total_size_bytes']:,} bytes")
        print(f"  總行數: {stats['total_lines']}")
        print(f"  估計 token 數: {estimated_tokens:,}")
        print(f"  估計成本 (deepseek-chat): ${estimated_tokens / 1000000 * 0.0:.4f}")
        
        return stats
    
    def count_lines(self, filepath):
        """計算檔案行數"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except:
            return 0
    
    def create_memory_index(self):
        """建立記憶索引"""
        print("\n📑 建立記憶索引...")
        
        index = {
            "created_at": datetime.now().isoformat(),
            "sections": {}
        }
        
        # 從 MEMORY.md 提取關鍵資訊
        if self.memory_file.exists():
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取章節
            sections = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            index["sections"]["MEMORY"] = {
                "sections": sections[:10],  # 只取前10個章節
                "size": os.path.getsize(self.memory_file),
                "lines": self.count_lines(self.memory_file)
            }
        
        # 建立每日記憶索引
        daily_files = []
        if self.memory_dir.exists():
            for file in sorted(self.memory_dir.glob("*.md")):
                daily_files.append({
                    "date": file.stem,
                    "size": os.path.getsize(file),
                    "lines": self.count_lines(file)
                })
        
        index["daily_files"] = daily_files[-7:]  # 最近7天
        
        # 儲存索引
        index_path = self.workspace / "memory_index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ 索引已建立: {index_path}")
        return index
    
    def optimize_daily_memory(self, keep_days=7):
        """優化每日記憶，只保留最近幾天"""
        print(f"\n🗑️  優化每日記憶 (保留最近 {keep_days} 天)...")
        
        if not self.memory_dir.exists():
            print("  ⚠️ 記憶目錄不存在")
            return
        
        cutoff_date = datetime.now() - timedelta(days=keep_days)
        
        deleted_count = 0
        kept_count = 0
        
        for file in self.memory_dir.glob("*.md"):
            try:
                # 從檔名解析日期
                date_str = file.stem
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                
                if file_date < cutoff_date:
                    # 壓縮舊檔案
                    self.compress_memory_file(file)
                    deleted_count += 1
                else:
                    # 優化新檔案格式
                    self.optimize_memory_format(file)
                    kept_count += 1
                    
            except ValueError:
                print(f"  ⚠️ 無法解析日期: {file.name}")
        
        print(f"  ✅ 完成: 保留 {kept_count} 個檔案，壓縮 {deleted_count} 個舊檔案")
    
    def compress_memory_file(self, filepath):
        """壓縮記憶檔案"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 建立摘要版本
            lines = content.split('\n')
            summary = []
            
            # 保留標題和重要項目
            for line in lines:
                if line.startswith('#') or line.startswith('- ') or line.startswith('•'):
                    if len(line) < 100:  # 只保留簡短的重要項目
                        summary.append(line)
            
            # 限制行數
            if len(summary) > 20:
                summary = summary[:20]
                summary.append("... (已壓縮)")
            
            compressed_content = '\n'.join(summary)
            
            # 重新寫入
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(compressed_content)
            
            original_size = os.path.getsize(filepath)
            print(f"  📦 壓縮: {filepath.name} ({len(lines)} → {len(summary)} 行)")
            
        except Exception as e:
            print(f"  ❌ 壓縮失敗 {filepath.name}: {e}")
    
    def optimize_memory_format(self, filepath):
        """優化記憶格式"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 優化格式：移除冗餘空格、合併短行
            lines = content.split('\n')
            optimized = []
            
            for line in lines:
                line = line.strip()
                if line:  # 跳過空行
                    # 合併過短的行
                    if optimized and len(optimized[-1]) < 50 and len(line) < 50:
                        optimized[-1] = optimized[-1] + " " + line
                    else:
                        optimized.append(line)
            
            optimized_content = '\n'.join(optimized)
            
            # 如果明顯變小才寫回
            if len(optimized_content) < len(content) * 0.9:  # 至少減少10%
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(optimized_content)
                print(f"  ✨ 優化: {filepath.name} ({len(content)} → {len(optimized_content)} 字元)")
            
        except Exception as e:
            print(f"  ⚠️ 優化失敗 {filepath.name}: {e}")
    
    def create_quick_reference(self):
        """建立快速參考指南"""
        print("\n📋 建立快速參考指南...")
        
        quick_ref = """# 🐻 OpenClaw 快速參考指南

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
""".format(datetime=datetime)
        
        ref_path = self.workspace / "QUICK_REFERENCE.md"
        with open(ref_path, 'w', encoding='utf-8') as f:
            f.write(quick_ref)
        
        print(f"  ✅ 快速參考指南已建立: {ref_path}")
        return ref_path
    
    def run_full_optimization(self):
        """執行完整優化流程"""
        print("=" * 60)
        print("🐻 記憶優化工具")
        print("=" * 60)
        
        # 1. 分析現狀
        stats = self.analyze_memory_usage()
        
        # 2. 建立索引
        index = self.create_memory_index()
        
        # 3. 優化每日記憶
        self.optimize_daily_memory(keep_days=7)
        
        # 4. 建立快速參考
        ref_path = self.create_quick_reference()
        
        # 5. 最終分析
        print("\n" + "=" * 60)
        print("📊 優化結果總結:")
        
        # 重新分析
        new_stats = self.analyze_memory_usage()
        
        reduction = stats["total_size_bytes"] - new_stats["total_size_bytes"]
        if reduction > 0:
            print(f"  ✅ 節省空間: {reduction:,} bytes")
            print(f"  📉 減少比例: {reduction/stats['total_size_bytes']*100:.1f}%")
        else:
            print("  ⚠️ 空間無明顯減少")
        
        print(f"\n💡 建議:")
        print("  1. 使用 QUICK_REFERENCE.md 快速查閱")
        print("  2. 定期執行此優化工具")
        print("  3. 使用 memory_index.json 查詢詳細記憶")
        print("  4. 保持每日記憶簡潔")
        
        print("\n" + "=" * 60)
        print("🎉 記憶優化完成！")
        print("=" * 60)

def main():
    """主程式"""
    workspace_path = "/Users/yu-tsehsiao/.openclaw/workspace"
    optimizer = MemoryOptimizer(workspace_path)
    optimizer.run_full_optimization()

if __name__ == "__main__":
    main()