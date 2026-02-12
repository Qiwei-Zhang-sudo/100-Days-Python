while True:
    age = int(input('Please enter your age:'))
    if  0 < age < 3:
        print('Ticket price: free')
    elif 3 <= age < 12:
        print('Ticket price: 10')
    elif age >= 12:
        print('Ticket price: 15')
    else:
        break
