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
