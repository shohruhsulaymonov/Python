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
import requests

api_key = 'a8d09063596f0bf1cbb25838831af6b5'

city = 'Tashkent'


u = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


def get_weather_info(url):
    try:
        response = requests.get(url)
        weather_data = response.json()
        response.raise_for_status()
        return weather_data
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error {err}')
    except Exception as e:
        print(f'Error {e}')

def print_weather_info(data):
    print(f'City: {data['name']}\nWeather: {data['weather'][0]['main']}\nTemperature: {data['main']['temp']}°C\nHumidity: {data['main']['humidity']}%\nWindSpeed: {data['wind']['speed']} m/s')

print_weather_info(get_weather_info(u))
