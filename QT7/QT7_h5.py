from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox, QLineEdit, QLabel, QPushButton
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())