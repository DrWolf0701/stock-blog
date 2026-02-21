tell application "Mail"
	-- 確保Mail應用程式開啟
	activate
	
	-- 創建新郵件
	set theMessage to make new outgoing message with properties {subject:"國際重點新聞摘要 - 2026年2月14-15日（可讀版）", content:"親愛的 Chris：

以下是為您整理的2026年2月14-15日國際重點新聞摘要。

**已解決PDF顯示問題：**
- 重新創建純文本PDF，文字可選取
- 使用系統中文字體（STHeiti）
- 確保在所有PDF閱讀器中正常顯示

**主要新聞：**
1. 台美簽署貿易協定
2. 古巴取消雪茄節
3. 蘇丹人道危機
4. 歐洲央行新政策
5. 巴西女性安全運動

附件為可讀版PDF檔案，文字可選取、可複製。

祝您有個美好的一天！

小熊抱 AI助手 🧸🤗
2026年2月15日"}
	
	-- 設定收件人
	tell theMessage
		make new to recipient at end of to recipients with properties {address:"s8824415@hotmail.com"}
	end tell
	
	-- 顯示郵件視窗
	set visible of theMessage to true
	
	-- 提示用戶手動添加附件
	display dialog "郵件已創建！" & return & return & ¬
		"請手動添加附件：" & return & ¬
		"國際重點新聞_simple.pdf" & return & return & ¬
		"步驟：" & return & ¬
		"1. 點擊「附加」按鈕" & return & ¬
		"2. 選擇檔案：國際重點新聞_simple.pdf" & return & ¬
		"3. 確認後發送郵件" buttons {"確定"} default button "確定"
end tell