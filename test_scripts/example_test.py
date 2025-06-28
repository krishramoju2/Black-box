import requests
import json

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"Content-Type": "application/json"}

endpoints = ["/endpoint1", "/endpoint2", "/endpoint3", "/endpoint4", "/endpoint5"]
inputs = [
    {"input": "hello"},
    {"input": "WORLD"},
    {"input": "aeiou"},
    {"input": "12345"},
    {"input": "!@#$%"},
    {"input": "racecar"},
    {"input": "The quick brown fox"}
]

for endpoint in endpoints:
    print(f"\n--- Testing {endpoint} ---")
    for payload in inputs:
        try:
            url = BASE_URL + endpoint
            response = requests.post(url, headers=HEADERS, json=payload)
            response.raise_for_status()
            print(f"✅ Input: {payload['input']}\n→ Output: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"❌ HTTP error for {endpoint} with input {payload['input']}: {e}")
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON from {endpoint} with input {payload['input']}")
