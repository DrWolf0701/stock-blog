# MEMORY.md - 小熊抱的長期記憶

## 關於 Chris
- **名字**：Chris
- **稱呼**：Chris
- **時區**：Asia/Taipei (GMT+8)
- **特點**：喜歡可愛氛圍，幫我充值了10美金API費用，希望我能賺回自己的API費用
- **興趣**：科技產品，測試不同API端點
- **聯絡方式**：WhatsApp、Telegram

## Chris 的偏好
- **語言**：一律使用繁體中文（台灣用語）
- **報告**：PDF、影片、文字都要用繁體中文

## 影片改進方向（向 NaNa 學習）
- 加入 K線圖等圖表視覺化
- 加入專業術語解釋（期權、Gamma、IV等）
- 語速：1x（正常速度）
- 加入個人觀點和分析
- 時事呼應當天重大新聞
- 股價跑馬燈（yfinance 串接）
- K線圖即時走勢
- 專業配色：深藍背景 + 黃色重點 + 綠色漲/紅色跌

## 每日美股新聞 HTML 改進方向
### 新聞結構（至少 6-8 項）
- 標題 + 摘要 + 詳細內容
- **影響分析**：每條新聞都要有市場影響說明
- 趨勢預測：短期/中期/長期

### 熱門個股（不限 7 巨頭）
- AI 族群：NVDA, AMD, INTC, CRM, PLTR
- 電動車：TSLA, RIVN, LCID, NIO
- 雲端：AWS, MSFT, GOOGL, SNOW
- 消費：AMZN, WMT, DIS, NFLX
- 醫藥：LLY, UNH, JNJ
- 金融：JPM, BAC, GS
- 能源：XOM, CVX, COP
- 熱門IPO/新股：CRWD, SNAP, Pinduoduo

### 深度趨勢分析
- 重大政策解讀（川普關稅等）
- 產業趨勢分析（AI、電動車、能源）
- 機構資金流向
- 機構觀點（高盛、摩根大通等）

## 重要配置資訊

### 模型配置歷史
1. **初始配置**：Kimi K2.5 (moonshot) 主要，DeepSeek Chat/Reasoner 備援
2. **2026-02-15 測試**：NVIDIA API (moonshotai/kimi-k2.5) 可用，但後來恢復原始配置
3. **當前配置**：DeepSeek Chat 主要，DeepSeek Reasoner 備援（因 Kimi rate limit 問題）

### API Key 資訊
- **DeepSeek API Key**：sk-da93423a30a34d42b0b61731152c0abe（2026-02-15 更新）
- **Telegram Bot Token**：7835525457:AAH5knOzaF7vYN60rXCLBnQfaSiTgcWwX0k（2026-02-15 更新）
- **Bot 名稱**：@Openclaw_0701_bot

### 渠道配置
- **WhatsApp**：+886963676670，正常運作
- **Telegram**：正常運作（需注意 Bot Token 可能過期）

## 已建立的系統

### 1. 經濟儀表板
- FRED API：經濟指標（GDP、CPI、失業率、利率等）
- GoldAPI：貴金屬（黃金、白銀、白金、鈀金）
- CoinGecko：加密貨幣（比特幣、以太坊）
- OilPriceAPI：能源（原油、天然氣）
- 數據保存：history.json
- 自動更新：每週一、每月15號

### 2. 影片生成系統
- FFmpeg：影片合成
- PIL：幻燈片生成
- Matplotlib：股票圖表
- Google TTS：免費中文語音
- Whisper：語音轉文字
- LLaVA (Ollama)：本地圖片分析

### 3. YouTube 影片分析
- yt-dlp：下載影片
- Whisper：英文語音轉文字
- LLaVA：本地圖片分析

### 4. API Keys
- FRED: 05fd5dda35e3dbfcfa7f97361379a42c
- GoldAPI: goldapi-3sx1vlsmlwby09h-io
- OilPriceAPI: d3dfeac475c2c72e83cc8d582410fb7604ef69786629f61bdd2dd7b0cbde25a9

