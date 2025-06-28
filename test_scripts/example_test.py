import requests

base_url = "https://blackbox-interface.vercel.app"

headers = {
    "Content-Type": "application/json"
}

endpoints = [
    "/endpoint1",
    "/endpoint2",
    "/endpoint3",
    "/endpoint4",
    "/endpoint5"
]

test_inputs = [
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
    for data in test_inputs:
        try:
            res = requests.post(base_url + endpoint, headers=headers, json=data)
            print(f"Input: {data['input']}\n→ Output: {res.json()}")
        except Exception as e:
            print(f"❌ Error on {endpoint} with input {data['input']}: {e}")
