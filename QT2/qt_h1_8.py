import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QCheckBox, QPushButton, QPlainTextEdit


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MacOrder')
        self.layout = QVBoxLayout(self)
        self.menu_checkboxes = {'Чизбургер': QCheckBox('Чизбургер'),
                                'Гамбургер': QCheckBox('Гамбургер'),
                                'Кока-кола': QCheckBox('Кока-кола'),
                                'Наггетсы': QCheckBox('Наггетсы'), }

        for item in self.menu_checkboxes.values():
            self.layout.addWidget(item)

        self.order_btn = QPushButton('Заказать', self)
        self.order_btn.clicked.connect(self.order)
        self.layout.addWidget(self.order_btn)
        self.order_btn.setContentsMargins(0, 40, 0, 40)

        self.result = QPlainTextEdit(self)
        self.result.setContentsMargins(0, 20, 0, 20)
        self.layout.addWidget(self.result)

    def order(self):
        self.result.clear()
        self.result.appendPlainText('Ваш заказ:\n')
        for item in self.menu_checkboxes.values():
            if item.isChecked():
                self.result.appendPlainText(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())
