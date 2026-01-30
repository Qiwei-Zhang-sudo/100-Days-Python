current_names = [
    'Admin',
    'John',
    'Alice',
    'Anne',
]
new_names = [
    'ADMIN',
    'ALICE',
    'JACK',
]
# 向列表中添加元素
# 方法append(默认向列表末尾追加至少一个元素)
# 方法insert(提供位置，和值，向指定位置插入)
# 方法extend(向列表末尾至少提供一个元素)
new_current_names=[]
for name in current_names:
    new_current_names.append(name.lower())

print(new_current_names)

for name in new_names:
    username = 1
    for nae in new_current_names:
        if name.lower() == nae:
            username = 0
            break
    if not username:
        print(f'你的用户名{name}已经被占用！')
    else:
        print(f'你的用户名{name}可以使用！')

 