from flask import Flask, render_template
import requests

app = Flask(__name__)

ESP32_URL = "http://192.168.1.100"  # ESP32 local IP


@app.route("/")
def index():
    try:
        response = requests.get(ESP32_URL, timeout=1)
        distance = response.json().get("distance", "No data")
    except Exception:
        distance = "ESP32 not connected"

    return render_template("index.html", distance=distance)
