def make_album(singer='zhangsan', album=2026):
    ''' 接受歌手名和专辑名并返回一个字典 '''
    return {singer: album}


a = make_album('chenglong', 2019)
print(a)

b = make_album('zhangsan', 2018)
print(b)

c = make_album('lisi', 2017)
print(c)

d = make_album(singer='wangwu')
print(d)