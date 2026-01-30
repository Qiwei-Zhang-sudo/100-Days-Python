'''
快递运费计算：同城：首重 1kg 内 8 元，续重每 kg2 元；异地：首重 1kg 内 12 元，续重每 kg3 元。输入是否同城（0/1）和重量（kg），计算运费（重量≥1）。要求使用多分支if语句实现
'''
home = int(input('是否同城（0/1）:'))
kilo = int(input('快递净重（kg）：'))
bill = 0
if home :
    if kilo <= 1:
        bill = 8
        print(f'你的账单是{bill}元')
    else:
        bill = 8 + (kilo - 1) * 2
        print(f'你的账单是{bill}元')
else:
    if kilo <= 1:
        bill = 12
        print(f'你的账单是{bill}元')
    else: 
        bill = 12 +(kilo -1) *3
        print(f'你的账单是{bill}元')
