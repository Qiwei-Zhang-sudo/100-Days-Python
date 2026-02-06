river={
    'yellow_river':'Chain',
    'changjiang':'Chain',
    'henhe':['Chain','yindu','yuenan',],
    'yamaxun':'baxi'
}
for key,value in river.items():
    print(f'The {key} uns through {value}')
for key in river.keys():
    print(f'{key}')
for value in river.values():
    print(value)