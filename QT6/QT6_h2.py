import csv

data = []

with open('wares.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        data.append((row[0], int(row[1])))


sorted_dta = sorted(data, key=lambda x: x[1])
balance = 1000
recommendations = []

for name, price in sorted_dta:
    nums = min(10, balance // price)
    if nums > 0:
        recommendations.extend([name] * nums)
        balance -= price * nums

if not recommendations:
    print('error')
else:
    print(', '.join(recommendations))