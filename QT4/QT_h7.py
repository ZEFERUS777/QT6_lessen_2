import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QTextBrowser


class Suffle(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 350, 370)
        self.setWindowTitle("Text refresh")

        self.button = QPushButton("Загрузить строки", self)
        self.button.move(20, 20)

        self.text_field = QTextBrowser(self)
        self.text_field.move(20, 50)
        self.text_field.resize(300, 300)
        self.button.clicked.connect(self.reformatertext)

    def reformatertext(self):
        with open("lines.txt", "r", encoding="utf-8") as f:
            file = f.readlines()

        even_lines = [value for idx, value in enumerate(file) if idx % 2 == 0]
        odd_lines = [value for idx, value in enumerate(file) if idx % 2 != 0]

        self.text_field.append('\n'.join(even_lines))
        self.text_field.append('\n'.join(odd_lines))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Suffle()
    window.show()
    sys.exit(app.exec())
