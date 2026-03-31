class User:
    """用户信息"""
    def __init__(self,first_name,last_name,age,sex,login_attempts=0):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts
    def describe_user(self):
        """打印用户信息"""
        print(f"username: {self.first_name} {self.last_name}")
        print(f'age: {self.age}')
        print(f'sex: {self.sex}')
    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f'hello,{self.first_name} {self.last_name}')
    def increment_login_attempts(self):
        """登录次数加一"""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """充值登录次数"""
        self.login_attempts = 0
example = User('magnus','grant','20','male')
example.increment_login_attempts()
example.increment_login_attempts()
example.increment_login_attempts()
example.increment_login_attempts()
example.increment_login_attempts()
example.increment_login_attempts()
print(example.login_attempts)
example.reset_login_attempts()
print(example.login_attempts)