"""
python:语言中的运算符
version:0.04
name:zqw
"""
# and(&&) or(||) not(!) 逻辑级运算用与整体判断真假，结果为bool型
# 按位与，按位或，按位异或，位级运算，逻辑门电路的基础
flog0=1==1
flog1=2>=3
flog3=5!=flog1
flog4=flog1 and flog3
flog5=flog3 or flog4
flog6 =not flog3
print(flog0);print(flog1);print(flog3)
print(flog4);print(flog5);print(flog6)
print("-"*50)
print("将华氏温度转化为摄氏温度")
f=float(input("请输入华氏温度："))
c=(f-32)/1.8
print('%.2f华氏度=%.2f摄氏度' % (f,c))
print(f'{f:.2f}华氏度={c:.2f}摄氏度')
print('-'*50)
print("计算圆的面积")
import math
radius =float(input('请输入半径：'))
perimeter=2*math.pi*radius
area=math.pi*radius**2
print(f"面积：{area:.2f} 周长：{perimeter:.2f}")
print("-"*50)
print("判断闰年")
year=int(input("请输入年份："))
is_leap=year%4==0 and year%100!=0 or year%400==0
print(f'{is_leap=}')
