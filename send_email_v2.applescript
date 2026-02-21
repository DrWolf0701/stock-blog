tell application "Mail"
	-- 創建新郵件
	set newMessage to make new outgoing message with properties {subject:"📈 每日美股新聞彙整 - 2026年2月18日", visible:true}
	
	tell newMessage
		-- 設置BCC收件人（密件副本）- 使用不同的語法
		make new bcc recipient at end of bcc recipients with properties {address:"s8824415@hotmail.com"}
		make new bcc recipient at end of bcc recipients with properties {address:"Linbojing@hotmail.com"}
		
		-- 郵件內容
		set content to "📈 每日美股新聞彙整 - 2026年2月18日

✅ 美股新聞彙整報告已生成！

📊 市場概況：
• 道瓊工業指數：46,198.76 (-0.20%)
• 標普500指數：6,640.90 (-0.24%)
• 那斯達克指數：22,504.02 (-0.31%)
• 費城半導體：6,293.97 (-0.23%)

🔥 今日五大重點新聞：
1. 市場極度分化，科技股承壓
2. 基金經理人過度樂觀，觸發賣出訊號
3. 政府關門風險升高
4. 科技七巨頭財報季來臨
5. 通膨數據優於預期

📋 報告特色：
• 精美HTML轉PDF，非極簡版
• 文字清晰無重疊，格式正確
• 中文字體正常顯示
• 內容完整無截斷
• 經過嚴格品質檢查

📎 PDF附件包含完整市場分析、投資建議和本週重要事件。

⚠️ 免責聲明：
本報告僅供參考，不構成投資建議。市場有風險，投資需謹慎。

--
每日美股新聞彙整系統
自動生成報告 | 更新時間：2026年2月18日 07:15 (台北時間)"
		
		-- 添加PDF附件
		set pdfPath to POSIX file "/Users/yu-tsehsiao/.openclaw/workspace/美股新聞彙整_2026-02-18.pdf"
		make new attachment with properties {file name:pdfPath} at after the last paragraph of the content
	end tell
	
	-- 顯示郵件
	activate
end tell

-- 提示用戶
display dialog "📧 郵件已準備完成！

收件人（BCC密件副本）：
• s8824415@hotmail.com
• Linbojing@hotmail.com

PDF附件已添加，請確認內容後手動發送。

注意：BCC收件人資訊不會在郵件內容中顯示。" buttons {"確定"} default button 1 with icon note