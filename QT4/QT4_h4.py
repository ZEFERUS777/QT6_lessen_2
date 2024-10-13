from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QApplication, QHBoxLayout
import sys
import random


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 350, 50)
        self.file_read = 'lines.txt'
        self.button = QPushButton('Получить', self)
        self.button.move(10, 13)
        self.text_field = QTextEdit(self)
        self.text_field.resize(250, 20)
        self.text_field.move(95, 15)
        self.button.clicked.connect(self.random_string)

    def random_string(self):
        with open(self.file_read, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.text_field.setText(random.choice(lines) if len(lines) > 0 else '')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomString()
    window.show()
    sys.exit(app.exec())
