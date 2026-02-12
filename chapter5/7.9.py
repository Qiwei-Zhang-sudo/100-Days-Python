'''
如果只是简单的遍历列表，可以用for循环，
如果需要动态的修改列表，用while循环更适合，
1 index < len(list)
2 value in list
3 while list 列表为空时，条件为假，结束循环

'''
sandwich_orders = [
    'pastrami',
    'chicken',
    'beef',
    'pastrami',
    'fish',
    'pastrami',
]
finished_sandwiches = []
print("Pastrami is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
index = 0
while index < len(sandwich_orders):
    print(f'I made your {sandwich_orders[index]}')
    # current_sandwich = sandwich_orders.pop(index)
    # del sandwich_orders[index]
    finished_sandwiches.append(sandwich_orders.pop(index))
# pop方法可以根据索引删除列表中的元素，并返回改元素，若没有索引，则默认删除列表最后一个元素
for sandwich in finished_sandwiches:
    print(sandwich)
