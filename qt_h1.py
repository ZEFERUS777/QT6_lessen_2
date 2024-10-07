import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
import math


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.value = ""
        self.total = 0
        self.operation = None
        self.decision = ''

        for i in range(10):
            getattr(self, f'btn{i}').clicked.connect(lambda checked, num=str(i): self.add_num(num))
        self.btn_plus.clicked.connect(lambda: self.set_operation('add', '+'))
        self.btn_minus.clicked.connect(lambda: self.set_operation('sub', '-'))
        self.btn_mult.clicked.connect(lambda: self.set_operation('mul', '*'))
        self.btn_div.clicked.connect(lambda: self.set_operation('div', '/'))
        self.btn_pow.clicked.connect(lambda: self.set_operation('pow', '^'))
        self.btn_sqrt.clicked.connect(lambda: self.set_operation('sqrt', '√'))
        self.btn_fact.clicked.connect(lambda: self.set_operation('fact', '!'))
        self.btn_clear.clicked.connect(self.clear)
        self.btn_eq.clicked.connect(self.calculate)

    def add_num(self, number):
        self.value += number
        self.decision += number
        self.table.display(self.value)

    def set_operation(self, operation, symbol):
        if self.value:
            if self.decision:
                self.decision += symbol
            self.total = float(self.value)
            self.value = ""
            self.operation = operation

    def calculate(self):
        if self.value:
            num = float(self.value)
            if self.operation == 'add':
                self.total += num
            elif self.operation == 'sub':
                self.total -= num
            elif self.operation == 'mul':
                self.total *= num
            elif self.operation == 'div':
                try:
                    self.total /= num
                except ZeroDivisionError:
                    self.table.display("Error")
                    return
            self.table.display(str(eval(self.decision)))
            self.value = ""
            self.operation = None
            self.decision = ''

    def clear(self):
        self.value = ""
        self.total = 0
        self.operation = None
        self.decision = ''
        self.table.display("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