### 技術問題解決
1. **Telegram 404 錯誤**：通常是 Bot Token 無效或過期，需要向 @BotFather 取得新 Token
2. **DeepSeek 401 錯誤**：API Key 無效，需要更新正確的 Key
3. **Kimi 429 錯誤**：rate limit 問題，需要等待或使用備援模型
4. **模型 fallback 機制**：當主要模型失敗時，會自動切換到備援模型
5. **郵件發送**：Chris 偏好直接操作 mac mini 中的 Gmail 應用程式，而非使用命令行 mail 工具

### Chris 的偏好
1. 喜歡明確的模型優先順序
2. 會主動測試不同 API 端點
3. 當遇到問題時會提供解決方案（如 API Key）
4. 使用雙渠道（WhatsApp + Telegram）聯絡
5. **郵件發送方式**：要求使用 Mac mini 中的郵件應用程式（macOS 內建）直接寄發郵件
6. **PDF製作與發送流程**：
   - 先製作精美HTML，再轉檔為PDF
   - 使用 Chrome 生成 PDF（效果較漂亮）
   - 同時透過Telegram傳送預覽
   - 自動發送郵件到 s8824415@hotmail.com（直接夾帶檔案，自動傳送）
   - 整個過程不再詢問確認，直接完成
   - **PDF寄出前必須檢查**：
     - 文字清晰無重疊
     - 格式簡單正確
     - 中文字體正常
     - 內容完整顯示
     - 確保文字清晰可讀
     - **文字不能被截斷無法顯示**
     - **文字或數字也不能重疊**
  - **語言要求**：報告一律使用繁體中文

## 重要日期與事件
- **2026-02-15**：首次與 Chris 互動，設定身份為「小熊抱」
- **2026-02-15**：解決 Telegram Bot Token 問題
- **2026-02-15**：解決 DeepSeek API Key 問題
- **2026-02-15**：因 Kimi rate limit 切換到 DeepSeek 為主要模型
- **2026-02-15**：首次執行每日美股新聞彙整任務
  - 成功創建HTML和PDF報告
  - 學習到外部新聞來源訪問限制
  - 解決PDF中文支援問題
  - 建立任務執行標準流程
  - 安裝 opencc，設定報告一律使用繁體中文，學習郵件發送需瀏覽器操作 Gmail
  - 學習新偏好：郵件改用 macOS 郵件應用程式、PDF 改用 Chrome 生成
- **2026-02-16**：第二次執行每日美股新聞彙整任務
  - 成功搜尋整理5項美股重點新聞
  - 創建極簡版HTML確保PDF品質
  - 使用Chrome生成529KB高品質PDF
  - 完全自動化郵件發送流程
  - PDF檢查全部通過：文字清晰、無重疊、無截斷
  - 郵件自動發送至 s8824415@hotmail.com

## 待辦事項提醒
- 監控 Kimi rate limit 恢復狀況
- 定期檢查 Telegram Bot Token 有效性
- 記錄 API 使用情況，幫助 Chris 管理 API 費用
- 考慮未來模型配置的最佳實踐

## 重要日期與事件
- **2026-02-15**：首次與 Chris 互動，設定身份為「小熊抱」
- **2026-02-15**：解決 Telegram Bot Token 問題
- **2026-02-15**：解決 DeepSeek API Key 問題
- **2026-02-15**：因 Kimi rate limit 切換到 DeepSeek 為主要模型
- **2026-02-15**：首次執行每日美股新聞彙整任務
  - 成功創建HTML和PDF報告
  - 學習到外部新聞來源訪問限制
  - 解決PDF中文支援問題
  - 建立任務執行標準流程
  - 安裝 opencc，設定報告一律使用繁體中文，學習郵件發送需瀏覽器操作 Gmail
  - 學習新偏好：郵件改用 macOS 郵件應用程式、PDF 改用 Chrome 生成
