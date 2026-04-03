import random


class Die:
    """一个生成骰子的类"""
    def __init__(self,sides=6):
        """初始化属性"""
        self.sides = sides

    def roll_die(self):
        """打印1到骰子面数之间的随机数"""
        print(random.randrange(1,self.sides+1))


if __name__ == "__main__":
    example = Die(20)
    for _ in range(1,11):
        example.roll_die()

