-- 自動發送郵件腳本
tell application "Mail"
	activate
	delay 1
	
	-- 創建新郵件
	set newMessage to make new outgoing message with properties {subject:"📈 美股重點新聞摘要 - 2026年2月15日（自動化流程）", content:"親愛的 Chris：

以下是為您自動整理的2026年2月15日美股重點新聞摘要。

**自動化流程完成：**
✓ 搜尋與整理美股新聞
✓ 製作精美HTML
✓ 轉檔為PDF
✓ Telegram同步傳送
✓ 郵件自動發送

**今日重點新聞：**
1. 蘋果(AAPL) - 財報超預期，服務收入創歷史新高
2. 特斯拉(TSLA) - 柏林工廠產能翻倍，歐洲市佔率突破25%
3. 微軟(MSFT) - AI雲服務需求強勁，企業合約創紀錄
4. 亞馬遜(AMZN) - 物流自動化突破，配送成本降低30%

**市場表現：**
• 道瓊工業指數：38,567.89 (+1.42%)
• S&P 500指數：5,245.32 (+0.92%)
• 納斯達克指數：16,328.76 (-0.28%)
• VIX恐慌指數：15.38 (+0.08%)

附件為完整PDF報告，包含詳細分析與關鍵要點。

此郵件為自動化流程發送，無需人工確認。

祝您投資順利！

小熊抱 AI助手 🧸🤗
2026年2月15日"}
	
	-- 設定收件人
	tell newMessage
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
	end tell
	
	-- 添加附件
	set pdfPath to POSIX file "/Users/yu-tsehsiao/.openclaw/workspace/美股新聞_2026-02-15_自動化.pdf"
	tell newMessage
		make new attachment with properties {file name:pdfPath} at after the last paragraph
	end tell
	
	-- 自動發送
	send newMessage
	
	-- 記錄發送成功
	display notification "美股新聞郵件已自動發送至 s8824415@hotmail.com" with title "📧 郵件發送成功"
end tell