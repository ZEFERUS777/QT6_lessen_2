import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.uip', self)
        self.pushButtonEqual.clicked.connect(self.calculate)
        self.pushButtonClear.clicked.connect(self.clear)

    def calculate(self):
        try:
            expression = self.lineEdit.text()
            result = eval(expression)
            self.lineEdit.setText(str(result))  #
        except ZeroDivisionError:
            self.show_error("Ошибка: Деление на ноль.")
        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}")

    def clear(self):
        self.lineEdit.clear()

    def show_error(self, message):
        QMessageBox.critical(self, 'Ошибка', message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
