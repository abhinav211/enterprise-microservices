from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":
        return jsonify({
            "status": "success",
            "token": "fake-jwt-token",
            "hostname": socket.gethostname()
        })

    return jsonify({
        "status": "failed"
    }), 401


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
