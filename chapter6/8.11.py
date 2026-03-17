def send_messages(messages, sent_messages):
    """ Print a every message, and move it to sent_messages """
    current_messages = messages[:]
    while current_messages:
        current_message = current_messages.pop()
        sent_messages.append(current_message)
   
profile = [
    'my name is magnus grant',
    'my motto is practice makes perfect',
    'my age is 19',
    'i love python',
]
send_profile = []
send_messages(profile, send_profile)
print(profile)
print('*'*50)
print(send_profile)