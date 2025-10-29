from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import Fusion_Engine
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# ------------------------------
# ✅ Home route
# ------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# ------------------------------
# ✅ Real-time scan route
# ------------------------------
@app.route("/realtime", methods=["POST"])
def realtime_scan():
    try:
        results = Fusion_Engine.scan_non_camera()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        print("Error in /realtime:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------------------
# ✅ Infrared scan route
# ------------------------------
@app.route("/infrared", methods=["POST"])
def infrared_scan():
    try:
        results = Fusion_Engine.scan_infrared()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        print("Error in /infrared:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------------------
# ✅ Optical scan route
# ------------------------------
@app.route("/optical", methods=["POST"])
def optical_scan():
    try:
        results = Fusion_Engine.scan_optical()
        return jsonify({"status": "success", "detected": results})
    except Exception as e:
        print("Error in /optical:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------------------
# ✅ Health check (optional)
# ------------------------------
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# ------------------------------
# ✅ Run server
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

