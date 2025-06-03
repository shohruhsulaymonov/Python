#1
python -m venv my_env # venv created
my_env\Scripts\activate # venv activated

pip install requests
pip install random
pip install matplotlib
#installing the libraries
#2
echo > math_operations.py # creating th module
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    try:
        a/b
    except ZeroDivisionError:
        return "Can't divide by zero!"
#----------------------
echo > string_utils.py #creating the module

def reverse_string(x):
    return x[::-1]

def count_vowels(x):
    vowels = 'aouie'
    return sum(1 for i in x if i.lower() in vowels)

#3 package and modules are created.
from math import pi
def calc_area(radius):
    return round(pi*radius**2, 2)

def calc_circumference(radius):
    return round(2*pi*radius, 2)

#Package and modulares are created
#file_reader:
def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    print(contents)
#file_writer:
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
