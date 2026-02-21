# MEMORY.md - 小熊抱的長期記憶

## 關於 Chris
- **名字**：Chris
- **稱呼**：Chris
- **時區**：Asia/Taipei (GMT+8)
- **特點**：喜歡可愛氛圍，幫我充值了10美金API費用，希望我能賺回自己的API費用
- **興趣**：科技產品，測試不同API端點
- **聯絡方式**：WhatsApp、Telegram

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

## 學習與經驗

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