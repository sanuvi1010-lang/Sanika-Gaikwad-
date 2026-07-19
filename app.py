from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "students.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)
    
    connection.commit()
    connection.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        course = data.get('course')
        city = data.get('city')

        if not all([name, age, course, city]):
            return jsonify({"message": "Please fill all fields"}), 400

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, course, city) VALUES (?, ?, ?, ?)",
            (name, age, course, city)
        )
        connection.commit()
        connection.close()
        return jsonify({"message": "Student Added Successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        connection.close()

        students_list = []
        for row in rows:
            students_list.append({
                "id": row["id"],
                "name": row["name"],
                "age": row["age"],
                "course": row["course"],
                "city": row["city"]
            })
        return jsonify(students_list), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    create_table()
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)