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
