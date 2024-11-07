import csv

Name_of_the_Federal_District = input().strip()
year_start, year_end = map(int, input().strip().split())

data = {}

with open('salary.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        if row['Федеральный округ'] == Name_of_the_Federal_District:
            data[row['Субъект']] = list((row[str(year_start)], row[str(year_end)]))

output = []

for key in data:
    val_1, val_2 = map(int, data[key])
    if val_2 < val_1 * 1.04:
        output.append([key, str(val_1), str(val_2)])

with open('out_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    if output:
        writer.writerow(['Субъект', str(year_start), str(year_end)])
        writer.writerows(output)
