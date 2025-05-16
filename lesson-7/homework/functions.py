#1
def is_prime(n):
    if n < 2:
        while True:
            n = int(input('Enter a natural number above 1: '))
            if n > 1:
                break
    
    divisors = 0
    for i in range(2, n):
        if n % i == 0:
            divisors += 1
    if divisors == 0:
        print(True)
    else:
        print(False)
is_prime(0)
#2
def digitsum(k) -> int:
    x = str(k)
    s = 0
    for i in x:
        s += int(i)
    return s
digitsum(502)

#3
def power(N):
    p = 1
    while 2**p <= N:
        print(2**p, end = ' ')
        p += 1
power(10)
