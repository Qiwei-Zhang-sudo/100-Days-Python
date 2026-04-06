"""
静默：
在程序发生异常时，不输出任何错误信息，
也不向用户输出任何异常情况
与pass搭配使用
"""
try:
    with open("cats.txt",'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    pass
