#!/usr/bin/env python3
import requests
import json
import base64
import sys

# 讀取圖片並轉為base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 使用Ollama API分析圖片
def analyze_image_with_llava(image_path, prompt):
    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"
    
    # 準備請求數據
    data = {
        "model": "llava:7b",
        "prompt": prompt,
        "images": [image_to_base64(image_path)],
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"錯誤: {response.status_code} - {response.text}"
    except Exception as e:
        return f"API請求錯誤: {str(e)}"

if __name__ == "__main__":
    image_path = "/Users/yu-tsehsiao/.openclaw/media/inbound/file_4---688ac980-f575-48c7-a238-2dd2e21dca54.jpg"
    prompt = "請詳細描述這張圖片的內容，包括所有文字、圖表、數據等資訊。這是股票投資相關的圖片嗎？請盡可能詳細地描述表格中的數字和文字。"
    
    print("正在使用LLaVA分析圖片...")
    result = analyze_image_with_llava(image_path, prompt)
    print("\n" + "="*50)
    print("圖片分析結果:")
    print("="*50)
    print(result)