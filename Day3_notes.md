🗓️ Day 3 — REST APIs + JSON Basics

🎯 Focus:

Understanding API communication, working with REST & GraphQL, practicing JSON read/write operations in Python, learning Node.js + TypeScript syntax, and solving a DSA drill.


🧩 1️⃣ API & REST Concepts
🔹 What is an API?

API (Application Programming Interface) acts as a bridge that allows two systems (client and server) to communicate and exchange data.

Example:
	https://api.weather.com/current?city=Paris


🌐 2️⃣ REST vs GraphQL

Feature	                   REST	                                            GraphQL
Definition	               Architecture using endpoints & HTTP methods	    Query language for APIs developed by Facebook
Endpoints	               Multiple (/users, /posts)	                    Single (/graphql)
Data Fetching	           Fixed response per endpoint	                    Client decides exact fields
Request Format	           HTTP (GET, POST, PUT, DELETE)	                Query-based
Best For	               CRUD-based APIs	                                Complex, data-intensive apps	


✅ REST Key Points
Uses HTTP methods:

Method	     Purpose
GET	         Retrieve data
POST	     Create new data
PUT	         Update/replace data
DELETE	     Remove data


🧠 GraphQL Example(GraphQL reduces over-fetching by allowing the client to request only specific fields.)
Query:
	{
  	 user(id: 1) {
    	name
    	email
  		}
	}

Response:
	{
  "data": {
    "user": {
      "name": "John Doe",
      "email": "johndoe@example.com"
    }
  }
}


🔗 3️⃣ API Endpoints & Request Bodies
🔹 Example API:
	https://jsonplaceholder.typicode.com/posts

Method	   Endpoint	     Description
GET	       /posts	     Fetch all posts
GET	       /posts/1	     Fetch post with ID 1
POST	   /posts	     Create new post
PUT	       /posts/1	     Update post with ID 1	


🔹 Request Body (Example)
Used in POST and PUT:
{
  "title": "Learning REST APIs",
  "body": "Practicing JSON and requests",
  "userId": 1
}


💻 4️⃣ Practical Session – JSON in Python
📁 Read JSON File:
import json 
from pathlib import Path

path = Path("data.json")
with path.open("r", encoding="utf-8") as f:
	data = json.load(f)
print("Loaded Data Type: ",type(data))
print(json.dumps(data, indent=0))	


📁 Write JSON File:
import json 
from pathlib import Path

path = Path("data.json")
data = json.loads(path.read_text(encoding="utf-8"))

data["last_updated"] = "2025-11-05T10:00:00+05:30"

path.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Updated data.json")	


📁 GET RQUEST:
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


📁 POST REQUEST:
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


📁 PUT REQUEST:
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


⚙️ 5️⃣ Syntax Hour (Node.js + TypeScript)
🟩 Node.js - Runs JavaScript outside the browser; Used for backend servers

Run code using node filename.js


🟨 JavaScript (ES6) Variables:
var name = "John";    // function-scoped
let age = 25;         // block-scoped
const PI = 3.14;      // constant value


🧠 TypeScript Basics -  Superset of JS; Adds Typing and Compile Type Checking to JS
let name: string = "John";
let age: number = 22;
let isActive: boolean = true;


🧩 Functions:
function add(a: number, b: number): number {
  return a + b;
}

const greet = (name: string): void => {
  console.log(`Hello, ${name}`);
};


🧾 Interface & Type Alias:
interface User {
  id: number;
  name: string;
  isActive: boolean;
}

type Product = {
  id: number;
  name: string;
  price?: number; // optional
};


🔗 Import & Export:
math.ts
export const add = (a: number, b: number): number => a + b;

main.ts
import { add } from "./math.js";
console.log(add(10, 5));


🧮 6️⃣ DSA Drill – Find 2nd Largest Number Without Sorting(Backend_learning.py)


