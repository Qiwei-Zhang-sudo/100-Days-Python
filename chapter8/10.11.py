import json


number = input("Enter a number, and I'll tell you if it's even or odd: ")
with open('favorite_number.json','w') as file:
    json.dump(number,file)

with open('favorite_number.json','r') as file:
    number = json.load(file)

print(f"I know your favorite number! It's {number}")
