class Employee:
    """这是一个企业员工的类"""

    def __init__(self,firstname,lastname,wage):
        """初始化员工的属性"""
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage

    def increase_wage(self,number=5000):
        """默认为员工增加工资5000"""
        self.wage += number


        