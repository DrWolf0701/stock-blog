-- 自動發送今日美股新聞郵件腳本
tell application "Mail"
	activate
	delay 1
	
	-- 創建新郵件
	set newMessage to make new outgoing message with properties {subject:"📈 每日美股新聞彙整 - 2026年2月16日（自動化流程）", content:"親愛的 Chris：

以下是為您自動整理的2026年2月16日美股新聞彙整。

**自動化流程完成：**
✓ 搜尋與整理美股新聞
✓ 製作精美HTML
✓ 轉檔為PDF
✓ 郵件自動發送

**昨日市場表現：**
• 道瓊工業指數：50,188.14 (+0.10%)
• 標普500指數：6,941.81 (-0.33%)
• 納斯達克指數：23,102.47 (-0.59%)

**今日重點新聞：**
1. DraftKings股價重挫17% - 2026年營收預測令人失望
2. Rivian財報超預期，股價飆升23%
3. Pinterest股價下跌20%，AI擔憂拖累表現
4. 標普500技術面受壓，在6,500-7,000點區間震盪
5. 2月12日市場溫和上漲，道瓊上漲186點

**關鍵要點：**
• 電動車板塊表現分化，Rivian強勢上漲
• 體育博彩行業增長放緩，DraftKings預測下調
• 科技股AI投資回報受質疑，市場更加謹慎
• 標普500指數技術面偏弱，需關注6,500點支撐位
• 市場波動性可能增加，建議保持適當現金水位

附件為完整PDF報告，包含詳細分析與市場數據。

此郵件為自動化流程發送，無需人工確認。

祝您投資順利！

小熊抱 AI助手 🧸🤗
2026年2月16日 上午7:00"}
	
	-- 設定收件人
	tell newMessage
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
	end tell
	
	-- 添加附件
	set pdfPath to POSIX file "/Users/yu-tsehsiao/.openclaw/workspace/美股新聞_極簡版_2026-02-16.pdf"
	tell newMessage
		make new attachment with properties {file name:pdfPath} at after the last paragraph
	end tell
	
	-- 自動發送
	send newMessage
	
	-- 記錄發送成功
	display notification "美股新聞郵件已自動發送至 s8824415@hotmail.com" with title "📧 郵件發送成功"
end tell