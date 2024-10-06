import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTimeEdit, QCalendarWidget, QHBoxLayout, QVBoxLayout, QLineEdit, \
    QPushButton, QListWidget
from PyQt6.QtCore import QDateTime


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Мини планировщик')
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setDisplayFormat('mm:ss')
        self.calendarWidget = QCalendarWidget(self)

        self.main_lay = QHBoxLayout(self)
        self.left_lay = QVBoxLayout(self)
        self.right_lay = QVBoxLayout(self)

        self.left_lay.addWidget(self.timeEdit)
        self.left_lay.addWidget(self.calendarWidget)

        self.task_inp = QLineEdit(self)
        self.left_lay.addWidget(self.task_inp)

        self.addEventBtn = QPushButton('Добавить событие', self)
        self.addEventBtn.clicked.connect(self.addEvent)
        self.left_lay.addWidget(self.addEventBtn)

        self.eventList = QListWidget(self)
        self.right_lay.addWidget(self.eventList)

        self.main_lay.addLayout(self.left_lay)
        self.main_lay.addLayout(self.right_lay)

        self.events = []

    def addEvent(self):
        selected_date = self.calendarWidget.selectedDate()
        time_str = self.timeEdit.text()
        task_str = self.task_inp.text()

        event_time = QDateTime(selected_date.year(), selected_date.month(),
                               selected_date.day(), int(time_str[:2]), int(time_str[3:]))

        self.events.append((event_time, task_str))
        self.events.sort(key=lambda x: x[0])

        self.updateEventList()

    def updateEventList(self):
        self.eventList.clear()
        for event_time, task_str in self.events:
            self.eventList.addItem(f"{event_time.toString('dd-MM-yyyy hh:mm')} - {task_str}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimplePlanner()
    window.show()
    sys.exit(app.exec())
