from pathlib import Path


username = input('What is your name:')
path = Path("guest.txt")
path.write_text(username)
