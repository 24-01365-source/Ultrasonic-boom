from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

latest_distance = 0

@app.route("/")
def index():
    return render_template("index.html", distance=latest_distance)

@app.route("/update", methods=["POST"])
def update():
    global latest_distance
    data = request.get_json()
    latest_distance = data.get("distance", 0)
    return jsonify({"status": "ok"})
