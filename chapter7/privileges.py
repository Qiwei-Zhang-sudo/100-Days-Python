from user0 import User


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