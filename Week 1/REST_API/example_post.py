import requests
import json
from pathlib import Path

url = "https://jsonplaceholder.typicode.com/posts/"
path = Path("data.json")
payload = json.loads(path.read_text(encoding="utf-8"))

try:
	resp = requests.post(url, json= payload, timeout=6)
	print("Status Code:",resp.status_code)
	print("Data Created Successfully")
	data = resp.json()
	print(json.dumps(data, indent=2))
	
except requests.RequestException as e:
	print("Error Occured: ",e)	

