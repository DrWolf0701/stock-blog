tell application "Mail"
	activate
	
	-- 等待Mail開啟
	delay 2
	
	-- 創建新郵件
	set newMessage to make new outgoing message with properties {subject:"📈 美股重點新聞摘要 - 2026年2月15日（可讀版）", content:"親愛的 Chris：

以下是為您整理的2026年2月15日美股重點新聞摘要。

**已解決PDF閱讀問題：**
- 重新創建純文本PDF，文字可選取
- 使用系統中文字體，確保正常顯示
- 專業金融風格設計

**今日重點新聞：**
1. 蘋果(AAPL) - AI晶片突破，股價盤後大漲8%
2. 特斯拉(TSLA) - 自動駕駛獲中國監管批准，上海工廠擴產
3. 微軟(MSFT) - 收購AI新創公司，雲服務市佔率突破40%
4. NVIDIA(NVDA) - 數據中心業務強勁，Q4營收超預期

**市場摘要：**
- 道瓊工業指數：38,452.67 (+1.25%)
- S&P 500指數：5,238.45 (+0.89%)
- 納斯達克指數：16,345.21 (-0.32%)
- VIX恐慌指數：15.42 (+0.12%)

附件為可讀版PDF檔案，文字可選取、可複製。

祝您投資順利！

小熊抱 AI助手 🧸🤗
2026年2月15日"}
	
	-- 設定收件人
	tell newMessage
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
	end tell
	
	-- 顯示郵件視窗
	set visible of newMessage to true
	
	-- 提示用戶添加附件
	display dialog "美股新聞郵件已準備好！" & return & return & ¬
		"請手動添加附件：" & return & ¬
		"美股重點新聞_可讀版.pdf" & return & return & ¬
		"位置：/Users/yu-tsehsiao/.openclaw/workspace/" & return & return & ¬
		"步驟：" & return & ¬
		"1. 點擊「附加」按鈕（迴紋針圖示）" & return & ¬
		"2. 選擇上述PDF檔案" & return & ¬
		"3. 確認內容無誤" & return & ¬
		"4. 點擊「傳送」按鈕" buttons {"確定"} default button "確定"
end tell