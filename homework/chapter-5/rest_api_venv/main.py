from fastapi import FastAPI, responses
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    group: str

class StudentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.post("/student/add")
def save_student(student: Student):
    students = []
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            students = list(data)
    except:
        students = []

    with open("data.json", "w+", encoding="utf-8") as file:
        students.append(student)
        json.dump(students, file, cls=StudentJsonEncoder)
    return "saved"

@app.get("/student/{student_id}", response_class=HTMLResponse)
def get_student_by_id(student_id:int):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        return "No students at all :("

    for student in data:
        if student['id'] == student_id:
            return str(student['id']) + ": " + student['name'] + ", " + student['group']

    return "No such student :("

@app.get("/student/all/", response_class=HTMLResponse)
def get_all_students():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        return "No students at all :("

    resultString = ""

    for student in data:
        resultString += str(student['id']) + ": " + student['name'] + ", " + student['group'] + "<br>"
    return resultString

@app.get("/")
def greet_newcomer():
    return {"Greetings" : "Newcomer"}

# import uvicorn
# uvicorn.run("main:app", port=8000, reload=True)