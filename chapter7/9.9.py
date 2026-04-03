class Battery:
    """这是一个关于电池的类"""
    def __init__(self,content=100):
        """初始化电池的属性"""
        self.content = content

    def upgrade_battery(self,new_content):
        """更新电池的电量"""
        self.content = new_content
        print(f'当前电量f{self.content}')


class ElectronicCar:
    """这是一个关于带电车的类"""


