# #student enroll management system using python

# students={} # dictionry to store student recored 
# student_ids=[] # List to keep track of student IDs

# while True:
#     print("\n1. Add Student Recored \n2.View All Students \n3.Search Student \n4.Upadate Student Information \n5. Delete Student REcored \n6. Exit ")
#     choice = input("Enter your choice : ")

#     if  choice == "1": #add student Recored 
#         student_id = input("Enter student ID: ")
#         name  = input("enter Student name: ") 
#         age = input("Enter Student aage : ")
#         grade = input("Enter Student Grade : ")
#         students[student_id] = {'name': name, 'age': age, 'grade':grade}
#         student_ids.append(student_id)
#         print("Student added ssuccessfully !!")
    
#     elif choice   == '2':#View all Student 
#         if not students:
#             print("No Student found.")
#         else:
#             for student_id in student_ids:
#                 student = students[student_id]
#                 print(f'ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grade : {student['grade']}')
#     elif choice == '3':
#         student_id = input("Enter student id to search")
#         if student_id in students:
#             student = students[student_id]
#             print(f"ID : {student_id}, Name: {student['name']}, age : {student['age']}, grade : {student['grade']}")
#         else:
#             print("student not found. ")


#     elif choice == '4': 
#         student_id = input("Enter a student ID to uodate: ")
#         if student_id in students:
#             name = input("Enter new name: ")
#             age = input("Enter new age : ")
#             grade = input("Enter new grade: ")
#             students[student_id]={'name': name, 'age':age, 'grade': grade }
#             print("student information updated successfully !!")
#         else:
#             print("student not found")
    
#     elif choice =='5':
#         student_id = input("Enter student ID to Delete : ")
#         if student_id in students:
#             del students[student_id]
#             student_ids.remove(student_id)
#             print("Student recored deleted successfully !!")
#         else:
#             print("student not found")
    
#     elif choice == '6':
#         print("Exiting....")
#         break
#     else:
#         print("Invalid choice. please try again")

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # Initialize data structures
# students = {}  # Dictionary to store student records
# student_ids = []  # List to keep track of student IDs

# @app.route('/')
# def home():
#     return render_template('index.html', students=students)

# @app.route('/add', methods=['POST'])
# def add_student():
#     student_id = request.form['student_id']
#     name = request.form['name']
#     age = request.form['age']
#     grade = request.form['grade']

#     students[student_id] = {'name': name, 'age': age, 'grade': grade}
#     student_ids.append(student_id)
    
#     return redirect(url_for('home'))

# @app.route('/search', methods=['POST'])
# def search_student():
#     student_id = request.form['student_id']
#     student = students.get(student_id)
#     return render_template('index.html', students=students, search_result=student)

# @app.route('/update', methods=['POST'])
# def update_student():
#     student_id = request.form['student_id']
#     if student_id in students:
#         students[student_id] = {
#             'name': request.form['name'],
#             'age': request.form['age'],
#             'grade': request.form['grade']
#         }
#     return redirect(url_for('home'))

# @app.route('/delete/<student_id>')
# def delete_student(student_id):
#     if student_id in students:
#         del students[student_id]
#         student_ids.remove(student_id)
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated database (in-memory dictionary)
students = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.json
    student_id = data.get("id")
    name = data.get("name")
    age = data.get("age")
    grade = data.get("grade")

    if student_id and name and age and grade:
        students[student_id] = {"name": name, "age": age, "grade": grade}
        return jsonify({"message": "✅ Student Added Successfully!"}), 200
    return jsonify({"message": "⚠️ Please fill all fields!"}), 400

@app.route("/search_student/<student_id>", methods=["GET"])
def search_student(student_id):
    if student_id in students:
        return jsonify(students[student_id]), 200
    return jsonify({"message": "⚠️ Student Not Found!"}), 404

@app.route("/update_student", methods=["PUT"])
def update_student():
    data = request.json
    student_id = data.get("id")
    if student_id in students:
        students[student_id] = {
            "name": data.get("name"),
            "age": data.get("age"),
            "grade": data.get("grade"),
        }
        return jsonify({"message": "✅ Student Updated Successfully!"}), 200
    return jsonify({"message": "⚠️ Student Not Found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
