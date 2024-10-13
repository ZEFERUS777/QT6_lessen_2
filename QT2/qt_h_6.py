from PyQt6.QtWidgets import QApplication, QWidget, QLCDNumber, QSpinBox, QListWidget, QLabel, QPushButton, QLineEdit
import sys
import random


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
        self.takeButton = QPushButton('Взять', self)
        self.takeButton.move(15, 110)
        self.takeButton.resize(473, 20)
        self.takeButton.clicked.connect(self.take)
        self.listWidget = QListWidget(self)
        self.listWidget.move(15, 140)
        self.listWidget.resize(473, 200)
        self.resultLabel = QLabel(self)
        self.resultLabel.move(200, 355)
        self.resultLabel.setFixedWidth(500)

    def start(self):
        self.listWidget.clear()
        self.remainLcd.display(self.stones.value())
        self.resultLabel.setText('')  # Clear win message on start

    def take(self):
        val = self.remainLcd.value()
        if val > 0:
            take_amount = int(self.takeInput.text() or 0)
            if 0 < take_amount <= val:
                val -= take_amount
                self.remainLcd.display(val)
                self.listWidget.addItem(f'Игрок взял - {take_amount}')
                if val <= 0:
                    self.resultLabel.setText('Выиграл игрок')
                else:
                    rnd = random.randint(1, min(1, val))  # Corrected random choice
                    val -= rnd
                    self.remainLcd.display(val)
                    self.listWidget.addItem(f'Компьютер взял - {rnd}')
                    if val <= 0:
                        self.resultLabel.setText('Выиграл компьютер')
            else:
                self.listWidget.addItem('Некорректное количество камней для взятия.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pseudonym()
    window.show()
    sys.exit(app.exec())
