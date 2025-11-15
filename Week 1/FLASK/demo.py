# Hello World Code
'''
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello Backend Developer"

if __name__ == "__main__":
	app.run(debug=True)	
'''	


# Returning JSON Data
'''
from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello World"

@app.route("/info")
def info():
	name = os.getenv("DEV_NAME", "John Doe")
	iso_time = datetime.now().astimezone().isoformat()	
	payload = { "name": name, "time": iso_time}
	return jsonify(payload),200

print(app.url_map)

if __name__ == "__main__":
	app.run()	
'''


#Werkzeug Routing
'''
from flask import Flask
app = Flask(__name__)

def greet_user():
    return "Welcome, Rishil!"

app.add_url_rule("/welcome", "greet_user", greet_user)

if __name__ == "__main__":
    print("URL Map:", app.url_map)
    print("View Functions:", app.view_functions)
    app.run(debug=True)
'''    


#HTTP Methods
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify({"message": "Fetching users"})
    elif request.method == 'POST':
        return jsonify({"message": "Creating a new user"})

@app.route('/users/<int:id>', methods=['PUT', 'PATCH', 'DELETE'])
def user_operations(id):
    if request.method == 'PUT':
        return jsonify({"message": f"User {id} fully updated"})
    elif request.method == 'PATCH':
        return jsonify({"message": f"User {id} partially updated"})
    elif request.method == 'DELETE':
        return jsonify({"message": f"User {id} deleted"})

if __name__ == "__main__":
	app.run() 
'''	       

