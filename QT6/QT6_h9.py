import csv

s = {}
with open('input.csv', encoding='utf-8') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
    Start = reader[-1]
    for c in reader[:-1]:
        if c[0] == Start[0] and c[1] == Start[1]:
            s[f'{c[0]} {c[1]}'] = int(c[2])
            continue
        for j in reader[:-1]:
            if c[1] == j[0] and c[0] == Start[0] and j[1] == Start[1]:
                s[f'{c[0]} {c[1]} {j[1]}'] = int(c[2]) + int(j[2])
    f = min(s.values())
    for c in s.keys():
        if s[c] == f:
            print(c)
