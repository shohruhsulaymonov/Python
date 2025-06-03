#1
python -m venv my_env
my_env\Scripts\activate
pip install requests
pip install random
pip install matplotlib
#2
echo > math_operations.py
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
echo > string_utils.py

def reverse_string(x):
    return x[::-1]

def count_vowels(x):
    vowels = 'aouie'
    return sum(1 for i in x if i.lower() in vowels)
