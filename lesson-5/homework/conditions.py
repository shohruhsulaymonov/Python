#1.  Determine whether a given year is a leap year.
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(True)
    else:
        print(False)
is_leap(2025)
#2. Conditional Statements Exercise
n = int(input())
if (n % 2 != 0) or (n % 2 == 0 and n in range(6, 21)):
    print('Weird')
else:
    print('Not weird')
#2. Conditional Statements Exercise
n = int(input('Input an integer bewtween 1 and 100: '))
while not 1 <= n <= 100:
    n = int(input('Input an integer bewtween 1 and 100: '))
if (n % 2 != 0) or (n % 2 == 0 and 6 <= n <= 20):
    print('Weird')
else:
    print('Not weird')
#3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#Solution 1 with if-else statement.
a = int(input('Enter a starting position: '))
b = int(input('Enter an ending position: '))
numbers = list(range(a, b + 1))
if a % 2 == 0:
    numbers = list(range(a, b + 1, 2))
else:
    numbers = list(range(a + 1 , b + 1, 2))
print(numbers)
#Solution 2 without if-else statement.
a = int(input('Enter a starting position: '))
b = int(input('Enter an ending position: '))
numbers = list(range(a, b + 1))
print([x for x in numbers if x % 2 == 0])
