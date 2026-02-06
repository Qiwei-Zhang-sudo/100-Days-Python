numbers={
    'admin':716088,
    'john':123456,
    'alice':888888,
    'jack':666666,
    'tom':999999,
}
for name in numbers.keys():
    number = []
    for item in range(2):
        item = int(input('Please input your number: '))
        number.append(item)
    numbers[name] = number
for name,number in numbers.items():
    print(f'{name}最喜欢的数字是：{number}')   