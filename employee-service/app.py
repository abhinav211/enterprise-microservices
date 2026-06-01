from flask import Flask, jsonify
import psycopg2
import os
import socket

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "employees")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password123")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/')
def home():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees;")
    rows = cur.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "role": row[2]
        })

    cur.close()
    conn.close()

    return jsonify({
        "service": "employee-service-v8",
        "hostname": socket.gethostname(),
        "employees": employees
    })

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
