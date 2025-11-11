from flask import Flask, request, jsonify, make_response
from datetime import datetime
import itertools


# Create the Flask application instance
app = Flask(__name__)


# -----------------------
# In-memory data storage
# -----------------------
# This is a temporary list of todos. Each todo is a dict with keys such as:
# id, title, description, completed, created_at, updated_at (optional)
todos = [
	{
		"id": 1,
		"title": "Learn Flask",
		"description": "Read docs & examples",
		"completed": False,
		"created_at": datetime.now().isoformat()
	}
]


# -----------------------
# ID generator
# -----------------------
# itertools.count gives us a lightweight, incrementing ID generator.
# We start after the number of existing todos so new IDs are sequential.
id_counter = itertools.count(start = len(todos) + 1)


# -----------------------
# Helper: find_todo
# -----------------------
def find_todo(todo_id):
	"""
	Find a todo by its integer id.
	Returns the todo dict if found, otherwise returns None.
	Using a generator expression with next(...) provides a concise one-liner.
	"""
	return next((t for t in todos if t["id"] == todo_id), None)


# -----------------------
# Route: List all todos
# GET /todos
# -----------------------
@app.route("/todos", methods = ["GET"])
def list_todos():
	"""
	Return the whole list of todos as JSON.
	Status code: 200 OK
	"""
	return jsonify(todos), 200	


# -----------------------
# Route: Get single todo
# GET /todos/<id>
# -----------------------
@app.route("/todos/<int:todo_id>", methods=["GET"])	
def get_todo(todo_id):
	"""
	Fetch a single todo by id.
	- If not found, returns 404.
	- If found, returns the todo dict with 200.
	"""
	todo = find_todo(todo_id)
	if not todo:
		# NOTE: The dict here is passed to jsonify. It should be {"error": "..."} or similar.
		# The current code uses a single-item set-like literal which still works with jsonify
		# but not as a canonical error object; consider changing key/value if you edit later.
		return jsonify({"Error, Todo not Found"}), 404
	return jsonify(todo), 200	


# -----------------------
# Route: Create a new todo
# POST /todos
# -----------------------
@app.route("/todos", methods=["POST"])
def create_todos():
	"""
	Create a new todo from the JSON request body.
	Validates presence and type of the required 'title' field.
	Returns 201 Created with the new todo on success.
	"""
	# Parse JSON body; silent=True returns None instead of raising on parse errors
	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	# Generate new id using the id generator
	new_id = next(id_counter)

	# Validate required 'title' field
	title = data.get("title")
	if not title or not isinstance(title,str):
		return jsonify({"error": "Field 'title' is required and must be a string"}),400	

	# Optional fields with defaults
	description = data.get("description", "")

	# NOTE: bool("False") -> True because non-empty strings are truthy.
	# This line will treat string "False" as True. If you later change logic,
	# consider parsing booleans more carefully (e.g., using explicit check).
	completed = bool(data.get("completed", "False"))

	# Build todo object
	todo = {
		"id": new_id,
		"title":title,
		"description": description,
		"completed": completed,
		"created_at": datetime.now().isoformat()
	}	

	# Append to in-memory list and return created resource
	todos.append(todo)
	return jsonify(todo), 201


# -----------------------
# Route: Replace a todo (PUT)
# PUT /todos/<id>
# -----------------------
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def replace_todos(todo_id):
	"""
	Replace the todo (full update). Requires 'title' in the JSON body.
	Updates title/description/completed and sets updated_at timestamp.
	"""
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"error": "Todo not Found"}), 404

	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	title = data.get("title")
	if not title or not isinstance(title,str):
		return jsonify({"error": "Field 'title' is required and must be a string"}),400	

	# Replace fields (preserving id and created_at)
	todo["title"] = title
	todo["description"] = data.get("description", "")
	# Same caveat about bool("False") above applies here as well
	todo["completed"] = bool(data.get("completed", "False"))
	todo["updated_at"] = datetime.now().isoformat()

	return jsonify(todo), 200	


# -----------------------
# Route: Partial update (PATCH)
# PATCH /todos/<id>
# -----------------------
@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todos(todo_id):
	"""
	Partially update fields in the todo.
	Only provided fields are updated (title, description, completed).
	"""
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"error": "Todo not Found"}), 404

	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400

	# If the client provided a title, validate and update it.
	# NOTE: the code currently uses `title` name inside the isinstance check,
	# but `title` isn't assigned here; keep this in mind if you refactor later.
	if "title" in data:
		if not isinstance(title,str) or not data["title"]:
			return jsonify({"error": "Field 'title' is required and must be a string"}),400	
		todo["title"] = title
		
	# Update description if provided
	if "description" in data:
		todo["description"] = str(data["description"])		

	# Update completed flag if provided (same caveat about string booleans applies)
	if "completed" in data:
		todo["completed"] = bool(data["completed"])

	# Stamp updated time
	todo["updated_at"] = datetime.now().isoformat()	

	return jsonify(todo), 200	


# -----------------------
# Route: Delete a todo
# DELETE /todos/<id>
# -----------------------
@app.route("/todos/<int:todo_id>", methods = ["DELETE"])
def remove_todo(todo_id):
	"""
	Delete a todo by id.
	Returns 404 if not found, otherwise removes and returns a confirmation message.
	"""
	todo = find_todo(todo_id)
	if not todo:
		return jsonify({"Error":"Todo not Found"}), 404

	todos.remove(todo)
	return jsonify({"message": f"Todo {todo_id} deleted"}),200	


# -----------------------
# App entry point
# -----------------------
if __name__ == "__main__":
	# debug=True gives useful stack traces and auto-reload during development.
	app.run(debug=True)	
