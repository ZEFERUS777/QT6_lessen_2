import random
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_button)
        self.timer.start(10)  # Запускаем таймер с интервалом в 10 миллисекунд

    def initUi(self):
        self.setWindowTitle('Убегающая кнопка')
        self.setGeometry(300, 300, 450, 450)
        self.button = QPushButton('Нажми на меня', self)
        self.button.move(50, 50)
        self.button.resize(100, 50)

    def move_button(self):
        cursor_pos = self.mapFromGlobal(QCursor.pos())
        button_rect = self.button.geometry()
        button_center = button_rect.center()

        if (cursor_pos - button_center).manhattanLength() < 100:
            new_x = random.randint(0, self.width() - self.button.width())
            new_y = random.randint(0, self.height() - self.button.height())
            self.button.move(new_x, new_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
