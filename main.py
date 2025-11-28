
import requests
import datetime

def run_api():
    url = "https://api.example.com/data"  # Replace with your API endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"[{datetime.datetime.now()}] API call successful!")
        print(response.json())  # Print or process the data
    else:
        print(f"[{datetime.datetime.now()}] API call failed: {response.status_code}")

if __name__ == "__main__":
    run_api()
