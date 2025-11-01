🧭 Day 1 — Backend Learning Journal
🔹 Focus:

    Client–Server Basics | API Testing | Syntax Refresher | Mini DSA


1️⃣ Client–Server & What Happens When You Type a URL

Flow Overview:

	Browser → DNS Lookup → HTTP Request → Server → Response → Browser Render

Steps Explained:

1.DNS Lookup — Translates the domain name (e.g., google.com) to an IP address using Domain Name System.

2.TCP Connection — Browser opens a connection using 3 way Handshake.

3.HTTP Request — Browser sends method (GET, POST, etc.) and headers to the server.

4.Server Response — Server processes, runs backend code, and returns HTML/JSON + status code.

5.Browser Render — Browser interprets HTML, loads assets, and displays the page.

📘 Concept takeaway: DNS = address lookup | HTTP = conversation | Server = responder | Response = data returned


2️⃣ HTTP Methods & Status Codes
⚙️ HTTP Methods

Method    Purpose	               Example Use
GET	      Retrieve data          Fetch a user list
POST	    Create data	           Submit a form / add record
PUT	      Update/replace data	   Edit an existing record
DELETE	  Remove data	           Delete a post	

Exmaples:
GET     https://jsonplaceholder.typicode.com/posts
POST    https://jsonplaceholder.typicode.com/posts
PUT     https://jsonplaceholder.typicode.com/posts/1
DELETE  https://jsonplaceholder.typicode.com/posts/1


🧾 Common Status Codes
Code	                      Meaning	                     Notes
200 OK	                    Successful request	         Everything worked
201 Created	                New resource created	       Returned on POST success
204                         Created,No Content
301                         Moved Permanently
302                         Moved Temporarily
304                         Not Modified
400 Bad Request             Cannot understand Request
401 Unauthorized
403 Forbidden
404 Not Found	              Resource doesn’t exist	     Wrong URL/id
500 Internal Server Error	  Server-side error	           Code bug / crash
502 Bad Gateway             
503 Server Unavailable
504 Bad Gateway


3️⃣ API Testing — Postman | curl | Python requests
🧪 a) Using Postman

    1. Choose method → POST.

    2. Enter URL: https://jsonplaceholder.typicode.com/posts.

    3. Go to Body → raw → JSON and type:
	     { "title": "foo", "body": "bar", "userId": 1 }

    4. Click Send → observe status code 201 and response JSON.

=> GUI-based tool for visually building, testing & debugging APIs.


💻 b) Using curl (Command Line)

    1. curl -X POST https://jsonplaceholder.typicode.com/posts \
       -H "Content-Type: application/json" \
       -d '{"title":"foo","body":"bar","userId":1}'

=> Command-line HTTP client for quick inline testing or scripting.

c) Using Python requests

import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}

resp = requests.post(url, json=data)
print(resp.status_code)     # → 201
print(resp.json())          # → JSON response

=> Converts JSON directly to Python dict/list → easy to parse and use.


4️⃣ Syntax Refresher – Python | C | Java
* Python Loops
* List Comprehension
* Dict Comprehension
* C Loops
* Java Loops  


5️⃣ Mini DSA Tasks(Backend_Learning.ipynb)
* Reverse a String
* Count Character Frequency
