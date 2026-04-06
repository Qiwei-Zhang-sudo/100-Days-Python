from pathlib import Path


try:
    with open("cats.txt",'r') as file:
        contents = file.readlines()
        print(contents)
except FileNotFoundError:
    print("Sorry,the file doesn't exist.")

try:
    dogs = Path('dogs.txt')
    contents = dogs.read_text()
    print(contents)
except FileNotFoundError:
    print("Sorry, the file doesn't exist.")