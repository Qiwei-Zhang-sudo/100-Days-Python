from pathlib import Path
import json


def get_stored_username(path):
    """读取用户的用户名"""
    if path.exists():
        try:
            contents = path.read_text()
            user_data = json.loads(contents)
            return user_data['username']
        except FileNotFoundError:
            return None
    return None 

def get_new_username():
    """获取用户信息"""
    username = input("请输入你的用户名：")
    age = input("请输入你的年龄：")
    address = input("请输入你的地址：")
    return {'username': username, 'age': age, 'address': address}

def greet_user():
    """问候用户，并验证"""
    path = Path('remember_me.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"你是 {username} 吗？(y/n) ")
        if correct.lower() == 'y':
            print(f"欢迎回来，{username}！")
        else:
            user_data = get_new_username()
            path.write_text(json.dumps(user_data))
            print(f"我们会记住你，{user_data['username']}！")

greet_user()


