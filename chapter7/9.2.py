class Restaurant:
    """ a simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, restaurant_type):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
    
    def describe_restaurant(self):
        """打印餐厅信息"""
        print(f"{self.restaurant_name}")
        print(f"{self.restaurant_type}")
    
    def open_restaurant(self):
        '''打印餐厅正在营业'''
        print(f'{self.restaurant_name}正在营业')

fish = Restaurant('fish','烤鱼店')
food = Restaurant('food','川菜')
cook = Restaurant('cook','西餐店')
fish.describe_restaurant()
food.describe_restaurant()
cook.describe_restaurant()
fish.open_restaurant()
food.open_restaurant()
cook.open_restaurant()

