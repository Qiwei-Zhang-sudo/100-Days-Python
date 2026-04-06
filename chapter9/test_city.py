from city import city


def test_city():
    example = city('shanghai', 'china', '100000000')
    assert example == 'Shanghai,China_Population 100000000'
    
def test_city_country():
    example = city('shanghai', 'china', '100000000')
    assert example == 'Shanghai,China_Population 100000000'
