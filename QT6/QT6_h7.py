import csv

data = {}

with open('wares.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        data[row[0]] = [row[1], row[2]]

output = []

for key, value in data.items():
    if int(value[0]) > int(value[1]):
        output.append(key)

print('\n'.join(output) if output else '')