from flask import Flask, jsonify, render_template
from flask_cors import CORS
import Fusion_Engine

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/realtime", methods=["POST"])
def realtime_scan():
    try:
        results = Fusion_Engine.scan_non_camera()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/infrared", methods=["POST"])
def infrared_scan():
    try:
        results = Fusion_Engine.scan_infrared()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/optical", methods=["POST"])
def optical_scan():
    try:
        results = Fusion_Engine.scan_optical()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8800, debug=True)

