
from flask import Flask, jsonify, request
import student_mang
from db import create_tables

app = Flask(__name__)
@app.route('/students', methods=["GET"])
def get_student():
    student = student_mang.get_student()
    return jsonify(student)


@app.route("/student", methods=["POST"])
def insert_student():
    student_details = request.get_json()
    name = student_details["name"]
    roll = student_details["roll"]
    score = student_details["score"]
    result = student_mang.insert_student(name, roll, score)
    return jsonify(result)


@app.route("/student", methods=["PUT"])
def update_student():
    student_details = request.get_json()
    id = student_details["id"]
    name = student_details["name"]
    roll = student_details["roll"]
    score = student_details["score"]
    result = student_mang.update_student(id, name, roll, score)
    return jsonify(result)


@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    result = student_mang.delete_student(id)
    return jsonify(result)


@app.route("/students/<id>", methods=["GET"])
def get_student_by_id(id):
    student = student_mang.get_by_id(id)
    return jsonify(student)

if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=True)