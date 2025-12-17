from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

current_distance = 0.0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/update_distance", methods=["POST"])
def update_distance():
    global current_distance
    try:
        data = request.get_json()
        current_distance = float(data["distance"])
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/get_distance", methods=["GET"])
def get_distance():
    return jsonify({"distance": current_distance})
