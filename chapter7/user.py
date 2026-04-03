class User:
    """用户信息"""
    def __init__(self,first_name,last_name,age,sex):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        """打印用户信息"""
        print(f"username: {self.first_name} {self.last_name}")
        print(f'age: {self.age}')
        print(f'sex: {self.sex}')

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f'hello,{self.first_name} {self.last_name}')


class Privileges:
    """一个模拟权限的类"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        """初始化子类属性"""
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()

    def show_privileges(self):
        """显示管理员权限"""
        self.privileges.show_privileges()