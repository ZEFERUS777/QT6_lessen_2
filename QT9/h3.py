import sqlite3

# Подключение к базе данных (если база данных не существует, она будет создана)
conn = sqlite3.connect('items.sql')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS Types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Spaces (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type INTEGER,
    year INTEGER,
    space INTEGER,
    FOREIGN KEY (type) REFERENCES Types(id),
    FOREIGN KEY (space) REFERENCES Spaces(id)
)
''')

# Вставка тестовых данных в таблицу Types
types_data = [
    (1, 'Мебель'),
    (2, 'Бытовая техника'),
    (3, 'Электроника')
]
cursor.executemany('INSERT INTO Types (id, name) VALUES (?, ?)', types_data)

# Вставка тестовых данных в таблицу Spaces
spaces_data = [
    (1, 'Кухня'),
    (2, 'Гостиная'),
    (3, 'Спальная комната')
]
cursor.executemany('INSERT INTO Spaces (id, name) VALUES (?, ?)', spaces_data)

# Вставка тестовых данных в таблицу Items
items_data = [
    (1, 'Стол', 1, 2018, 1),
    (2, 'Холодильник', 2, 2019, 1),
    (3, 'Диван', 1, 2020, 2),
    (4, 'Телевизор', 3, 2021, 2),
    (5, 'Кровать', 1, 2017, 3),
    (6, 'Пылесос', 2, 2022, 3)
]
cursor.executemany('INSERT INTO Items (id, name, type, year, space) VALUES (?, ?, ?, ?, ?)', items_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно создана и заполнена тестовыми данными.")