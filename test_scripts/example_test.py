import requests
import json

# Replace this with the actual endpoint you want to test
url = "https://blackbox-interface.vercel.app/api/example"  # Dummy endpoint

def test_example_endpoint():
    test_inputs = [
        {"input": "hello"},
        {"input": "1234"},
        {"input": ""},
        {"input": "A very long input to see how it reacts to length"},
    ]

    for i, data in enumerate(test_inputs):
        response = requests.post(url, json=data)
        print(f"\nTest case {i+1}")
        print(f"Input: {data}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    test_example_endpoint()
