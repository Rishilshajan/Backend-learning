🗓️ Day 4 — Flask Setup & First API
🎯 Focus:

Setting up Flask environment, writing your first API routes, and revising advanced Python and Java syntax concepts.


🧩 1️⃣ Environment Setup — Flask + venv
🔹 Objective: To create an isolated workspace for Flask development and configure the editor for a smooth workflow.


⚙️ What is a Virtual Environment (venv)?
=> A virtual environment is an isolated Python environment that allows you to install project-specific dependencies without affecting global packages.

💡 Analogy:
Think of it like a private workspace within your system — just like how variables inside a function exist only within that function.


✅ Steps to Create and Activate venv
# Step 1: Create virtual environment
python3 -m venv venv

# Step 2: Activate environment
source venv/bin/activate          # macOS/Linux
# or
venv\Scripts\activate             # Windows

# Step 3: Install Flask
pip install flask

Once installed, check the version:
python -m flask --version


🟢 Output Example:
Flask 3.1.2
Werkzeug 3.1.3
Jinja2 3.1.6
Python 3.12.x


🧠 Why Use venv:

Keeps dependencies clean and project-specific
Prevents version conflicts
Simplifies deployment (via requirements.txt)


📁 Project Structure

FLASK/
│
├── venv/                 # virtual environment
├── app.py                # main Flask app
├── templates/            # (optional) HTML templates
├── static/               # (optional) CSS/JS files
└── requirements.txt      # list of dependencies

To export dependencies:
pip freeze > requirements.txt


🧩 2️⃣ Hands-On: Your First Flask API
🔹 Objective:
Write your first API with:
A root route (/) returning a text message
A /info route returning JSON data


✅ Code: app.py
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Backend Developer!"

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "name": "John Doe",
        "date": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)


🔹 Explanation:
@app.route('/') → Defines the root endpoint (the home page).

return "Hello Backend Developer!" → Sends a plain text response.

/info route returns a JSON response with:

name → developer name

date → current timestamp in ISO format


✅ Run the Application
source venv/bin/activate
python app.py


Open your browser:

http://127.0.0.1:5000/ → shows Hello Backend Developer!

http://127.0.0.1:5000/info → returns your name + date in JSON


Testing via curl:
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/info


✅ Expected Output:
Hello Backend Developer!
{"name": "John Doe", "date": "2025-11-10T10:00:00+05:30"}


🧩 Concept Recap
Concept	                   Description
Flask	                   Lightweight Python web framework
@app.route()	           Decorator that binds a function to a specific URL
Routing	                   Mapping URLs to Python functions
jsonify()	               Converts Python data into JSON response
debug=True	               Enables auto-reload and error visibility during development


🧠 3️⃣ Syntax Hour (“Refresher Mode 4”)
🟦 Python — Decorators, *args, **kwargs
🔹 1. Decorators

A decorator modifies or enhances the behavior of a function without changing its actual code.

💡 Analogy:
Think of it like wrapping a gift — you enhance it, but the content remains the same.


def uppercase(func):
    def wrapper():
        msg = func()
        return msg.upper()
    return wrapper

@uppercase
def greet():
    return "hello backend developer"

print(greet())

🟢 Output: HELLO BACKEND DEVELOPER


🔹 **2. *args and kwargs
✅ *args — Variable-length positional arguments
def total(*args):
    s = 0
    for i in args:
        s += i
    return s

print(total(10, 20, 30))  # 60

*args collects positional arguments into a tuple.

✅ **kwargs — Variable-length keyword arguments
def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

details(name="John Doe", age=21, city="Paris")

🟢 Output:
name: John Doe
age: 21
city: Paris


🟨 Java — Classes and Constructors (10 min Refresher)
🔹 Class and Object Basics

A class is a blueprint; an object is an instance of that class.
public class Person {
    String name;
    int age;

    // Constructor
    Person(String n, int a) {
        this.name = n;
        this.age = a;
    }

    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    public static void main(String[] args) {
        Person p1 = new Person("John Doe", 21);
        p1.display();
    }
}

🟢 Output:	Name: John Doe, Age: 21


✅ Constructor Notes
Feature            	Description
Constructor	        Special method called when an object is created
Name	            Must match class name
Return Type	        None (not even void)
Overloading	        You can have multiple constructors with different parameters

🧾 4️⃣ Summary
Section	                Focus	                         Key Learning
Environment Setup	    Flask + venv	                 Isolated workspace setup for backend development
First API	            / and /info routes	             Routing, jsonify, app.run(debug=True)
Python Refresher	    Decorators, *args, **kwargs	     Advanced syntax features for clean, reusable code
Java Refresher	        Classes & Constructors	         Object-oriented fundamentals

* For more references , check demo.py of FLASK folder.