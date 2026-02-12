sandwich_orders = [
    'chicken',
    'beef',
    'fish',
]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich)
    finished_sandwiches.append(current_sandwich)
# 当列表为空时，条件为假，结束循环
print('I made all the sandwiches')
for sandwich in finished_sandwiches:
    print(sandwich)    