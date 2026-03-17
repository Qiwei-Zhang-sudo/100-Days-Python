def send_messages(messages, sent_messages):
    """ Print a every message, and move it to sent_messages """
    while messages:
        current_message = messages.pop()
        print(f'Printing message: {current_message}')
        sent_messages.append(current_message)
      
profile = [
    'Hello World!',
    'Hello Pyhton',
    'My name is Magnus Grant',
    'My motto is practice makes perfect'
]
send_profile = []
send_messages(profile, send_profile)
print(profile)
print(send_profile)
