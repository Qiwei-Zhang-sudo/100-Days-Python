names = [
    'john',
    'admin',
    'alice',
    'jack'
]
for name in names:
    if name == 'admin':
        print('yes')
    else:
        print('ok')

# 删除列表元素
# 方法remove（按值删除）
# 方法clear(清空整个列表)
# 方法pop(根据索引删除)
# 函数del(根据切片删除)

names.clear()
print(names)
if not names:
    print('We need to find some users')
else:
    for name in names:
        if name == 'admin':
            print('yes')
        else:
            print('ok')