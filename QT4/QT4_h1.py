import random

file = open('lines.txt')
lines = file.readlines()
if len(lines) > 0:
    print(lines[random.randint(0, len(lines) - 1)])
file.close()