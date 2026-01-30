names = [
    'admin',
    'john',
    'jack',
    'alice',
]
for name in names:
    if name == 'admin':
        print(f'Hello,{name},would you like to see a status report')
    else:
        print(f"Hello {name},thank you for logging in again")