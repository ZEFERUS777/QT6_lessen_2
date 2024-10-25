import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QListWidget, QInputDialog


class administrator_LMS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Admin_LMS')
        self.setWindowIcon(QIcon('widget_icon.png'))
        self.unit_name = QLabel('Имя ученика:', self)
        self.unit_name.move(20, 20)

        self.name_mug = QLabel('Название кружка:', self)
        self.name_mug.move(self.unit_name.x(), self.unit_name.y() + self.unit_name.height())

        self.unit_name_input = QLineEdit(self)
        self.unit_name_input.setPlaceholderText('Имя ученика')
        self.unit_name_input.resize(100, 23)
        self.unit_name_input.move(self.name_mug.x() + self.name_mug.width() + 10, self.unit_name.y() + 5)

        self.name_mug_input = QLineEdit(self)
        self.name_mug_input.setPlaceholderText('Название кружка')
        self.name_mug_input.resize(100, 23)
        self.name_mug_input.move(self.unit_name_input.x(), self.name_mug.y() + 5)

        self.add_unit = QPushButton('Добавить ученика', self)
        self.add_unit.move(300, 23)
        self.add_unit.adjustSize()

        self.save_all_units_btn = QPushButton('Сохранить всё в файл', self)
        self.save_all_units_btn.move(self.add_unit.x(), self.add_unit.y() + 10 + self.add_unit.height())
        self.save_all_units_btn.adjustSize()
        self.add_unit.resize(self.save_all_units_btn.width(), self.save_all_units_btn.height())

        self.units_list = []

        self.units_list_ui = QListWidget(self)
        self.units_list_ui.move(self.save_all_units_btn.x(),
                                self.save_all_units_btn.y() + 10 + self.save_all_units_btn.height())
        self.units_list_ui.resize(self.save_all_units_btn.width(), self.save_all_units_btn.height())

        self.add_unit.clicked.connect(self.add_unit_to_list)
        self.save_all_units_btn.clicked.connect(self.save_all_units)

    def add_unit_to_list(self):
        try:
            self.units_list_ui.addItem(f'{self.unit_name_input.text()}: {self.name_mug_input.text()}')
            self.units_list_ui.resize(self.save_all_units_btn.width(), self.units_list_ui.height() + 15)
            self.units_list.append(f'{self.unit_name_input.text()} {self.name_mug_input.text()}')
        except ValueError:
            print('Необходимо ввести имя ученика и название кружка')

    def save_all_units(self):
        file_name, ok_pressed = QInputDialog.getText(self, 'Сохранить', 'Введите имя файла')
        if ok_pressed:
            with open(file_name + '.txt', 'w', encoding='utf-8') as file:
                for unit in self.units_list:
                    unit = unit.split(' ')
                    file.write(f'Имя ученика: {unit[0]} Название кружка: {unit[1]}\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = administrator_LMS()
    window.show()
    sys.exit(app.exec())
