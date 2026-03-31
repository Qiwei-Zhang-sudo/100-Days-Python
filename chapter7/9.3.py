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

user1 = User('magnus','grant','20','male')
user2 = User('zhangsan','lisi','19','male')
user3 = User('wangwu','zhaoliu','18','female')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()




