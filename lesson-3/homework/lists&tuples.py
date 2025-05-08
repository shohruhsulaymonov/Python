#1. Create and Access List Elements
list = ['Apple', 'Orange', "Pineapple", 'Banana', 'Pomegranate']
print(list[2])
#2. Concatenate Two Lists
list1 = ['Potato', 'Cucumber', 'Corn', 'Tomato']
list2 = ['Apple', 'Orange', "Pineapple", 'Banana', 'Pomegranate']
concatlists = list1 + list2
#3. Extract Elements from a List
elements = ['Interstellar', 'Lalaland', 'Corn', 'Tomato', 'Banana']
first = elements[0]
middle = elements[2]
last = elements[-1]
newlist = [first, middle, last]
print(newlist)
#4. Convert List to Tuple
movies = ['Interstellar', 'Lalaland', 'Inception', 'Groundhog Day', '8 Mile']
tpmovies = tuple(movies)
print(tpmovies[1])
#5. Check Element in a List
lst = ['London', 'New York', 'Washington D.C.', 'Tashkent', 'Paris']
print('Paris' in lst)
#6. Duplicate a List Without Using Loops
lst = [1, 4, 2, 7, 2, 6, 8, 2, 0, 2, 1, 0]
print(lst * 2)
#7. Swap First and Last Elements of a List
elements = ['Interstellar', 'Lalaland', 'Corn', 'Tomato', 'Banana']
elements[0], elements[-1] = elements[-1], elements[0]
print(elements)
#8. Slice a Tuple
num = list(range(1, 11))
print(num[3:7])
#9. Count Occurrences in a List
colors = ['Blue', 'Red', 'Yellow', 'Blue', 'Green', 'Blue']
print(colors.count('Blue'))
#10. Find the Index of an Element in a Tuple
animals = ('lion', 'Hawk', 'Cat', 'Bear', 'Wolf', 'Slime')
print(animals.index('lion'))
#11. Merge Two Tuples
colors = ('Blue', 'Red', 'Yellow', 'Blue', 'Green', 'Blue')
animals = ('lion', 'Hawk', 'Cat', 'Bear', 'Wolf', 'Slime')
anicolors = colors + animals
print(anicolors)
#12. Find the Length of a List and Tuple
colors = ['Blue', 'Red', 'Yellow', 'Blue', 'Green', 'Blue']
animals = ('lion', 'Hawk', 'Cat', 'Bear', 'Wolf', 'Slime')
print(len(colors))
print(len(animals))
#13. Convert Tuple to List
numbers = (12, 3, 9, 98 ,93)
numbers = list(numbers)
print(numbers)
#14. Find Maximum and Minimum in a Tuple
numbers = (12, 3, 9, -98 ,93)
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')
#15. Reverse a Tuple
colors = ('Blue', 'Red', 'Yellow', 'Blue', 'Green', 'Blue')
print(colors[::-1])
