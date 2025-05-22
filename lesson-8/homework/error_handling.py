#1
try:
    1/0
except ZeroDivisionError:
    print("You can't divide by zero idiot")
#2
try:
    n = int(input('Please, enter an integer: '))

except ValueError:
    print('Only integers are allowed')

#3
try:
    f = open("D:\\Project\\categories.txt", 'r')
except FileNotFoundError:
    print('The file does not exist')
#4
a = input('Enter the first number: ')
b = input('Enter the second number: ')

if isinstance(a, int) and isinstance(b, int) :
    pass
else:
    print('Values must be numbers!')
#5
try:
    f = open("D:\\Project\\categories.txt", 'r')
except PermissionError:
    print("You don't have the necessary right to access this file")
#6
try:
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst[30])
except IndexError:
    print('The index is out of range')
#7
try:
    val = int(("Type a number: ")) # the user presses Ctrl + C
except KeyboardInterrupt:
    print('\nThe user has cancelled the input')
#8
def division(a, b):
    try:
        c = a / b
        print(f'The result of dividing {a} by {b} is: {c}')
    except ArithmeticError:
        print('An arithmetic error occured')
division(3, 0)
#9
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except UnicodeDecodeError as e:
        print(f'Unicode decoding error: {e}')
    except FileNotFoundError:
        print("The file you're looking for isn't found. Please assure that the file is in the correct path")
    except Exception as e:
        print(f'An unexpected error occured: {e}')
file_path = 'D:\\Project\\categories.csv'
read_file(file_path)

#10
#11
#12
#13
