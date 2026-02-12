pizza_active = True
while pizza_active:
    pizzas = input('Please add a pizza:')
    if pizzas == 'quit':
        pizza_active = False
    else:
        print(f'I will add {pizzas} to your pizzas')
