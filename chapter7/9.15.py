import random

numbers = list(range(1,10))
winning = random.sample(numbers,4)

count = 0
while True:
    drawn = random.sample(numbers,4)
    count += 1
    if drawn == winning:
        print('你中奖了')
        print(count)
        break
    if count > 1000:
        print('你没有中奖')
        break