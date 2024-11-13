import requests

def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()
        data = response.json()
        print("Fetched Data:", data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_data()
