import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit


class MyNotes(QWidget):
    def __init__(self):
        super(MyNotes, self).__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('My Notes')

        self.contac_name = QLabel(self)
        self.contac_name.setText('Имя')
        self.contac_name.move(20, 40)

        self.contac_phone = QLabel(self)
        self.contac_phone.setText('Телефон')
        self.contac_phone.move(20, 80)

        self.contactName = QLineEdit(self)
        self.contactName.move(130, 40)
        self.contactName.resize(200, 30)

        self.contactNumber = QLineEdit(self)
        self.contactNumber.move(130, 80)
        self.contactNumber.resize(200, 30)

        self.contactList = QListWidget(self)
        self.contactList.move(20, 125)
        self.contactList.resize(300, 200)

        self.addContactBtn = QPushButton('Добавить', self)
        self.addContactBtn.move(350, 61)
        self.addContactBtn.clicked.connect(self.addContact)

    def addContact(self):
        name = self.contactName.text()
        phone = self.contactNumber.text()
        self.contactList.addItem(f'{name} {phone}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyNotes()
    window.show()
    sys.exit(app.exec())
