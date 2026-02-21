#!/usr/bin/env python3
import subprocess
import json
import base64

# 讀取圖片並轉為base64
with open("/Users/yu-tsehsiao/.openclaw/media/inbound/file_4---688ac980-f575-48c7-a238-2dd2e21dca54.jpg", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

# 創建請求JSON
request_data = {
    "model": "llava:7b",
    "prompt": "請詳細描述這張圖片的內容，包括所有文字、圖表、數據等資訊。這是股票投資相關的圖片嗎？請盡可能詳細地描述表格中的數字和文字。",
    "images": [image_base64],
    "stream": False
}

# 寫入臨時文件
with open("/tmp/llava_request.json", "w") as f:
    json.dump(request_data, f)

print("正在使用LLaVA分析圖片...")
print("="*50)

# 使用curl發送請求
try:
    result = subprocess.run(
        ["curl", "-s", "-X", "POST", "http://localhost:11434/api/generate",
         "-H", "Content-Type: application/json",
         "-d", "@/tmp/llava_request.json"],
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        response = json.loads(result.stdout)
        print("圖片分析結果:")
        print("="*50)
        print(response.get("response", "沒有獲取到分析結果"))
    else:
        print(f"錯誤: {result.stderr}")
except Exception as e:
    print(f"執行錯誤: {str(e)}")