import csv
import sys
import random

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QApplication, QWidget, QTableWidget,
                             QTableWidgetItem, QLineEdit, QLabel,
                             QPushButton)


class Expensive(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 700, 400)
        self.setWindowTitle('Интерактивный чек')
        self.objects = []
        with open('price.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                self.objects.append((row[0], int(row[1])))

        self.objects = sorted(self.objects, key=lambda x: x[1], reverse=True)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(len(self.objects))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Цена', 'Количество'])
        self.tableWidget.resize(700, 300)
        for item, price in self.objects:
            self.tableWidget.setItem(self.objects.index((item, price)), 0, QTableWidgetItem(item))
            self.tableWidget.setItem(self.objects.index((item, price)), 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(self.objects.index((item, price)), 2, QTableWidgetItem('0'))
        self.total = QLineEdit(self)
        self.total.move(550, self.tableWidget.y() + self.tableWidget.height() + 10)

        self.total_price_lbl = QLabel('Итого:', self)
        self.total_price_lbl.move(500, self.total.y() + 3)
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.itemChanged.connect(self.update_total)
        self.total_sum = 0

        self.updateButton = QPushButton('Обновить', self)
        self.updateButton.move(self.tableWidget.x() + 10, self.tableWidget.y() + self.tableWidget.height() + 10)

        self.update_colors()

        self.updateButton.clicked.connect(self.update_colors)

    def update_total(self):
        self.total_sum = 0
        for i in range(self.tableWidget.rowCount()):
            self.total_sum += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.total.setText(str(self.total_sum))

    def update_colors(self):
        for i in range(5):
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.tableWidget.item(i, 0).setBackground(color)
            self.tableWidget.item(i, 1).setBackground(color)
            self.tableWidget.item(i, 2).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Expensive()
    window.show()
    sys.exit(app.exec())
