my_pizzas=[item for item in range(10,20,2)]
friend_pizzas=my_pizzas[:]
my_pizzas.append(100)
friend_pizzas.insert(0,100)
for item in my_pizzas:
    print(item)
print("-"*50)
for item in friend_pizzas:
    print(item)
