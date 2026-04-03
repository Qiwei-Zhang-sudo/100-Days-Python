print("Enter 'q' to quit.")
while True:
    try:
        x = input('Enter a number:')
        if x == 'q':
            break
        y = input('enter a number:')
        if y == 'q':
            break
        sum_result = int(x) + int(y)
    except ValueError:
        print('ValueError,Please enter a number again.')
    else:
        print(f'The sum of {x} and {y} is {sum_result}')
                                        