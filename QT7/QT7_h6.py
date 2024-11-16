import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.connector = sqlite3.connect('films_db.sqlite')
        self.cursor = self.connector.cursor()

        self.cursor.execute("SELECT title FROM genres")

        dt = self.cursor.fetchall()

        self.result = [row[0] for row in dt]

        self.setGeometry(300, 300, 550, 350)
        self.setWindowTitle('Фильтрация по жанрам')

        self.parameterSelection = QComboBox(self)
        self.parameterSelection.move(20, 20)
        self.parameterSelection.resize(150, 20)
        self.parameterSelection.addItems(self.result)

        self.queryButton = QPushButton('Пуск', self)
        self.queryButton.move(45, 80)
        self.queryButton.resize(90, 40)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(self.parameterSelection.x() + self.parameterSelection.width() + 10,
                              self.parameterSelection.y())
        self.tableWidget.resize(350, 300)
        self.addobj()

        self.queryButton.clicked.connect(self.addobj)

    def addobj(self):
        self.cursor.execute("""SELECT films.title, films.genre, films.year FROM films 
        JOIN genres ON films.genre = genres.id WHERE genres.title = ?""", (self.parameterSelection.currentText(),))

        reslt = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(reslt))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])
        for i, elem in enumerate(reslt):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
