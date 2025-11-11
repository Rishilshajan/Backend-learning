from flask import Flask, request, jsonify, make_response
from datetime import datetime
import itertools

app = Flask(__name__)

todos = [
	{"id": 1, "title": "Learn Flask", "description": "Read docs & examples", "completed": False, "created_at": datetime.now().isoformat()}
]

id_counter = itertools.count(start = len(todos) + 1)

def find_todo(todo_id):
	return next((t for t in todos if t["id"] == todo_id), None)

@app.route("/todos", methods = ["GET"])
def list_todos():
	return jsonify(todos), 200	

@app.route("/todos/<int:todo_id>", methods=["GET"])	
def get_todo(todo_id):
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"Error, Todo not Found"}), 404
	return jsonify(todo), 200	

@app.route("/todos", methods=["POST"])
def create_todos():
	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	new_id = next(id_counter)

	title = data.get("title")
	if not title or not isinstance(title,str):
		return jsonify({"error": "Field 'title' is required and must be a string"}),400	

	description = data.get("description", "")

	completed = bool(data.get("completed", "False"))

	todo = {
		"id": new_id,
		"title":title,
		"description": description,
		"completed": completed,
		"created_at": datetime.now().isoformat()
	}	

	todos.append(todo)
	return jsonify(todo), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def replace_todos(todo_id):
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"error": "Todo not Found"}), 404

	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	title = data.get("title")
	if not title or not isinstance(title,str):
		return jsonify({"error": "Field 'title' is required and must be a string"}),400	

	todo["title"] = title
	todo["description"] = data.get("description", "")
	todo["completed"] = bool(data.get("completed", "False"))
	todo["updated_at"] = datetime.now().isoformat()

	return jsonify(todo), 200	

@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todos(todo_id):
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"error": "Todo not Found"}), 404

	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	if "title" in data:
		if not isinstance(title,str) or not data["title"]:
			return jsonify({"error": "Field 'title' is required and must be a string"}),400	
		todo["title"] = title
		
	if "description" in data:
		todo["description"] = str(data["description"])		

	if "completed" in data:
		todo["completed"] = bool(data["completed"])

	todo["updated_at"] = datetime.now().isoformat()	

	return jsonify(todo), 200	

@app.route("/todos/<int:todo_id>", methods = ["DELETE"])
def remove_todo(todo_id):
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"Error":"Todo not Found"}), 404

	todos.remove(todo)
	return jsonify({"message": f"Todo {todo_id} deleted"}),200	

if __name__ == "__main__":
	app.run(debug=True)	

