a='abcde'
b='abcde'
if a==b:
    print('True')
else:
    print('False')

c='zhangqiwei'
d='ZHANGQIWEI'
if d.lower()==c:
    print('Yes')
    print(d.lower())
else:
    print('No')

if 5 < 3:
    print("yes")
elif 5>3:
    print('NO')
else :
    print('error')

age = int(input('请输入你的年龄:'))
if age >= 18 and age <= 60:
    print('年龄充许')
elif age < 18:
    print('年龄不足')
elif age > 60 :
    print('年龄过大')

names=[
    'john',
    'anna',
    'alice',
    'tom',
]
if  'john' in names:
    print('Yes')

if 'jack' not in names:
    print('Yes')

name='zhangqiwei'
if 'qiwei' in name:
    print('OK')

