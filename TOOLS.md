# Tavily API 使用教學

## 什麼是 Tavily？
- AI 友善的搜尋 API
- 免費方案：每月 1,000 credits
- 搜尋一次：1-2 credits

## API Key（2026-03-07）
```
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
```

## 使用方法

### 1. curl 命令
```bash
curl -s -X POST "https://api.tavily.com/search" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "你的問題", "max_results": 5}'
```

### 2. Python
```python
import requests

url = "https://api.tavily.com/search"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "query": "你的問題",
    "max_results": 5
}

response = requests.post(url, json=data, headers=headers)
results = response.json()

for r in results.get("results", []):
    print(f"標題: {r['title']}")
    print(f"網址: {r['url']}")
    print(f"摘要: {r['content'][:200]}...")
    print("---")
```

### 3. Node.js
```javascript
const axios = require('axios');

const response = await axios.post('https://api.tavily.com/search', {
    query: '你的問題',
    max_results: 5
}, {
    headers: {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
});

console.log(response.data.results);
```

## 測試問題
- "WBC 2026 中華隊"
- "AI news today"
- "Apple 最新產品"
- "NVDA 財報"
- "Home Assistant 教學"

## 價格
- 免費：1,000 credits/月
- Basic 搜尋：1 credit/次
- Advanced 搜尋：2 credits/次

## 文件
- https://docs.tavily.com/

## 更新記錄
- 2026-03-07：首次啟用，API Key 取得
