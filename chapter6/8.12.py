def sandwich(*others):
    """添加任意数量的参数到列表中并打印出来"""
    for item in others:
        print(item)

sandwich('ham','tomato','cheese')
sandwich('chicken','fish',)
sandwich('egg',)
