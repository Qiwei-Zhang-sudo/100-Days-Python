"""
python语言中的变量
version:0.03
name:zqw

"""
# int float str bool char
a=100
b=123.45
c=True
d='abc'
print(type(a))
print(type(b))
print(type(c))
print(type(d))
e='100'
f='123.45'
print(int(b))
print(float(a))
print(int(e))
print(int(c))
print(chr(a))# 将字符编码（整数）转化为相应的字符串（一个字符）
print(ord('d'))# 将相应的字符串（一个字符）转化为相应的字符编码（整数）
print(int(e,base=2))# base指定了参数的进制，它是一个base进制的参数
print(int(e,base=8))
print(int(e,base=16))
print(0x256) # 16进制
print(0o64) # 8进制
print(0b11) # 2进制
