#!/bin/bash
# 每日自動修復腳本
# 由 OpenClaw 定時任務執行

echo "🐻 開始每日自動修復檢查..."
echo "時間: $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "========================================"

# 1. 檢查 OpenClaw 狀態
echo "1. 檢查 OpenClaw 狀態..."
openclaw status
STATUS_CODE=$?

if [ $STATUS_CODE -eq 0 ]; then
    echo "✅ OpenClaw 運行正常"
else
    echo "⚠️ OpenClaw 狀態異常，嘗試修復..."
    openclaw doctor --fix
fi

echo ""
echo "2. 檢查系統資源..."
# 檢查磁碟空間
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "   磁碟使用率: ${DISK_USAGE}%"

if [ $DISK_USAGE -gt 90 ]; then
    echo "   ⚠️ 磁碟空間不足，嘗試清理..."
    # 清理暫存檔案
    find /tmp -name "openclaw-*" -mtime +1 -delete 2>/dev/null
    find ~/.openclaw -name "*.log" -mtime +7 -delete 2>/dev/null
fi

# 檢查記憶體
MEM_FREE=$(free -m | awk 'NR==2 {print $4}')
echo "   可用記憶體: ${MEM_FREE}MB"

echo ""
echo "3. 檢查工作區狀態..."
WORKSPACE_DIR="$HOME/.openclaw/workspace"

if [ -d "$WORKSPACE_DIR" ]; then
    # 檢查檔案數量
    FILE_COUNT=$(find "$WORKSPACE_DIR" -type f | wc -l)
    echo "   工作區檔案數: ${FILE_COUNT}"
    
    # 檢查記憶檔案
    MEMORY_DIR="$WORKSPACE_DIR/memory"
    if [ -d "$MEMORY_DIR" ]; then
        MEMORY_FILES=$(find "$MEMORY_DIR" -name "*.md" | wc -l)
        echo "   記憶檔案數: ${MEMORY_FILES}"
        
        # 壓縮舊記憶檔案（保留最近7天）
        find "$MEMORY_DIR" -name "*.md" -mtime +7 -exec gzip {} \;
        echo "   ✅ 已壓縮7天前的記憶檔案"
    fi
else
    echo "   ❌ 工作區目錄不存在"
fi

echo ""
echo "4. 檢查 Python 環境..."
PYTHON_PROJECT="$WORKSPACE_DIR/python_project"
if [ -d "$PYTHON_PROJECT" ]; then
    # 檢查虛擬環境
    VENV_DIR="$PYTHON_PROJECT/venv"
    if [ -d "$VENV_DIR" ]; then
        echo "   ✅ Python 虛擬環境存在"
        
        # 檢查套件更新
        echo "   檢查 Python 套件狀態..."
        source "$VENV_DIR/bin/activate" 2>/dev/null
        if [ $? -eq 0 ]; then
            pip list --outdated | head -10
        fi
    else
        echo "   ⚠️ Python 虛擬環境不存在"
    fi
fi

echo ""
echo "5. 檢查定時任務..."
CRON_COUNT=$(crontab -l 2>/dev/null | grep -v "^#" | wc -l)
echo "   定時任務數: ${CRON_COUNT}"

echo ""
echo "6. 檢查權限問題..."
# 檢查重要目錄權限
IMPORTANT_DIRS=(
    "$HOME/.openclaw"
    "$WORKSPACE_DIR"
    "$PYTHON_PROJECT"
)

for dir in "${IMPORTANT_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        PERM=$(stat -f "%Sp" "$dir")
        OWNER=$(stat -f "%Su" "$dir")
        echo "   $dir: $PERM (所有者: $OWNER)"
    fi
done

echo ""
echo "7. 執行 OpenClaw 深度修復..."
echo "   執行 openclaw doctor --fix..."
openclaw doctor --fix

echo ""
echo "8. 產生修復報告..."
REPORT_FILE="$WORKSPACE_DIR/daily_fix_report_$(date '+%Y%m%d').txt"
{
    echo "每日修復報告 - $(date '+%Y-%m-%d %H:%M:%S')"
    echo "========================================"
    echo "1. OpenClaw 狀態: $([ $STATUS_CODE -eq 0 ] && echo '正常' || echo '已修復')"
    echo "2. 磁碟使用率: ${DISK_USAGE}%"
    echo "3. 可用記憶體: ${MEM_FREE}MB"
    echo "4. 工作區檔案數: ${FILE_COUNT}"
    echo "5. 記憶檔案數: ${MEMORY_FILES}"
    echo "6. 定時任務數: ${CRON_COUNT}"
    echo "7. 修復動作: 執行 openclaw doctor --fix"
    echo ""
    echo "📊 總結:"
    if [ $STATUS_CODE -eq 0 ] && [ $DISK_USAGE -lt 90 ] && [ $MEM_FREE -gt 100 ]; then
        echo "✅ 系統狀態良好，無需重大修復"
    else
        echo "⚠️ 系統需要關注，已執行修復動作"
    fi
} > "$REPORT_FILE"

echo "✅ 修復報告已儲存: $REPORT_FILE"

echo ""
echo "========================================"
echo "🐻 每日自動修復完成！"
echo "下次檢查: 明日凌晨5:00"
echo "========================================"