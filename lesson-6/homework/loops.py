#1. Modify String with Underscores


#2. Integer Squares Exercise
while True:
    n = int(input('Input a number: '))
    if 1 <= n <= 20:
        break
    else:
        print('Input a number between 1 and 20')
for i in range(n):
    print(i**2)
#3 Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1
#Exercise 2: Print the following pattern
for i in range(1, 6):
    
    for j in range(1, 6):
        print(j, end = ' ')

    print(end ='\n')
#Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input('Enter a number: '))
s = 0
for i in range(1, n+1):
    s += i
print(f'Sum is: {s}')
#Exercise 4: Print multiplication table of a given number
n = int(input('Enter a number: '))
for i in range(1, 11):
    print(n*i)
#Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    print(x)
#Exercise 6: Count the total number of digits in a number
numbers = 75869
num = str(numbers)
counter = 0
for i in num:
    counter += 1
print(counter)
#Exercise 7: Print reverse number pattern
