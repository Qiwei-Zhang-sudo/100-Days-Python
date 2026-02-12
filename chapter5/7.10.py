Places = {}
while True:
    name = input('Please input your name:')
    place = input('If you coule visit one place in the world,where is it? ')
    Places[name] = place
    repeat = input('If you want to continue,enter "y",if not,enter "n":')
    if repeat == 'n':
        break
for name, place in Places.items():
    print(f'{name} favorite place is:{place}')    