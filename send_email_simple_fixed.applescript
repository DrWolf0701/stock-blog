tell application "Finder"
	set pdfPath to (container of (path to me) as text) & "國際重點新聞_final.pdf"
	set pdfFile to pdfPath as alias
end tell

tell application "Mail"
	-- 創建新郵件
	set newMsg to make new outgoing message with properties {subject:"國際重點新聞摘要 - 2026年2月14-15日（修復版）", content:"親愛的 Chris：

以下是為您整理的2026年2月14-15日國際重點新聞摘要。

**已修復PDF亂碼問題，確保中文字體正確顯示。**

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
	
	tell newMsg
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
		make new attachment with properties {file name:pdfFile}
	end tell
	
	set visible of newMsg to true
	activate
	
	display dialog "修復版郵件已準備好！" & return & return & ¬
		"請檢查 Mail 應用程式，" & return & ¬
		"確認PDF內容正常後發送。" buttons {"確定"} default button "確定"
end tell