from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QToolButton
import sys


class WidgetArt(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.matrix = matrix
        self.setGeometry(400, 400, 500, 500)
        self.setWindowTitle('Art')
        self.widgetArt = QGridLayout(self)
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                button = QPushButton('*' if value == 1 else '')
                button.setFixedSize(40, 40)

                self.widgetArt.addWidget(button, i, j)
        self.setLayout(self.widgetArt)
