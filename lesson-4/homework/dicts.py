#Sort a Dictionary by Value
dict = {
    'Uzbekistan': 'Tashkent',
    'USA': 'Washington D.C.',
    'England': 'London',
    'Japan': 'Tokyo',
    'China': 'Beijing'
}
capitals = dict.items()
vals = sorted(list(dict.values()))
print(vals)
#2. Add a Key to a Dictionary
dict = {0: 10, 1: 20}
dict[2] = 30
print(dict)
#3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#4. Generate a Dictionary with Squares
n = int(input('Enter a number: '))
i = 1
dic = {}
while i <= n:
    dic[i] = i*i
    i += 1
print(dic)
#5. Dictionary of Squares (1 to 15)
n = 15
i = 1
dic = {}
while i <= n:
    dic[i] = i*i
    i += 1
print(dic)
#1. Create a Set
st = {1, 4, 3, 15, 80, 3, 38, 2, 6, 8, 32, 5, 35}
print(st)
#2. Iterate Over a Set
st = {1, 4, 3, 15, 80, 3, 38, 2, 6, 8, 32, 5, 35}
for x in st:
    print(x)
#Add Member(s) to a Set
st = {1, 4, 3, 15, 80, 3, 38, 2, 6, 8, 32, 5, 35}
st.update([100, 0, 123,50])
print(st)
#4. Remove Item(s) from a Set
st = {1, 4, 3, 15, 80, 3, 38, 2, 6, 8, 32, 5, 35}
st.remove(999)
print(st)
#5. Remove an Item if Present in the Set
st.discard(100)
print(st)
