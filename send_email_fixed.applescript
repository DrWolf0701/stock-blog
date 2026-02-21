tell application "Mail"
	-- 先關閉可能存在的舊郵件視窗
	try
		set outgoingMessages to outgoing messages
		repeat with msg in outgoingMessages
			try
				close window of msg
			end try
		end repeat
	end try
	
	-- 等待一下
	delay 1
	
	-- 創建新郵件
	set theMessage to make new outgoing message with properties {subject:"國際重點新聞摘要 - 2026年2月14-15日（修復版）", content:"親愛的 Chris：

以下是為您整理的2026年2月14-15日國際重點新聞摘要。

**已修復PDF亂碼問題：**
- 重新創建完整HTML結構
- 添加UTF-8字符編碼
- 確保中文字體正確顯示
- 使用weasyprint生成高品質PDF

**主要新聞：**
1. 台美簽署貿易協定
2. 古巴取消雪茄節
3. 蘇丹人道危機
4. 歐洲央行新政策
5. 巴西女性安全運動

詳細內容請參閱附件PDF檔案。

祝您有個美好的一天！

小熊抱 AI助手 🧸🤗
2026年2月15日"}
	
	-- 設定收件人
	tell theMessage
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
	end tell
	
	-- 添加附件（使用修復後的PDF）
	set pdfPath to "/Users/yu-tsehsiao/.openclaw/workspace/國際重點新聞_final.pdf"
	set theAttachment to POSIX file pdfPath
	tell theMessage
		make new attachment with properties {file name:theAttachment} at after the last paragraph
	end tell
	
	-- 顯示郵件視窗
	set visible of theMessage to true
	activate
	
	-- 提示用戶
	display dialog "修復版郵件已創建完成！" & return & return & ¬
		"附件：國際重點新聞_final.pdf（修復版）" & return & return & ¬
		"請檢查 Mail 應用程式中的郵件內容，" & return & ¬
		"確認PDF內容正常後點擊「傳送」按鈕。" buttons {"確定"} default button "確定"
end tell