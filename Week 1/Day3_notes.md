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
Endpoints	                 Multiple (/users, /posts)	                      Single (/graphql)
Data Fetching	             Fixed response per endpoint	                    Client decides exact fields
Request Format	           HTTP (GET, POST, PUT, DELETE)	                  Query-based
Best For	                 CRUD-based APIs	                                Complex, data-intensive apps	


✅ REST Key Points
Uses HTTP methods:

Method	     Purpose
GET	         Retrieve data
POST	       Create new data
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
GET	       /posts	       Fetch all posts
GET	       /posts/1	     Fetch post with ID 1
POST	     /posts	       Create new post
PUT	       /posts/1	     Update post with ID 1	


🔹 Request Body (Example)
Used in POST and PUT:
{
  "title": "Learning REST APIs",
  "body": "Practicing JSON and requests",
  "userId": 1
}


💻 4️⃣ Practical Session – JSON in Python (REST_API => Files)
📁 Read JSON File

📁 Write JSON File

📁 GET RQUEST

📁 POST REQUEST

📁 PUT REQUEST


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


* Python Requests are present in REST_API Folder.
* DSA Tasks are present in Backend_Learning.ipynb


