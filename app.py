from flask import Flask, render_template
import time

app = Flask(__name__)

ESP32_URL = "http://192.168.1.100"  # change to ESP32 IP

@app.route("/")
def index():
    try:
        response = requests.get(ESP32_URL, timeout=1)
        distance = response.json()["distance"]
    except:
        distance = "ESP32 not connected"

    return render_template("index.html", distance=distance)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

ESP32_URL = "http://192.168.1.100"  # change to ESP32 IP

@app.route("/")
def index():
    try:
        response = requests.get(ESP32_URL, timeout=1)
        distance = response.json()["distance"]
    except:
        distance = "ESP32 not connected"

    return render_template("index.html", distance=distance)

if __name__ == "__main__":

 HEAD
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

ESP32_URL = "http://192.168.1.100"  # change to ESP32 IP

@app.route("/")
def index():
    try:
        response = requests.get(ESP32_URL, timeout=1)
        distance = response.json()["distance"]
    except:
        distance = "ESP32 not connected"

    return render_template("index.html", distance=distance)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

ESP32_URL = "http://192.168.1.100"  # change to ESP32 IP

@app.route("/")
def index():
    try:
        response = requests.get(ESP32_URL, timeout=1)
        distance = response.json()["distance"]
    except:
        distance = "ESP32 not connected"

    return render_template("index.html", distance=distance)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
