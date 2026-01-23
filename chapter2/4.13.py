foods=('vegetables','grain','fruits','noodles')
numbers=[item for item in range(1,10,2)]
new_numbers=tuple(numbers)
print(type(foods))
print(type(new_numbers))
for item in foods:
    print(item)
for item in numbers:
    print(item)
print("-"*50)

try:
    foods.append('water')
except AttributeError:
    print('AttributeError')
else:
    print("This is not TypeError")

new_numbers=(item for item in range(10,20,2))
for item in new_numbers:
    print(item)



