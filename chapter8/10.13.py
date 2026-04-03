import json


name = input('Please enter your name:')
age = input('Please enter your age:')
address = input("Please enter your address:")
with open('remember_me.json','w') as file:
    info = {}
    info.update({'name': name,'age':age,'address':address})
    json.dump(info,file)
    print('信息保存成功')

with open('remember_me.json','r') as file:
    user_info = json.load(file)
    for key,value in user_info.items():
        print(f'{key}: {value}')
