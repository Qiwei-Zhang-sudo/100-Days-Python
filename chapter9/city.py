def city(city, country, population):
    example = city + ',' + country + "_" +  'population' +' ' + population
    return example.title()

if __name__ == '__main__':
    example = city('shanghai', 'china', '100000000')
    print(example)