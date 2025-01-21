import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QApplication, QWidget


class Clicker(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setGeometry(300, 300, 300, 300)

        self.main_lay = QVBoxLayout(self)
        self.click_lay = QLabel(self, text=f'Clicked: {self.counter}')
        self.click_lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_lay.addWidget(self.click_lay)

        self.click_btn = QPushButton(self, text='Click me')
        self.main_lay.addWidget(self.click_btn)
        self.click_btn.clicked.connect(self.update_counter)

        self.reset_btn = QPushButton(self, text='Reset')
        self.main_lay.addWidget(self.reset_btn)
        self.reset_btn.clicked.connect(self.reset_counter)

        self.change_the_result = QPushButton(self, text='Change the result')
        self.main_lay.addWidget(self.change_the_result)

        self.main_lay.setContentsMargins(20, 20, 20, 20)

        font = QFont('Arial Black', 20)
        self.click_lay.setFont(font)

        self.click_btn.setStyleSheet("""
        QPushButton:pressed {background-color: rgb(100, 195, 227);
        }""")
        self.reset_btn.setStyleSheet("""
        QPushButton:pressed {background-color: red;
        }""")

        self.setStyleSheet("""
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
        border: 2px solid rgb(100, 195, 227);
        """)

    def update_counter(self):
        self.counter += 1
        self.click_lay.setText(f'Clicked: {self.counter}')

    def reset_counter(self):
        self.counter = 0
        self.click_lay.setText(f'Clicked: {self.counter}')

    def change_the_result(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Clicker()
    window.show()
    sys.exit(app.exec())
