languages={
    'admin':'python',
    'john':'c',
    'alice':'java',
    'jack':'c++'
}
names=[
    'admin',
    'john',
    'alice',
    'jack',
    'tom'
]
for name in names:
    symbol=0
    for key in languages.keys():
        if name == key:
            symbol=1
            break
    if symbol:
        print(f'{name} is a good person ')
    else:
        print(f'{name} is a bad person')