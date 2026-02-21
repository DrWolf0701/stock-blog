#!/bin/bash
# VS Code 擴充功能安裝腳本

echo "🐻 安裝 VS Code Python 開發擴充功能"
echo "========================================"

# 擴充功能清單
EXTENSIONS=(
    # Python 核心
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-toolsai.jupyter"
    "ms-toolsai.jupyter-keymap"
    "ms-toolsai.jupyter-renderers"
    
    # Python 工具
    "ms-python.black-formatter"
    "ms-python.flake8"
    "njpwerner.autodocstring"
    "kevinrose.vsc-python-indent"
    "littlefoxteam.vscode-python-test-adapter"
    
    # AI 輔助
    "visualstudioexptteam.vscodeintellicode"
    "github.copilot"
    
    # Web 框架
    "batisteo.vscode-django"
    "wholroyd.jinja"
    
    # 開發工具
    "gruntfuggly.todo-tree"
    "yzhang.markdown-all-in-one"
    "shardulm94.trailing-spaces"
    "eamodio.gitlens"
    
    # 容器化
    "ms-azuretools.vscode-docker"
    
    # 其他實用擴充
    "esbenp.prettier-vscode"
    "dbaeumer.vscode-eslint"
    "christian-kohler.path-intellisense"
    "formulahendry.code-runner"
)

echo "📦 總共 ${#EXTENSIONS[@]} 個擴充功能"

# 檢查 code 命令是否存在
if ! command -v code &> /dev/null; then
    echo "❌ VS Code 命令行工具未找到"
    echo "請先安裝 VS Code 並確保 'code' 命令可用"
    exit 1
fi

# 安裝擴充功能
for extension in "${EXTENSIONS[@]}"; do
    echo "正在安裝: $extension"
    code --install-extension "$extension" --force
done

echo ""
echo "========================================"
echo "✅ 擴充功能安裝完成！"
echo ""
echo "🎯 已安裝的擴充功能分類："
echo "1. Python 開發核心"
echo "2. Jupyter Notebook 支援"
echo "3. 程式碼格式化與檢查"
echo "4. AI 輔助程式設計"
echo "5. Web 框架支援"
echo "6. 開發效率工具"
echo "7. 版本控制"
echo "8. 容器化開發"
echo ""
echo "🚀 重新啟動 VS Code 以套用所有擴充功能"
echo "========================================"