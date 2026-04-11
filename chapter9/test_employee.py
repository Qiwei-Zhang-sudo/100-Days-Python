from employee import Employee


def test_employee():
    example = Employee('Magnus','Grant',5000)
    example.increase_wage()
    assert example.wage == 10000

def test_employee_two():
    emp = Employee('Magnus','Grant',1000)
    emp.increase_wage(9000)
    assert emp.firstname == 'Magnus'
    assert emp.lastname == 'Grant'
    assert emp.wage == 10000
