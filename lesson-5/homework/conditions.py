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

#Solution 2 without if-else statement.
