#GET REQUEST
'''
import requests

url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url)

# Check status
print(resp.status_code)        # e.g., 200

# Parse JSON
posts = resp.json()            # Python list (of dicts)
print(type(posts))             # <class 'list'>
print(len(posts))              # e.g., 100

# Access some fields
for pos in posts[:5]:
    print(pos['id'], pos['title'])
'''    


#GET PARTICULAR VALUE REQUESTS
'''
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if resp.status_code == 200:
    posts = resp.json()
    print(posts['title'], posts['body'])
else:
    print("Request failed:", resp.status_code)
'''


#POST REQUEST
'''
import requests

data = {"title": "foo", "body": "bar", "userId": 1}
resp = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(resp.status_code)   # usually 201 Created (or fake 201 for this service)
print(resp.json())        # server response with the new resource
'''


#QUERY STRINGS
'''
resp = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
posts = resp.json()
'''


