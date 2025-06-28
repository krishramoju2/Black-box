import requests

base_url = "https://blackbox-interface.vercel.app"

endpoints = [
    "/endpoint1",
    "/endpoint2",
    "/endpoint3",
    "/endpoint4",
    "/endpoint5"
]

test_cases = [
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
    for case in test_cases:
        try:
            res = requests.post(base_url + endpoint, json=case)
            print(f"Input: {case['input']}\n→ Output: {res.json()}")
        except Exception as e:
            print(f"Error on {endpoint} with input {case['input']}: {e}")
