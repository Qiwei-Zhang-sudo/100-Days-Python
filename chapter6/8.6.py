def city_country(city,country = 'China'):
    ''' 返回城市国家 '''
    return f'{city},{country}'

city = city_country('shanghai')
print(city)
country = city_country('New York',country = 'America')
print(country)
citys = city_country('tok',country = 'Japapn')
print(citys)