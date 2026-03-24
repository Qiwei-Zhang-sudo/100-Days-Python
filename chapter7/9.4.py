class Restaurant:
    """ a simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, restaurant_type,number_served=0):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = number_served
    def describe_restaurant(self):
        """打印餐厅信息"""
        print(f"{self.restaurant_name}")
        print(f"{self.restaurant_type}")
    def open_restaurant(self):
        '''打印餐厅正在营业'''
        print(f'{self.restaurant_name}正在营业')
        print(f'{self.number_served}人正在就餐')
    def set_number_served(self,increment_number):
        """让就餐人数增加"""
        self.number_served += increment_number
        print(f'{self.number_served}人正在就餐')

fish = Restaurant('food','fish',)
fish.open_restaurant()
fish.number_served = 1
fish.open_restaurant()
fish.number_served = 2
fish.open_restaurant()
fish.restaurant_name = '码哥烤鱼'
fish.number_served = 20
fish.open_restaurant()
fish.set_number_served(100)
fish.open_restaurant()

