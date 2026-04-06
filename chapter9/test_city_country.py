from city_functions import city_country


def test_city_country():
    assert city_country('shanghai', 'china') == 'Shanghai,China'
    example = city_country('New York', 'America')
    assert example == 'New York,America'
    
    