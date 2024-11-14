import sqlite3

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox, QLineEdit, QLabel, QPushButton, QListWidget
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 250)
        self.parameterSelection = QComboBox(self)
        self.parameterSelection.addItems(['Год выпуска', 'Название', 'Продолжительность'])
        self.parameterSelection.move(10, 10)
        self.parameterSelection.resize(190, 23)

        self.queryLine = QLineEdit(self)
        self.queryLine.move(self.parameterSelection.x() + self.parameterSelection.width() + 10,
                            self.parameterSelection.y())
        self.queryLine.resize(self.parameterSelection.size())

        self.queryButton = QPushButton('Поиск', self)
        self.queryButton.move(self.queryLine.x() + self.queryLine.width() + 5, self.queryLine.y() - 5)
        self.queryButton.resize(70, 29)

        self.id_lbl = QLabel('ID:', self)
        self.id_lbl.move(self.parameterSelection.x() + 5,
                         self.parameterSelection.y() + self.parameterSelection.height() + 10)

        self.name_lbl = QLabel('Название:', self)
        self.name_lbl.move(self.id_lbl.x(), self.id_lbl.y() + 20)

        self.year_lbl = QLabel('Год выпуска:', self)
        self.year_lbl.move(self.name_lbl.x(), self.name_lbl.y() + 20)

        self.janr_lbl = QLabel('Жанр:', self)
        self.janr_lbl.move(self.year_lbl.x(), self.year_lbl.y() + 20)

        self.duration_lbl = QLabel('Продолжительность:', self)
        self.duration_lbl.move(self.janr_lbl.x(), self.janr_lbl.y() + 20)

        self.queryButton.clicked.connect(self.query_database)

        self.idEdit = QLineEdit(self)
        self.idEdit.move(self.duration_lbl.x() + self.duration_lbl.width() + 15, self.id_lbl.y() - 5)
        self.idEdit.resize(200, 23)

        self.titleEdit = QLineEdit(self)
        self.titleEdit.move(self.idEdit.x(), self.idEdit.y() + self.idEdit.height() + 3)
        self.titleEdit.resize(200, 23)

        self.yearEdit = QLineEdit(self)
        self.yearEdit.move(self.titleEdit.x(), self.titleEdit.y() + self.titleEdit.height() + 3)
        self.yearEdit.resize(200, 23)

        self.genreEdit = QLineEdit(self)
        self.genreEdit.move(self.yearEdit.x(), self.yearEdit.y() + self.yearEdit.height() + 3)
        self.genreEdit.resize(200, 23)

        self.durationEdit = QLineEdit(self)
        self.durationEdit.move(self.genreEdit.x(), self.genreEdit.y() + self.genreEdit.height() + 3)
        self.durationEdit.resize(200, 23)
        self.duration_lbl.adjustSize()

        self.errorlnl = QLabel('', self)
        self.errorlnl.move(self.duration_lbl.x(), self.duration_lbl.y() + self.duration_lbl.height() + 40)

    def query_database(self):
        parameter = self.parameterSelection.currentText()
        search = self.queryLine.text()
        conn = sqlite3.connect('films_db.sqlite')
        curr = conn.cursor()
        result = None
        execute = None

        if parameter == 'Год выпуска':
            curr.execute("""
            SELECT films.id, films.title, films.year, genres.title, 
            films.duration FROM films JOIN genres ON films.genre = genres.id WHERE films.year = ?""", (search,))

            result = curr.fetchall()
            if len(result) > 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            elif len(result) == 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            elif len(result) == 0:
                self.errorlnl.setText('Ничего не найдено')
        elif parameter == 'Название':
            curr.execute("""
            SELECT films.id, films.title, films.year, genres.title, 
            films.duration FROM films JOIN genres ON films.genre = genres.id WHERE films.title = ?""", (search,))
            result = curr.fetchall()
            if len(result) > 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            elif len(result) == 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            else:
                self.errorlnl.setText('Ничего не найдено')
        elif parameter == 'Продолжительность':
            curr.execute("""
            SELECT films.id, films.title, films.year, genres.title, 
            films.duration FROM films JOIN genres ON films.genre = genres.id WHERE films.duration = ?""", (search,))
            result = curr.fetchall()
            if len(result) > 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            elif len(result) == 1:
                exer = result[0]
                self.idEdit.setText(str(exer[0]))
                self.titleEdit.setText(str(exer[1]))
                self.yearEdit.setText(str(exer[2]))
                self.genreEdit.setText(str(exer[3]))
                self.durationEdit.setText(str(exer[4]))
            else:
                self.errorlnl.setText('Ничего не найдено')
        self.errorlnl.adjustSize()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
