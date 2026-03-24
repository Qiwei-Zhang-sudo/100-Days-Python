class Restaurant:
    """一个关于餐厅的类"""
    def __init__(self,restaurant_name,restaurant_type):
        """初始化餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
    def decrible(self):
        print(f"名称：{self.restaurant_name}")
        print(f'类型：{self.restaurant_type}')
    def open(self):
        print('我们正在营业中')

class IceCreamStand(Restaurant):
    """一个餐厅的子类"""
    def __init__(self, restaurant_name, restaurant_type,*flavors):
        """初始化子类的属性"""
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = list(flavors[:]) 
    def show_flavors(self):
        if self.flavors == []:
            print('我们没有冰淇淋')
        else:
            for flavor in self.flavors:
                print(flavor)

# 函数参数*args 接受任意数量的参数，打包为一个元组，**args 接受任意数量的参数，打包为一个字典
example = IceCreamStand('冰淇淋小店','冰淇淋','香草','巧克力','草莓')
example.show_flavors()
example.decrible()
example.open()
print(bool(example.flavors))
# del example.flavors[:]
# example.flavors = []
# example.flavors[:] = []
# example.clear()
print(bool(example.flavors))
example.show_flavors()