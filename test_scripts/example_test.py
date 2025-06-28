import requests
import json

BASE_URL = "https://blackbox-interface.vercel.app"
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
    print(f"\n--- {endpoint} ---")
    for payload in inputs:
        try:
            response = requests.post(BASE_URL + endpoint, headers=HEADERS, json=payload)
            response.raise_for_status()  # catch HTTP errors
            print(f"Input: {payload['input']}\n→ Output: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Network or HTTP error for {endpoint} with input {payload['input']}: {e}")
        except json.JSONDecodeError:
            print(f"❌ Response from {endpoint} with input {payload['input']} is not valid JSON")
