import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0411",
    database="student_course_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route('/add', methods=['POST'])
def add():
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    cursor.execute(
        "INSERT INTO students (full_name, email, phone, address) VALUES (%s, %s, %s, %s)",
        (full_name, email, phone, address)
    )
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    cursor.execute(
        "UPDATE students SET full_name = %s, email = %s, phone = %s, address = %s WHERE id = %s",
        (full_name, email, phone, address, id)
    )
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)