import sys

from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.coord = []
        self.setGeometry(300, 300, 800, 900)
        self.btn = QPushButton('Показать', self)
        self.btn.move(15, 15)

        self.a = 300  # Size of the side of the largest square
        self.k = 0.9  # Scaling factor
        self.n = 10  # Number of repetitions

        self.lbl_s = QLabel('Side:', self)
        self.lbl_s.move(self.btn.x() + self.btn.width() + 70, self.btn.y())
        self.coeff_lbl = QLabel('Coeff:', self)
        self.coeff_lbl.move(self.lbl_s.x(), self.lbl_s.y() + 30)
        self.n_lbl = QLabel('N', self)
        self.n_lbl.move(self.coeff_lbl.x(), self.coeff_lbl.y() + 30)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(self.lbl_s.x() + 40, self.lbl_s.y())
        self.lineEdit.resize(100, 25)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.move(self.lineEdit.x(), self.coeff_lbl.y())
        self.lineEdit_2.resize(100, 25)

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.move(self.lineEdit.x(), self.n_lbl.y())
        self.lineEdit_3.resize(100, 25)
        self.color = QColor(255, 255, 255)

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_square(self.qp)
            self.qp.end()

    def draw_square(self, qp: QPainter):
        self.a = int(self.lineEdit.text()) if self.lineEdit.text() else 300
        self.k = float(self.lineEdit_2.text()) if self.lineEdit_2.text() else 0.9
        self.n = int(self.lineEdit_3.text()) if self.lineEdit_3.text() else 10
        color = QColor(255, 0, 0)
        xs = 50
        self.coords = xs, 130
        self.qp.setBrush(QColor(0, 0, 0))
        self.qp.setPen(color)
        rectangle_center = None
        count = 0
        for i in range(self.n):
            if count == 0:
                rectangle = QRectF(self.coords[0], self.coords[1], self.a, self.a)
                rectangle_center = rectangle.center()
                qp.drawRect(rectangle)
                count += 1
                self.a = self.a * self.k
            else:
                rectangle = QRectF(rectangle_center.x() - self.a / 2, rectangle_center.y() - self.a / 2,
                                   self.a, self.a)
                qp.drawRect(rectangle)
                self.a = self.a * self.k


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Square1()
    window.show()
    sys.exit(app.exec())
