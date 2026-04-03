with open('guest.txt','a') as file:
    while True:
        username = input('请输入你的名字：（输入q退出）')
        if username == 'q':
            break
        file.write(username + '\n')