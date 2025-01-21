import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, \
    QTableWidgetItem, QHBoxLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фильмы")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

        self.conn = sqlite3.connect('films_db.sqlite')
        self.cursor = self.conn.cursor()

        self.buttons = []
        layout = QHBoxLayout()
        for letter in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
            button = QPushButton(letter)
            button.setFixedSize(20, 20)
            button.clicked.connect(self.filter_films(letter))
            layout.addWidget(button)
            self.buttons.append(button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.tableWidget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.statusBar().showMessage("Готово")

    def init_ui(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Год", "Жанр", "Продолжительность"])

    def filter_films(self, letter):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        query = f"SELECT * FROM films WHERE title LIKE '{letter}%'"
        self.cursor.execute(query)
        films = self.cursor.fetchall()

        for row_number, film in enumerate(films):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(film):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        count = len(films)
        if count > 0:
            self.statusBar().showMessage(f"Нашлось {count} записей")
        else:
            self.statusBar().showMessage("К сожалению, ничего не нашлось.")

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
