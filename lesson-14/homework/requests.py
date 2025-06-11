#1
import json

students = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "age": 20,
        "grade": "Sophomore",
        "subjects": ["Math", "Physics", "Computer Science"]
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "age": 22,
        "grade": "Senior",
        "subjects": ["History", "English Literature", "Philosophy"]
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "age": 19,
        "grade": "Freshman",
        "subjects": ["Biology", "Chemistry", "Statistics"]
    },
    {
        "id": 4,
        "name": "Diana Prince",
        "age": 21,
        "grade": "Junior",
        "subjects": ["Political Science", "Economics", "Sociology"]
    },
    {
        "id": 5,
        "name": "Ethan Hunt",
        "age": 23,
        "grade": "Senior",
        "subjects": ["Engineering", "Mathematics", "Physics"]
    }
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)


with open('students.json') as file:
    student = json.load(file)
    for i in student:
        print('\n============')
        for j in i:
            print(f'{j}: {i[j]}')
#2
