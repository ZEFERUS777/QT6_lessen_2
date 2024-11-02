import csv

data = {}

with open('rez.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        data[row['login']] = [row['Score'], row['user_name']]

units = {}
school_number, class_number = input().split()

for key in data:
    fg = key.split('-')
    if fg[2] == str(school_number) and fg[3] == str(class_number):
        units[key] = data[key]

sorted_units = sorted(units.items(), key=lambda x: x[1][0], reverse=True)
for unit in sorted_units:
    unity = unit[1][1].split(' ')
    print(f'{unity[3]} {unit[1][0]}')
