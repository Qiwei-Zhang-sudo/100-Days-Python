numbers=[item**2 for item in range(1,11)]
for number in numbers[:3]: # 默认从列表的开头开始遍历
    print(f"The first three items in the list are:{number}")
for number in numbers[3:6]:
    print(f"Three items from the middle of the list are:{number}")
for number in numbers[-3:]: # 默认到列表的结尾结束遍历
    print(f"The last items in the list are:{number}")


