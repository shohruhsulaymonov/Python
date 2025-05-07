# 1. Age Calculator
Name = input('Enter your name: ')
birthyear = int(input('Enter your year of birth: '))
print(f'{Name}, you are {2025 - birthyear} years old')

#2. Extract Car Names
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])

#3. Extract Car Names
txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[-1::-2])

#4. Extract Residence Area
txt = "I'am John. I am from London"
print(txt[-6:])

#5. Reverse String
Usertxt = input('Enter a text: ')
print(Usertxt[::-1])

#6. Count Vowels
string = 'Interstellar'
vowels = 'aoieuAOIEUE'
vowelcnt = sum(1 for i in string if i in vowels)
print (vowelcnt)

#7. Find Maximum Value
numbers = [1, 3, 4, 2, 8, 3, 0, 98]
print(max(numbers))

#8. Check Palindrome
Word = input('Enter a word: ')
if Word == Word[::-1]:
    print('Yes')
else:
    print('No')

#9. Extract Email Domain
email = input('Enter your email ')
atpos = email.find('@') + 1
print(email[atpos:])

#10. Generate Random Password
import random
import string

length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)
