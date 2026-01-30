age = int(input('please add your age:'))
if age < 2:
    print("婴儿")
elif 2 <= age < 4:
    print('幼儿')
elif 4 <= age < 13:
    print('儿童')
elif 13 <= age < 18:
    print('少年')
elif 18 <= age < 65:
    print('中青年人')
else:
    print('老年人')