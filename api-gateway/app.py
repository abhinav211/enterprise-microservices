from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AUTH_SERVICE = "http://auth-service"
EMPLOYEE_SERVICE = "http://employee-service"

@app.route('/auth/login', methods=['POST'])
def login():
    try:
        response = requests.post(
            f"{AUTH_SERVICE}/login",
            json=request.json,
            timeout=5
        )

        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Auth service unavailable",
            "details": str(e)
        }), 503


@app.route('/employees', methods=['GET'])
def employees():
    try:
        response = requests.get(
            f"{EMPLOYEE_SERVICE}/",
            timeout=5
        )

        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Employee service unavailable",
            "details": str(e)
        }), 503


@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
