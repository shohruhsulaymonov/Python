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
