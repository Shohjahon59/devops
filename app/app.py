from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Agriculture Management System - Shohjahon Rashidov"

@app.route('/health')
def health():
    return jsonify({"status": "active", "user": "rashidov2005"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
