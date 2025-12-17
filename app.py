from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
DB_FILE = "distance.json"

# Ensure the JSON file exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"distance": 0}, f)

@app.route("/")
def index():
    # Read the latest distance from JSON
    with open(DB_FILE) as f:
        data = json.load(f)
    distance = data.get("distance", 0)
    return render_template("index.html", distance=distance)

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    distance = data.get("distance", 0)
    # Save distance to JSON file
    with open(DB_FILE, "w") as f:
        json.dump({"distance": distance}, f)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
