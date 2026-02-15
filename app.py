from flask import Flask
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>🚀 DevOps CI/CD Pipeline Project</h1>
    <hr>
    <p><strong>Status:</strong> Application Running Successfully ✅</p>
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>Timestamp:</strong> {current_time}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
