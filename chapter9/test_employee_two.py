import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee('Magnus','Grant',1000)

def test_give_default_raise(employee):
    employee.increase_wage()
    assert employee.wage == 6000

def test_give_custom_raise(employee):
    employee.increase_wage(9000)
    assert employee.wage == 10000
    