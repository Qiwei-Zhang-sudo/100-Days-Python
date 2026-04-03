with open('learning_python.txt','r') as file:
    content = file.read()
    print(content)
    new_content = content.replace('python','C')
    print(new_content)