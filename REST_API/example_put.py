import requests, json
from pathlib import Path

url = "https://jsonplaceholder.typicode.com/posts/1"
path = Path("data.json")
payload = json.loads(path.read_text(encoding="utf-8"))
payload["Title"] = "Header"

try:
	resp = requests.put(url, json= payload, timeout=6)
	print("Status Code:",resp.status_code)
	print("Data Created Successfully")
	data = resp.json()
	print(json.dumps(data, indent=2))
	
except requests.RequestException as e:
	print("Error Occured: ",e)	

