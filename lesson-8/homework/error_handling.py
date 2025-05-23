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
def call_method(lst):
    try:
        lst.add()
        print(lst)
    except AttributeError:
        print('No such attribute exists')
my_list = [23, 53, 42, 2, 5]
call_method(my_list)
#11
contents = open('D:\\Project\\categories.txt', 'r')
print(contents)
#12
def read_line(n):
    with open('D:\\Project\\categories.txt', 'r') as file:
        contents = file.readlines()

    return contents[:n]
print(*read_line(2))
#13
def read_lines():
    with open("D:\\Project\\categories.txt", 'a') as file:
        file.write('\n8,Starbucks')

        file = open("D:\\Project\\categories.txt", 'r')
        contents = file.read()
        
    print(contents)
    
read_lines()
#14
def read_lines(n):
    try:
        with open("D:\\Project\\categories.txt", 'r') as file:
            contents = file.readlines()
            
        return contents[-n:]
    except FileNotFoundError as e:
        print("File doesn't exist in the given path")
        return []
    except Exception as e:
         print(f"An error occurred: {e}")
         return []
print(*read_lines(5))
#15
def read_lines():
    try:
        with open("D:\\Project\\categories.txt", 'r') as file:
            contents = file.readlines()
            
        return contents
    except FileNotFoundError as e:
        print("File doesn't exist in the given path")
    
print(read_lines())
#16
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = file.readlines()
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#17
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = tuple(file.readlines())
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#18
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = list(file.readlines())
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#19
def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        words = [word.strip(".,!?;:'\"()[]{}") for word in words]

        max_length = 0
        longest_text = list()

        for text in words:
            if len(text) > max_length:
                max_length = len(text)
                longest_text = [text]

            elif len(text) == max_length:
                if text not in longest_text:
                    longest_text.append(text)

        return longest_text, max_length
    except FileNotFoundError:
        print(f'The file "{filename}" not found')
    except Exception as e:
        print(f'An error occured. {e}')

longest, len = find_longest_words('D:\\Project\\categories.txt')
print(f'Longest word(s) of {len}: ')
for i in longest:
    print(i)
#20

#21
#22
#23
#24
#25
#26
