cat = {
    'host': 'alice',
    'name': 'cat',
    'age': 2,
}
dog = {
    'host': 'bob',
    'name': 'dog',
    'age': 3,
}
pig = {
    'host': 'admin',
    'name': 'pig',
    'age': 4,
}
pets = [cat,dog,pig]
for pet in pets:
    print(f'{pet['name']} is a {pet['age']} years old pet owned by {pet['host']}')
