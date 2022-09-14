import os 
from pathlib import Path

path_os = os.getcwd()
path_Path = Path.cwd()

print(path_Path)
print(path_Path.name)
print(type(path_Path))

path = Path('test/expenses.txt')

print(path)
print(path.parts)
print(path.name)
print(path.stem)
print(path.suffix)