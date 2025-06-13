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

#3
import json


def load_books(filename="Books.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"{filename} is corrupted or not valid JSON.")
    except Exception as e:
        print(f"Unexpected error loading file: {e}")
    return



def add_book(title: str , author: str, year: int, country: str, genre: str) -> None:
  books_list = load_books()

  new_book = {"title": title,
              "author": author,
              "year_published": year,
              "country": country,
              "genre": genre
              }

  if new_book not in books_list["books"]:
    books_list["books"].append(new_book)

    with open("Books.json", "w") as f:
      json.dump(books_list, f, indent=2)

    print("The book was successfully added to the file!")

  else:
    print("The book already exists in the file!")




def remove_book(title: str) -> None:

  books_list = load_books()
        

  for book in books_list["books"]:
    if book["title"].lower() == title.strip().lower():
      books_list["books"].remove(book)

      with open("Books.json", "w") as f:
        json.dump(books_list, f, indent=2)

      print("The book was succeessfully removed from the file")
      break

  else:
    print(f"There's no such book '{title}'")




def update_book(title: str,  target:str, new_info) -> None:

  books_list = load_books()

  for book in books_list["books"]:
    if book["title"].lower() == title.strip().lower():
      if target in ("title", "author", "year_published", "country", "genre"):
        book.update({f"{target}": new_info })
        print(f"The {target} of the book {title} was changed to {new_info}")
        break
      else:
        print(f"{target} is not a valid info about the book")
        break
  else:
    print(f"There's no such book {"title"}")

  with open("Books.json", "w") as f:
    json.dump(books_list, f, indent=2)

#4
# lists of titles movies of a particular genre to fetch a movie based on the genre the user inputs
genres = {
    "Action": [
        "Mad Max: Fury Road",
        "John Wick",
        "Die Hard",
        "Gladiator",
        "The Dark Knight"
    ],
    "Comedy": [
        "Superbad",
        "The Hangover",
        "Step Brothers",
        "Monty Python and the Holy Grail",
        "Groundhog Day"
    ],
    "Drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "The Godfather",
        "Fight Club",
        "12 Angry Men"
    ],
    "Science Fiction": [
        "Interstellar",
        "Inception",
        "Blade Runner 2049",
        "The Matrix",
        "Arrival"
    ],
    "Horror": [
        "The Conjuring",
        "Get Out",
        "Hereditary",
        "A Nightmare on Elm Street",
        "The Exorcist"
    ],
    "Romance": [
        "The Notebook",
        "Titanic",
        "Pride & Prejudice",
        "La La Land",
        "Before Sunrise"
    ],
    "Fantasy": [
        "The Lord of the Rings: The Fellowship of the Ring",
        "Harry Potter and the Sorcerer's Stone",
        "The Chronicles of Narnia",
        "Pan's Labyrinth",
        "Stardust"
    ]
}

#Actual code
import random
import requests


def movie_recommendation(genre):

    key = '42cc9218' #API key from the website
    movie = random.sample(genres[genre], 1) # retrieves a random movie name based on the genre
    url = f'http://www.omdbapi.com/?t={movie}&apikey={key}' #url of the website
    
    try:
        response = requests.get(url) # the response of the website
    except requests.exceptions.HTTPError:
        print("HHTPError occured")
    #Handling potential error

    dct_response = response.json() #Converting the .json format to dict object to work with data

    return f"Title: {dct_response['Title']}\nActors: {dct_response['Actors']}\nDirector: {dct_response['Director']}\nGenre: {dct_response['Genre']}\nRatings: {dct_response['Ratings'][0]['Value']}" # returns the main info about the movie
