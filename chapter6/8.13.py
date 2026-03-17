def user_profile(first, last, **others):
    '''创建一个字典，其中包含我们知道的关于用户的一切'''
    """**others 用于接收任意数量的键值对并带包成一个字典"""
    profile = {'firstname': first,'lastname': last}
    profile.update(others)
    # update() 方法是Python字典的一个内置方法，
    # 用于将一个字典中的键值对更新到另一个字典中
    return profile

my_profile = user_profile(
    'magnus',
    'grant',
    age = 19,
    location = 'China',
    phone = 123456,
    )
# 字典中的元素用冒号表示键值对
# 在函数调用时传递关键字参数时，需要使用等号语法
''' 
age='19' - 这是关键字参数，age 是参数名，'19' 是值。
Python会将 age='19' 自动打包进 **others 字典中，变成
{'age': '19'}
这种方式下，age 是参数名称，不需要加引号

关键字参数用于函数调用时传递参数：

python
def my_function(age='19', location='china'):
    pass

my_function(age='20', location='USA')  # 这里age='20'是关键字参数
用于函数调用时指定参数
使用等号 = 连接参数名和值
参数名通常是标识符（不加引号）
让函数调用更清晰易懂
'''   
for key, value in my_profile.items():
    print(f'{key}: {value}')
    