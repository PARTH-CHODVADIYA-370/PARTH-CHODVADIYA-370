from db import get_db


def insert_student(name, roll, score):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO student(name, roll, score) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, roll, score])
    db.commit()
    return True


def update_student(id, name, roll, score):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE student SET name = ?, roll = ?, score = ? WHERE id = ?"
    cursor.execute(statement, [name, roll, score, id])
    db.commit()
    return True


def delete_student(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM student WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, roll, score FROM student WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_student():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, roll, score FROM student"
    cursor.execute(query)
    return cursor.fetchall()