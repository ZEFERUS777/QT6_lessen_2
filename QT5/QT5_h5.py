import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QInputDialog
import random


class RandomFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 300, 400)
        self.button = QPushButton('Ввести количество цветов флага', self)
        self.button.move(70, 100)
        self.button.adjustSize()
        self.base = [self.button.x(), self.button.y() + self.button.height() + 20, 120, 30]
        self.button.clicked.connect(self.activate_dialog)
        self.num = 3
        self.do_paint = False

    def activate_dialog(self):
        self.number, ok_pressed = QInputDialog.getInt(self, 'Enter the number of flag colors',
                                                      'Enter the number of flag colors', 3, 1,
                                                      10, 1)
        self.num = int(self.number)
        if ok_pressed:
            self.paint()

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            self.draw_flag(qp)

    def draw_flag(self, qp):
        colors = [QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in
                  range(self.num)]
        qp.setBrush(QColor(255, 255, 255))
        for i in range(self.num):
            qp.setBrush(colors[i])
            qp.drawRect(self.base[0], self.base[1], self.base[2], self.base[3])
            self.base[1] += 30


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomFlag()
    window.show()
    sys.exit(app.exec())
