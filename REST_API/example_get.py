import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"
headers = {"Authorization": "Bearer <token>", "Accept": "application/json"}

try:
	resp = requests.get(url, params={"userId": 1}, headers= headers, timeout= 5)
	resp.raise_for_status()
	print("Status Code:",resp.status_code)
	data = resp.json()
	print(json.dumps(data, indent=2))

except requests.RequestException as e:
	print("Error Occured: ",e)	

