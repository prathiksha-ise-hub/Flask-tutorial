from flask import Flask
app = Flask(__name__)
@app.route("/students")
def users():
    return "This is student page"
@app.route("/students/<studentname>")
def useru(studentname):
    return f"Hello, {studentname}!"
@app.route("/students/<studentname>/<course>")
def student_course(studentname, course):
    return f"Student: {studentname}, Course: {course}"
if __name__ == '__main__':
    app.run(debug=True)