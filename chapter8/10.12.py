import json


def get_stored_number():
    """尝试从文件中已存取的数字，若不存在返回None"""
    try:
        with open('favorite_number.json','r') as file:
            number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number
    
def get_new_number():
    """提示用户输入一个喜欢的数字，并将其存储到文件中"""
    number = input("请输入你喜欢的数字: ")
    with open('favorite_number.json','w') as file:
        json.dump(number, file)
    return number

def greet_number():
    """先查询是否已存储数字，存在则显示，否则收集新数字"""
    number = get_stored_number()
    if number:
        print(f'I know your favorite number! It\'s {number}')
    else:
        number = get_new_number()
        print(f'我们已经记住了你的喜欢的数字: {number}')

greet_number()
greet_number()
