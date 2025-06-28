import requests
import json
import time

base_url = "https://blackbox-interface.vercel.app"
endpoints = [
    "/api/reverse",
    "/api/uppercase",
    "/api/double",
    "/api/mystery",
    "/api/validate",
    "/api/fibonacci",
    "/api/hash"
]

test_inputs = [
    {"input": "hello"},
    {"input": "1234"},
    {"input": ""},
    {"input": "A very long input to see how it reacts to length"},
    {"input": "racecar"},
    {"input": "0"},
    {"input": "999999999"}
]

report = {}

def test_endpoint(endpoint):
    full_url = base_url + endpoint
    print(f"\nTesting endpoint: {full_url}")
    report[endpoint] = []

    for test in test_inputs:
        try:
            res = requests.post(full_url, json=test)
            output = res.text.strip()
        except Exception as e:
            output = f"ERROR: {str(e)}"
        
        print(f"Input: {test['input']} -> Output: {output}")
        report[endpoint].append({
            "input": test['input'],
            "output": output
        })
        time.sleep(0.5)  # Respectful delay

if __name__ == "__main__":
    for endpoint in endpoints:
        test_endpoint(endpoint)

    # Save report
    with open("blackbox_report.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print("\n✅ Testing complete. Results saved to blackbox_report.json")
