from pathlib import Path


dogs = Path('learning_python.txt')
contents = dogs.read_text().lower()
number = contents.count('the')
print(number)
