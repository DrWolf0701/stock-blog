# 🐻 記憶索引

## 📅 最後更新
2026-02-13 15:30

## 🔑 核心資訊索引

### 身份設定
- **我的身份**：OpenClaw (熊抱哥風格) - 見 `IDENTITY.md`
- **使用者**：Chris - 見 `USER.md`
- **行為準則**：直接、朋友模式 - 見 `SOUL.md`

### 已建立能力
#### 影片處理
- 工具：FFmpeg, OpenCV, PIL, moviepy
- 能力：影片生成、剪輯、文字顯示
- 關鍵學習：OpenCV 無法顯示中文，需用 PIL
- 範例：熊抱哥賀歲影片 (10秒)

#### 文件生成
- PDF：reportlab (已測試)
- Excel：pandas, openpyxl (已測試)
- PPT：python-pptx (已測試，需調整參數)

#### 開發環境
- Python 虛擬環境：`python_project/venv`
- VS Code 完整設定
- 常用套件：pandas, numpy, matplotlib 等

#### 模型管理
- 當前模型：deepseek/deepseek-chat
- 備用模型：GPT (openai/gpt-5.1-codex)
- 切換模式：模式 A (我建議，你決定)

### 重要決策記錄
#### 2026-02-13
- 影片文字顯示問題解決：改用 PIL 繪製中文
- 模型切換策略確定：模式 A
- 記憶優化策略：智慧載入機制

#### 2026-02-12
- 建立完整 Python 開發環境
- 安裝 PDF/Excel/PPT 生成能力
- 測試 Peekaboo 螢幕截圖

#### 2026-02-11
- 初次設定：熊抱哥風格
- 建立身份檔案
- 開始美股新聞報告功能

### 聯絡資訊
- Telegram：DrWolf (ID: 8591494215)
- WhatsApp：+886963676670

### 專案目錄結構
```
workspace/
├── python_project/          # Python 開發專案
│   ├── venv/               # 虛擬環境
│   ├── video_output/       # 影片生成輸出
│   ├── minimal_output/     # 最小檔案測試
│   └── *.py               # 各種功能腳本
├── memory/                 # 每日記憶
│   ├── 2026-02-11.md
│   ├── 2026-02-12.md
│   └── 2026-02-13.md
└── MEMORY.md              # 完整長期記憶
```

### 快速查詢指南
#### 當需要影片功能時：
1. 檢查 `python_project/video_output/`
2. 參考 `python_project/create_lotso_video_fixed.py`
3. 關鍵：使用 PIL 處理中文字體

#### 當需要文件生成時：
1. 檢查 `python_project/minimal_output/`
2. 參考對應的生成腳本

#### 當需要開發環境時：
1. 進入 `python_project/`
2. 執行 `source venv/bin/activate`

### 成本節省策略
1. **智慧載入**：分層載入記憶
2. **精簡內容**：只載入必要資訊
3. **索引查詢**：先查索引，再載入詳細
4. **定期清理**：壓縮舊記憶檔案

---
*此索引檔案約 1.2KB，代替載入完整的 MEMORY.md (可能數十KB)*