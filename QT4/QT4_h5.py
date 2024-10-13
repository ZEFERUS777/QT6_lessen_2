from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QPushButton
import sys


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 260)
        self.setWindowTitle('File statistic')
        self.read_file_name = QLabel('Имя файла', self)
        self.read_file_name.move(10, 10)
        self.filenameEdit = QLineEdit(self)
        self.filenameEdit.move(90, 13)
        self.filenameEdit.resize(100, 23)
        self.button = QPushButton('Рассчитать', self)
        self.button.move(210, 15)
        self.button.resize(100, 23)
        self.max_val_lbl = QLabel('Максимальное значение:', self)
        self.max_val_lbl.move(10, 50)
        self.max_val_lbl.adjustSize()
        self.maxEdit = QLineEdit(self)
        self.maxEdit.move(self.max_val_lbl.x() + self.max_val_lbl.width() + 15, 45)
        self.maxEdit.resize(100, 23)
        self.min_val_lbl = QLabel('Минимальное значение:', self)
        self.min_val_lbl.move(self.max_val_lbl.x(), self.max_val_lbl.y() + self.max_val_lbl.height() + 10)
        self.min_val_lbl.adjustSize()
        self.minEdit = QLineEdit(self)
        self.minEdit.move(self.maxEdit.x(), self.maxEdit.y() + self.maxEdit.height() + 10)
        self.minEdit.resize(100, 23)
        self.avg_val_lbl = QLabel('Среднее значение:', self)
        self.avg_val_lbl.move(self.min_val_lbl.x(), self.min_val_lbl.y() + self.min_val_lbl.height() + 10)
        self.avg_val_lbl.adjustSize()
        self.avgEdit = QLineEdit(self)
        self.avgEdit.move(self.minEdit.x(), self.minEdit.y() + self.minEdit.height() + 10)
        self.avgEdit.resize(100, 23)
        self.statusBar = self.statusBar()
        self.statusBar.move(10, 95)
        self.button.clicked.connect(self.calculate_stats)

    def calculate_stats(self):
        filename = self.filenameEdit.text().strip()
        try:
            with open(filename, 'r') as file:
                numbers = [int(num) for num in file.read().split() if num.strip().isdigit()]
                if not numbers:
                    self.statusbar.showMessage("Указанный файл пуст")
                    self.minEdit.setText("0")
                    self.maxEdit.setText("0.00")
                    self.avgEdit.setText("0.00")
                else:
                    self.minEdit.setText(f"{min(numbers)}")
                    self.maxEdit.setText(f"{max(numbers)}")
                    average = sum(numbers) / len(numbers)
                    self.avgEdit.setText(f"{average:.2f}")

                    with open('out.txt', 'w', encoding='utf-8') as output_file:
                        output_file.write(f"Максимальное значение = {max(numbers)}\n")
                        output_file.write(f"Минимальное значение = {min(numbers)}\n")
                        output_file.write(f"Среднее значение = {average:.2f}\n")

        except FileNotFoundError:
            self.statusbar.showMessage("Указанный файл не существует")
            self.minEdit.setText("0")
            self.maxEdit.setText("0")
            self.avgEdit.setText("0.00")
        except ValueError:
            self.statusbar.showMessage("Файл содержит некорректные данные")
            self.minEdit.setText("Min Value: ")
            self.maxEdit.setText("Max Value: ")
            self.avgEdit.setText("Average Value: ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileStat()
    window.show()
    sys.exit(app.exec())
