🗓️ Day 5 — Flask Routing & Templates
🎯 Focus:

Understanding Flask routing, HTTP methods, decorators, and developing a complete CRUD API using a simple in-memory Todo list.
Additionally, practicing form submission and API interaction using HTML + JavaScript fetch().


🧩 1️⃣ Concepts — Flask Routing, HTTP Methods, and app.route()
🔹 Routing in Flask

Routing defines how specific URLs map to functions in your Flask application.
Each route corresponds to a web address (endpoint) that executes a function when accessed.


💡 Analogy:
Think of Flask routing like a directory — each URL (like /about or /todos) points to a specific function.

✅ Basic Example:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Routing!"

@app.route('/about')
def about():
    return "This is the About page"


URL	       Function 	Response
/	       home()	    "Welcome to Flask Routing!"
/about	   about()	    "This is the About page"    


🔹 The @app.route() Decorator
Used to bind a URL to a function.

Parameters:
	=> path: URL endpoint
	=> methods: list of HTTP methods allowed (['GET'] by default)

Example: 
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "Hi there!"


🔹 HTTP Methods Overview
Method	       Purpose	                     Example Use
GET	           Retrieve data	             Display todo list
POST	       Create new resource	         Add new todo
PUT	           Replace a resource	         Update existing todo
PATCH	       Modify part of a resource	 Update completion status
DELETE	       Remove resource	             Delete a todo    


✅ In Flask, you specify methods per route:
@app.route('/data', methods=['GET', 'POST'])


🔹 Dynamic Routing
Flask supports parameters inside URLs:
@app.route('/user/<name>')
def greet_user(name):
    return f"Hello, {name}!"



🧩 2️⃣ Hands-On (1 hr) — Create CRUD API for Todo List(FLASK_API)
🧱 Objective:

Build a simple RESTful API for a Todo list using a temporary Python list as storage.(FLASK => App.py)    



🧪 Test the API (with curl)
🟢 List All Todos
curl http://127.0.0.1:5000/todos

🟢 Create a Todo
curl -X POST http://127.0.0.1:5000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": "Build CRUD API", "description": "Flask practice"}'

🟢 Get One Todo
curl http://127.0.0.1:5000/todos/1

🟢 Update a Todo
curl -X PUT http://127.0.0.1:5000/todos/1 \
     -H "Content-Type: application/json" \
     -d '{"completed": true, "description": "Updated!"}'

🟢 Delete a Todo
curl -X DELETE http://127.0.0.1:5000/todos/2


🧠 Concept Recap
Concept	                     Description
CRUD	                     Create, Read, Update, Delete operations
jsonify()	                 Converts Python dict/list to JSON response
request.get_json()	         Reads JSON body from client request
HTTP Codes	                 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found)
app.run(debug=True)          Auto-reload + debug mode for development     


🟩 3️⃣ Syntax Hour (“Refresher Mode 5”)[HTML + JS]
🔹 HTML Forms + JavaScript Fetch Requests

Forms collect data from users, and fetch() sends it to your Flask backend using HTTP.

* CRUD API for Todo List is present in app.py of Flask folder
* Syntax Snippets for HTML forms and Javascrpt Fetch is present in HTML + JS folder.