import requests, base64

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = False

headers = {
    "Authorization": "Bearer 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",
    "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
    "model": "moonshotai/kimi-k2.5",
    "messages": [{"role":"user","content":"Hello, please respond briefly."}],
    "max_tokens": 1024,
    "temperature": 1.00,
    "top_p": 1.00,
    "stream": stream,
}

response = requests.post(invoke_url, headers=headers, json=payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
