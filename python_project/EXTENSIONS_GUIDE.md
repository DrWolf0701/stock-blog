# VS Code Python 擴充功能使用指南

由 OpenClaw 建立的完整 Python 開發環境 🐻

## 🎯 核心擴充功能

### 1. **Python (ms-python.python)**
- **功能**: Python 語言支援、除錯、測試
- **快捷鍵**:
  - `F5`: 執行/除錯
  - `Ctrl+Shift+P` → "Python: Select Interpreter": 選擇 Python 直譯器
  - `Ctrl+Shift+P` → "Python: Run Python File": 執行 Python 檔案

### 2. **Pylance (ms-python.vscode-pylance)**
- **功能**: 智能程式碼補全、類型檢查、文件提示
- **特色**: 快速、準確的程式碼分析

### 3. **Jupyter (ms-toolsai.jupyter)**
- **功能**: Jupyter Notebook 支援
- **快捷鍵**:
  - `Ctrl+Shift+P` → "Jupyter: Create New Jupyter Notebook"
  - `Shift+Enter`: 執行儲存格
  - `Ctrl+Enter`: 執行儲存格並停留在原處

## 🔧 開發工具

### 4. **Black Formatter (ms-python.black-formatter)**
- **功能**: 自動程式碼格式化
- **設定**: 儲存時自動格式化（已在設定中啟用）
- **格式**: PEP 8 兼容，行長 88 字元

### 5. **Flake8 (ms-python.flake8)**
- **功能**: 程式碼風格檢查
- **檢查項目**: PEP 8、程式碼複雜度、未使用變數等

### 6. **AutoDocstring (njpwerner.autodocstring)**
- **功能**: 自動生成文件字串
- **使用**: 在函數定義後輸入 `"""` 並按 Enter
- **快捷鍵**: `Ctrl+Shift+2` (macOS: `Cmd+Shift+2`)

### 7. **Python Indent (kevinrose.vsc-python-indent)**
- **功能**: 正確的 Python 縮排
- **特色**: 自動處理多行語句的縮排

## 🤖 AI 輔助

### 8. **IntelliCode (visualstudioexptteam.vscodeintellicode)**
- **功能**: AI 輔助程式碼補全
- **特色**: 基於 GitHub 上數百萬個開源專案的智慧建議

### 9. **GitHub Copilot (github.copilot)**
- **功能**: AI 配對程式設計
- **使用**: 輸入註解或部分程式碼，Copilot 會建議完整實現
- **快捷鍵**:
  - `Tab`: 接受建議
  - `Alt+[` / `Alt+]`: 切換建議

## 🌐 Web 開發

### 10. **Django (batisteo.vscode-django)**
- **功能**: Django 框架支援
- **特色**: 模板語法高亮、標籤補全、命令面板

### 11. **Jinja (wholroyd.jinja)**
- **功能**: Jinja2 模板語言支援
- **適用**: Flask、Django 模板

## 📊 開發效率

### 12. **Todo Tree (gruntfuggly.todo-tree)**
- **功能**: 收集所有 TODO、FIXME 註解
- **快捷鍵**: `Ctrl+Shift+T` 開啟 Todo 面板
- **標記**: `TODO:`, `FIXME:`, `BUG:`, `HACK:`

### 13. **GitLens (eamodio.gitlens)**
- **功能**: 增強 Git 功能
- **特色**: 行內 Git 紀錄、作者資訊、提交歷史

### 14. **Markdown All in One (yzhang.markdown-all-in-one)**
- **功能**: Markdown 編輯增強
- **快捷鍵**:
  - `Ctrl+B`: 粗體
  - `Ctrl+I`: 斜體
  - `Ctrl+Shift+]`: 預覽

## 🐳 容器化

### 15. **Docker (ms-azuretools.vscode-docker)**
- **功能**: Docker 容器管理
- **特色**: 建立、執行、管理 Docker 容器和映像

## 🚀 快速開始

### 啟用所有擴充功能
```bash
# 執行擴充功能安裝腳本
./setup_extensions.sh
```

### 常用工作流程
1. **開啟專案**: `code python_project/`
2. **選擇直譯器**: `Ctrl+Shift+P` → "Python: Select Interpreter" → 選擇 `venv/bin/python`
3. **執行測試**: 側邊欄點擊測試圖標，或執行 `python -m pytest tests/`
4. **建立 Notebook**: `Ctrl+Shift+P` → "Jupyter: Create New Jupyter Notebook"
5. **格式化程式碼**: 儲存時自動格式化，或 `Shift+Alt+F`

## ⚙️ 自訂設定

擴充功能設定可在以下位置調整：
1. **使用者設定**: `Ctrl+,` (macOS: `Cmd+,`)
2. **工作區設定**: `.vscode/settings.json`
3. **擴充功能設定**: 擴充功能面板 → 點擊齒輪圖標

## 🔍 擴充功能管理

```bash
# 列出已安裝擴充功能
code --list-extensions

# 安裝擴充功能
code --install-extension <extension-id>

# 解除安裝擴充功能
code --uninstall-extension <extension-id>
```

## 🐻 提示與技巧

1. **命令面板**: `Ctrl+Shift+P` 是 VS Code 最強大的功能
2. **快速開啟**: `Ctrl+P` 快速開啟檔案
3. **多重游標**: `Alt+Click` 建立多重游標
4. **行操作**: `Ctrl+X` 剪下行（未選取時）
5. **區塊選取**: `Shift+Alt+拖曳` 或 `Shift+Alt+方向鍵`

---

**建立時間**: 2026年2月12日  
**更新時間**: 2026年2月12日  
**建立者**: OpenClaw 可愛助理 🐻✨