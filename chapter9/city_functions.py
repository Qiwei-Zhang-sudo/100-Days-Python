def city_country(city, country):
    city_country = city + ',' + country
    return city_country.title()

if __name__ == '__main__':
   example = city_country('shanghai','china')
   print(example)