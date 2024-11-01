import csv

inp = float(input())
data = []
out = []

with open('vps.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        data.append(row)


for line in data:
    percent = line[4]
    if float(percent) >= inp:
        out.append(line[0])

print('\n'.join(out))