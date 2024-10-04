import sys

from PyQt6.QtWidgets import QWidget, QApplication, QTimeEdit, QCalendarWidget, QHBoxLayout, QVBoxLayout, QLineEdit, \
    QPushButton, QListWidget


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Мини планировщик')
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setGeometry(100, 100, 200, 200)
        self.timeEdit.setDisplayFormat('mm:ss')
        self.timeEdit.move(0, 0)
        self.timeEdit.resize(320, 25)
        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.move(0, 30)
        self.calendarWidget.resize(320, 400)
        self.main_lay = QHBoxLayout(self)
        self.left_lay = QVBoxLayout(self)
        self.right_lay = QVBoxLayout(self)

        self.left_lay.addWidget(self.timeEdit)
        self.left_lay.addWidget(self.calendarWidget)

        self.task_inp = QLineEdit(self)
        self.task_inp.move(0, 425)
        self.task_inp.resize(320, 25)
        self.left_lay.addWidget(self.task_inp)

        self.addEventBtn = QPushButton('Добавить событие', self)
        self.addEventBtn.clicked.connect(self.addEvent)
        self.addEventBtn.move(0, 460)
        self.addEventBtn.resize(320, 25)

        self.eventList = QListWidget(self)
        self.eventList.move(330, 0)
        self.eventList.resize(265, 485)

    def addEvent(self):
        selected_data = self.calendarWidget.selectedDate()
        self.eventList.addItem(
            f"{selected_data.toString('dd-MM-yyyy')} 00:{self.timeEdit.text()} - {self.task_inp.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec())
