from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
import sys
import csv


class OlympResult(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 500)
        self.loadData('rez.csv')
        self.classes = QComboBox(self)
        self.classes.setGeometry(10, 10, 200, 20)
        self.classes.addItem('Все')
        self.classes.addItems(self.clas)

        self.schools = QComboBox(self)
        self.schools.setGeometry(self.classes.x() + self.classes.width() + 10, 10, 200, 20)
        self.schools.addItem('Все')

        self.resultButton = QPushButton('Узнать результаты', self)
        self.resultButton.adjustSize()
        self.resultButton.move(self.schools.x() + self.schools.width() + 10, self.schools.y())

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(10, self.schools.y() + self.schools.height() + 10)
        self.tableWidget.resize(600, 400)

        self.resultButton.clicked.connect(self.filterResults)

    def loadData(self, filename):
        self.data = []
        schools_set = set()
        classes_set = set()

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Пропустить заголовок

            for row in reader:
                self.data.append(row)
                school_class = row[2].split('-')[2:4]
                schools_set.add(school_class[0])
                classes_set.add(school_class[1])

        self.schools.addItems(sorted(schools_set))
        self.classes.addItems(sorted(classes_set))
        self.displayResults(self.data)

    def displayResults(self, data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for row_idx, row in enumerate(data):
            for col_idx, item in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(item))

    def filterResults(self):
        selected_school = self.schools.currentText()
        selected_class = self.classes.currentText()

        filtered_data = []
        for row in self.data:
            login = row[2]
            school_num, class_num = login.split('-')[2:4]
            if (selected_school == "" or school_num == selected_school) and \
                    (selected_class == "" or class_num == selected_class):
                filtered_data.append(row)

        self.displayResults(filtered_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OlympResult()
    window.show()
    sys.exit(app.exec())
