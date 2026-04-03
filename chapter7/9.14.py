import random


numbers = list(str(n) for n in range(1,10))
letters = ['a','b','c','d',]
pool = numbers + letters

winning = random.sample(pool,4)
print(f'本期中奖号码：{winning}')

try:
    user = list(input('请输入4个不重复的数字或字母：'))
    print(user)
    if len(user) != 4:
        raise ValueError
    if user == winning:
        print('恭喜你中奖了')
    else:
        print('你未中奖')
except ValueError:
    print('输入格式不正确，请重新输入')
