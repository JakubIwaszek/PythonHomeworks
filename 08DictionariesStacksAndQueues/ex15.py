import json

def writeStudentData():
    student = {
        "name": "John",
        "surname": "Bloom",
        "age": 23,
        "studentId": "321234",
        "studentCardActive": True,
        "subjects": ["math", "english", "chemistry"]
    }
    with open("student.txt", "w") as jsonFile:
        json.dump(student, jsonFile, indent = 4)
        
writeStudentData()