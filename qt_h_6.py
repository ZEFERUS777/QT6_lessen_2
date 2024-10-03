from PyQt6.QtWidgets import QApplication, QWidget, QLCDNumber, QSpinBox, QListWidget, QLabel, QPushButton, QLineEdit
import sys



class Pseudonym(QWidget):
    def __init__(self):
        super(Pseudonym, self).__init__()
        self.setGeometry(500, 500, 500, 400)
        self.lbl_ston = QLabel('Задать количество камней', self)
        self.lbl_ston.move(20, 25)
        self.stones = QSpinBox(self)
        self.stones.resize(130, 20)
        self.stones.move(185, 23)
        self.remainLcd = QLCDNumber(self)
        self.remainLcd.resize(473, 20)
        self.remainLcd.move(15, 55)
        self.startButton = QPushButton('Задать', self)
        self.startButton.clicked.connect(self.start)
        self.startButton.resize(100, 20)
        self.startButton.move(340, 23)
        self.lbl_st = QLabel('Сколько камней взять?', self)
        self.lbl_st.move(15, 83)
        self.takeInput = QLineEdit(self)
        self.takeInput.move(150, 83)
        self.takeInput.resize(339, 20)
        self.listWidget = QListWidget(self)
        self.listWidget.move(15, 111)
        self.listWidget.resize(473, 200)

    def start(self):
        self.remainLcd.display(self.stones.value())
        count_stones = self.stones.value()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Pseudonym()
    widget.show()
    sys.exit(app.exec())