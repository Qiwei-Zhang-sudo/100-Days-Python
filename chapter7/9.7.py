class User:
    """用户信息"""
    def __init__(self,first_name,last_name,age,sex):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describle_user(self):
        """打印用户信息"""
        print(f"username: {self.first_name} {self.last_name}")
        print(f'age: {self.age}')
        print(f'sex: {self.sex}')
    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f'hello,{self.first_name} {self.last_name}')
class Admin(User):
    """admin"""
    def __init__(self, first_name, last_name, age, sex,*privileges):
        super().__init__(first_name, last_name, age, sex)     
        self.privileges = list(privileges[:])
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

example = Admin('admin','admin',18,'male','can add post','can delete post','can ban user')
example.show_privileges()
example.describle_user()