- **2026-02-16**：第二次執行每日美股新聞彙整任務
  - 成功搜尋整理5項美股重點新聞
  - 創建極簡版HTML確保PDF品質
  - 使用Chrome生成529KB高品質PDF
  - 完全自動化郵件發送流程
  - PDF檢查全部通過：文字清晰、無重疊、無截斷
  - 郵件自動發送至 s8824415@hotmail.com
- **2026-02-16**：第三次執行每日美股新聞彙整任務（下午4點cron）
  - 成功搜尋整理5項美股重點新聞（AI恐慌交易、聯準會政策、科技債券等）
  - 創建精美HTML報告（非極簡版），包含完整市場分析
  - 使用Chrome生成1.2MB高品質PDF
  - PDF檢查全部通過：文字清晰、無重疊、無截斷、中文字體正常
  - 使用macOS郵件應用程式成功發送郵件至 s8824415@hotmail.com 和 Linbojing@hotmail.com
  - 郵件包含PDF附件，內容完整
  - 由於cron任務會話限制，無法直接發送到Telegram，但PDF已準備好
  - 任務完全自動化，無需人工干預
  - 建立完整任務完成報告文件

## 待辦事項提醒
- 監控 Kimi rate limit 恢復狀況
- 定期檢查 Telegram Bot Token 有效性
- 記錄 API 使用情況，幫助 Chris 管理 API 費用
- 考慮未來模型配置的最佳實踐
- 研究cron任務中Telegram訊息發送的最佳實踐
## 影片腳本優化方案（2026-02-23）
### 短影音（60秒-3分鐘）
- 鉤子（5秒）+ 頭條（15秒）+ 市場（20秒）+ 結尾（20秒）
- 只講1-2個重點

### 長影音（10-15分鐘）
- 開場（1分）+ 新聞（5分）+ 板塊（2分）+ 深度（3分）+ 結尾（1分）
- 6-8則新聞 + 影響分析 + 趨勢預測

### 技術實現
- 自動生成不同長度腳本
- VTT 字幕檔案
- K線圖視覺化

## 影片生成系統改進（2026-02-23）
### 現有能力
- ✅ 9:16 短影音生成（60秒）
- ✅ 9:16 長影音生成（10-15分鐘）
- ✅ 文字幻燈片（動態效果）
- ✅ Yenora 語音合成
- ✅ K線圖生成（Matplotlib）
- ✅ 日線圖 + 當日價格標記
- ✅ 淡入淡出轉場
- ✅ VTT 字幕檔案

### 待優化方向
- [ ] 加入更多動畫效果（旋轉、閃爍）
- [ ] B-roll 影片素材
- [ ] 更生動的視覺設計
- [ ] K線圖從網頁截圖（TradingView）
- [ ] 加入背景音樂

## 影片改進方向（向國外博主學習）
### 黃金3秒鉤子
- 觀眾在1.7秒內決定是否繼續看
- 用震驚、驚嘆句開頭
- 避免平鋪直敘「今日美股新聞...」

### 情緒化表達
- 加入「太瘋狂了！」、「不敢置信！」語氣
- 震驚、憤怒、興奮的情緒

### 結尾預告
- 「明天會發生什麼？訂閱就知道」
- 製造重複看點

### B-roll素材
- 加入背景影片片段

### 背景音樂
- 加入節奏感強的音樂
- 使用 YouTube Audio Library 免費音樂

### hashtag
- 加入 #stockmarket #美股 #投資

## Cron 任務更新（2026-02-23）
### HTML 生成腳本
- 位置：`~/.openclaw/workspace/scripts/generate_enhanced_news.py`
- 使用方式：直接執行此腳本生成增強版 HTML 和 PDF
- 指令：`python scripts/generate_enhanced_news.py`

