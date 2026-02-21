#!/bin/bash
# Python 開發環境啟動腳本

echo "🐻 啟動 Python 開發環境"
echo "================================"

# 檢查虛擬環境
if [ ! -d "venv" ]; then
    echo "❌ 虛擬環境不存在，正在建立..."
    python3 -m venv venv
fi

# 啟動虛擬環境
source venv/bin/activate

# 檢查套件
echo "🔧 檢查 Python 版本..."
python --version

echo "📦 檢查已安裝套件..."
pip list | head -20

echo ""
echo "🎯 可用指令："
echo "1. 執行主程式: python src/main.py"
echo "2. 執行測試: python -m pytest tests/"
echo "3. 啟動 Jupyter: jupyter notebook"
echo "4. 安裝套件: pip install <套件名稱>"
echo "5. 更新套件: pip install -r requirements.txt"
echo ""
echo "📁 專案目錄: $(pwd)"
echo "🐍 Python 路徑: $(which python)"
echo "================================"
echo "輸入 'exit' 離開虛擬環境"
echo ""

# 保持虛擬環境啟動狀態
exec $SHELL