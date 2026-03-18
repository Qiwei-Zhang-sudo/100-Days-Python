
def make_album(singer='zhangsan', album=2026):
    """ 接受歌手名称和专辑名称并存入字典中 """



while True:
    print('enter "q" at any tiem to quit')
    singer = input('Please enter your favorite singer:')
    if singer == 'q':
        break
    album = input('Please enter your favorite ablum:')
    if album == 'q':
        break
    make_album(singer, album)

for key, value in album.items():
    print(f'{key} : {value}')
