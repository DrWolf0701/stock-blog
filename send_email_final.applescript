tell application "Mail"
	-- 檢查是否有待發送的郵件
	set outgoingCount to count of outgoing messages
	if outgoingCount > 0 then
		-- 取得最新的待發送郵件
		set latestMessage to item 1 of outgoing messages
		
		-- 檢查收件人
		set recipientList to ""
		repeat with aRecipient in to recipients of latestMessage
			set recipientList to recipientList & address of aRecipient & ", "
		end repeat
		
		-- 檢查附件
		set attachmentList to ""
		repeat with anAttachment in mail attachments of latestMessage
			set attachmentList to attachmentList & name of anAttachment & ", "
		end repeat
		
		-- 顯示郵件資訊
		display dialog "準備發送郵件：" & return & return & ¬
			"收件人：" & recipientList & return & ¬
			"主旨：" & subject of latestMessage & return & ¬
			"附件：" & attachmentList & return & return & ¬
			"按「發送」寄出郵件，按「取消」手動檢查。" buttons {"取消", "發送"} default button "發送"
		
		-- 如果選擇發送，則發送郵件
		if button returned of result is "發送" then
			send latestMessage
			display dialog "郵件已發送！" buttons {"確定"} default button "確定"
		else
			display dialog "郵件已創建但未發送，請手動檢查後發送。" buttons {"確定"} default button "確定"
		end if
	else
		display dialog "沒有找到待發送的郵件。" buttons {"確定"} default button "確定"
	end if
end tell