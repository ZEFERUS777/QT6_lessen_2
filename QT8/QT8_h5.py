import sqlite3
import sys

from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QTableWidget, QStatusBar, QTableWidgetItem, QMessageBox, \
    QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 500)

        self.textEdit = QLineEdit(self)
        self.textEdit.move(20, 20)
        self.textEdit.resize(100, 45)

        self.pushButton = QPushButton('Запуск', self)
        self.pushButton.move(self.textEdit.x() + self.textEdit.width() + 5, self.textEdit.y() + 10)

        self.saveButton = QPushButton('Изменить', self)
        self.saveButton.move(self.pushButton.x() + self.pushButton.width() - 20, self.pushButton.y())

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, self.textEdit.y() + self.textEdit.height() + 20)
        self.tableWidget.resize(660, 350)

        self.statusbar = QStatusBar(self)
        self.statusbar.move(20, self.tableWidget.y() + self.tableWidget.height() + 30)

        self.pushButton.clicked.connect(self.load_items)
        self.saveButton.clicked.connect(self.edit_items)

        self.conn = sqlite3.connect('films_db.sqlite')
        self.cursor = self.conn.cursor()

    def load_items(self):
        parameter = self.textEdit.text().strip()
        if not parameter.isdigit():
            self.statusbar.showMessage("Введите корректный индекс")
            return

        parameter = int(parameter)
        self.cursor.execute('SELECT * FROM films WHERE id = ?', (parameter,))
        self.result = self.cursor.fetchall()

        if not self.result:
            self.statusbar.showMessage("По этому запросу ничего не найдено")
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
        else:
            self.statusbar.showMessage("")
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(str(self.result[0][0])))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(self.result[0][1]))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(str(self.result[0][2])))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(str(self.result[0][3])))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(str(self.result[0][4])))

    def edit_items(self):
        parameter = self.textEdit.text().strip()
        if not parameter.isdigit():
            self.statusbar.showMessage("Введите корректный индекс")
            return
        parameter = int(parameter)
        self.cursor.execute('SELECT * FROM films WHERE id = ?', (parameter,))
        res = self.cursor.fetchall()

        if not res:
            self.statusbar.showMessage("По этому запросу ничего не найдено")
            return
        old_title = res[0][1]
        year = res[0][2]
        genre = res[0][3]
        duration = res[0][4]

        new_title = old_title[::-1]
        new_year = year + 1000
        new_duration = duration * 2
        self.cursor.execute('UPDATE films SET title = ?, year = ?, duration = ? WHERE id = ?',
                            (new_title, new_year, new_duration, parameter))
        self.conn.commit()
        self.load_items()
        QMessageBox.information(self, "Успешно", "Запись успешно изменена")

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
