#1
import json
with open('students.json') as file:
    student = json.load(file)
    for i in student:
        print('\n============')
        for j in i:
            print(f'{j}: {i[j]}')
