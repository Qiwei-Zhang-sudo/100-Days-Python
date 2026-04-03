a = input('请输入第一个数字：')
b = input('请输入第二个数字：')
try:
    sum_result = int(a) + int(b)
except ValueError:
    print('输入异常，请重新输入')
else:
    print(f'两个数字之和：{sum_result}')