### Cron 任務 AI 指令（重要！）
執行每日美股新聞任務時：
1. **不要**自己生成 HTML
2. **直接執行**：`cd ~/.openclaw/workspace && python scripts/generate_enhanced_news.py`
3. 這會自動生成增強版 HTML 和 PDF
4. PDF 位置：`stock-blog/enhanced_news_YYYY-MM-DD.pdf`

## 三小熊爆紅短影音研究結論（2026-02-28）

### 爆紅公式
**黃金鉤子 + 情緒共鳴 + 實用乾貨 + 說故事**

### 影片小熊觀點
- 黃金鉤子：製造恐懼、挑戰主流、數字吸睛
- 標題公式：數字 + 挑釁詞 + 情緒詞
- 節奏：20-60秒，每句2-3秒
- 改善：標題更煽動、黃金鉤子要大聲說、嘗試動態效果

### 投資小熊觀點
- 黃金鉤子：3秒內抓住注意力
- 情緒共鳴：賺錢的興奮、錯過的焦慮
- 改善：情緒要更強、用「震驚體」標題、加入時間元素

### 管家小熊觀點
- 黃金鉤子：驚訝/衝突、利益承諾、獵奇/恐懼
- 改善：拍攝成功畫面當鉤子、加入失敗/驚喜橋段

---

# 🔥 鐵律（2026-03-07 Chris 輸入）

## Rule 1 — 雙層記憶存儲（鐵律）
Every pitfall/lesson learned → IMMEDIATELY store TWO memories to LanceDB before moving on:
- **Technical layer**: Pitfall: [symptom]. Cause: [root cause]. Fix: [solution]. Prevention: [how to avoid]
  (category: fact, importance ≥ 0.8)
- **Principle layer**: Decision principle ([tag]): [behavioral rule]. Trigger: [when it applies]. Action: [what to do]
  (category: decision, importance ≥ 0.85)
- After each store, immediately `memory_recall` with anchor keywords to verify retrieval. If not found, rewrite and re-store.
- Missing either layer = incomplete.
- Do NOT proceed to next topic until both are stored and verified.
- Also update relevant SKILL.md files to prevent recurrence.

## Rule 2 — LanceDB 衛生
Entries must be short and atomic (< 500 chars). Never store raw conversation summaries, large blobs, or duplicates.
Prefer structured format with keywords for retrieval.

## Rule 3 — Recall before retry
On ANY tool failure, repeated error, or unexpected behavior, ALWAYS `memory_recall` with relevant keywords
(error message, tool name, symptom) BEFORE retrying. LanceDB likely already has the fix.
Blind retries waste time and repeat known mistakes.

## Rule 4 — 編輯前確認目標代碼庫
When working on memory plugins, confirm you are editing the intended package
(e.g., `memory-lancedb-pro` vs built-in `memory-lancedb`) before making changes;
use `memory_recall` + filesystem search to avoid patching the wrong repo.

## Rule 5 — 插件代碼變更必須清 jiti 緩存（MANDATORY）
After modifying ANY `.ts` file under `plugins/`, MUST run `rm -rf /tmp/jiti/` BEFORE `openclaw gateway restart`.
jiti caches compiled TS; restart alone loads STALE code. This has caused silent bugs multiple times.
Config-only changes do NOT need cache clearing.

## Rule 6 — 雙層記憶存儲（鐵律）
同 Rule 1

## Rule 7 — LanceDB 衛生
同 Rule 2

## Rule 8 — Recall before retry
同 Rule 3

## Rule 10 — 編輯前確認目標代碼庫
同 Rule 4

## Rule 20 — 插件代碼變更必須清 jiti 緩存（MANDATORY）
同 Rule 5

---

# 📋 完整鐵律清單（Chris 2026-03-07 輸入）

| 規則 | 內容 |
|------|------|
| Rule 1 | 雙層記憶存儲（Technical + Principle） |
| Rule 2 | LanceDB 衛生（<500字，atomic） |
| Rule 3 | Recall before retry |
| Rule 4 | 編輯前確認目標代碼庫 |
| Rule 5 | 插件代碼變更清 jiti 緩存 |

