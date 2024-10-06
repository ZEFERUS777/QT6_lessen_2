import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QButtonGroup, QRadioButton, QPushButton, QHBoxLayout
)


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый флаг")
        self.layout = QHBoxLayout(self)
        self.btn_1_lay = QVBoxLayout(self)
        self.btn_2_lay = QVBoxLayout(self)
        self.btn_3_lay = QVBoxLayout(self)
        self.layout.addLayout(self.btn_1_lay)
        self.layout.addLayout(self.btn_2_lay)
        self.layout.addLayout(self.btn_3_lay)

        self.color_group_1 = QButtonGroup(self)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_3 = QButtonGroup(self)

        colors = ['Красный', 'Синий', 'Зеленый']
        self.btn_1_lay.addWidget(QLabel("Цвет №1"))
        self.btn_2_lay.addWidget(QLabel("Цвет №2"))
        self.btn_3_lay.addWidget(QLabel("Цвет №3"))
        for i, color in enumerate(colors):
            rb = QRadioButton(color)
            self.color_group_1.addButton(rb, i)
            self.btn_1_lay.addWidget(rb)

        for i, color in enumerate(colors):
            rb = QRadioButton(color)
            self.color_group_2.addButton(rb, i)
            self.btn_2_lay.addWidget(rb)

        for i, color in enumerate(colors):
            rb = QRadioButton(color)
            self.color_group_3.addButton(rb, i)
            self.btn_3_lay.addWidget(rb)

        self.make_flag = QPushButton("Создать флаг")
        self.make_flag.clicked.connect(self.show_result)
        self.result = QLabel(self)
        self.layout.addWidget(self.make_flag)

        self.btn_1_lay.setContentsMargins(0, 10, 10, 0)
        self.btn_2_lay.setContentsMargins(0, 10, 10, 0)
        self.btn_3_lay.setContentsMargins(0, 10, 10, 0)

        self.result = QLabel(self)
        self.result.move(10, 150)
        self.result.setMaximumSize(400, 200)

        self.btn_1_lay.addWidget(QLabel('\t', self))
        self.btn_2_lay.addWidget(QLabel('\t', self))
        self.btn_3_lay.addWidget(QLabel('\t', self))

        self.setFixedSize(400, 200)

    def show_result(self):
        color_1 = self.color_group_1.checkedButton().text() if self.color_group_1.checkedButton() else 'Не выбрано'
        color_2 = self.color_group_2.checkedButton().text() if self.color_group_2.checkedButton() else 'Не выбрано'
        color_3 = self.color_group_3.checkedButton().text() if self.color_group_3.checkedButton() else 'Не выбрано'

        result_text = f"Цвета: {color_1}, {color_2} и {color_3}"
        self.result.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlagMaker()
    window.show()
    sys.exit(app.exec())
