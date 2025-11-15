from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/users", methods=["POST"])
def create_user():
	data = request.get_json(silent=True)
	if not data:
		return jsonify({"Error":"Missing JSON Body"}), 400
	name = data.get("name")
	email = data.get("email")
	return jsonify({
		"Message": "User received",
		"User": {"name": name, "email": email}
		}), 201

if __name__ == "__main__":
	app.run()