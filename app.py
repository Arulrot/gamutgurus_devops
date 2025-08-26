from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok", "message": "App is healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
