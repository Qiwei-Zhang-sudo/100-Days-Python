class Restaurant:
    """一个关于餐厅的类"""
    def __init__(self,restaurant_name,restaurant_type):
        """初始化餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe(self):
        print(f"名称：{self.restaurant_name}")
        print(f'类型：{self.restaurant_type}')

    def open(self):
        print('我们正在营业中')