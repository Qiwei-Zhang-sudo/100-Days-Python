shanghai = {
    'name': '上海',
    'population': 24250000,
    'country': '中国',
}
new_york = {
    'name': '纽约',
    'population': 8500000,
    'country': '美国',
}
tokyo = {
    'name': '东京',
    'population': 38500000,
    'country': '日本',
}
cities = {
    '上海': shanghai,
    '纽约': new_york,
    '东京': tokyo,
}
for city,city_info  in cities.items():
    print(f'{city}_info:')
    for key,value in city_info.items():
        print(f"{key}:{value}")
    print('-'*10)