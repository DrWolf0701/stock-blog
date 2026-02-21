-- 開啟Mail應用程式
tell application "Mail"
	activate
	delay 1
	
	-- 顯示提示
	display dialog "📧 美股新聞郵件發送指南" & return & return & ¬
		"請手動執行以下步驟：" & return & return & ¬
		"1. 點擊「新增郵件」按鈕" & return & ¬
		"2. 收件人：s8824415@hotmail.com" & return & ¬
		"3. 主旨：📈 美股重點新聞摘要 - 2026年2月15日（精美版）" & return & ¬
		"4. 內容：" & return & ¬
		"   親愛的 Chris：" & return & ¬
		"   以下是為您整理的2026年2月15日美股重點新聞摘要。" & return & return & ¬
		"   主要新聞：" & return & ¬
		"   1. 蘋果(AAPL) - AI晶片突破" & return & ¬
		"   2. 特斯拉(TSLA) - 中國市場進展" & return & ¬
		"   3. 微軟(MSFT) - AI收購與雲服務" & return & ¬
		"   4. NVIDIA(NVDA) - 強勁財報" & return & return & ¬
		"   附件為精美版PDF，排版美觀、文字完整。" & return & return & ¬
		"   小熊抱 AI助手 🧸🤗" & return & ¬
		"   2026年2月15日" & return & return & ¬
		"5. 附件：美股重點新聞_精美版.pdf" & return & ¬
		"   檔案位置：/Users/yu-tsehsiao/.openclaw/workspace/" & return & return & ¬
		"6. 點擊「傳送」按鈕" buttons {"確定"} default button "確定"
end tell