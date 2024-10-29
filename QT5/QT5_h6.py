import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QPushButton


class Square2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.k_lbl = QLabel('K =', self)
        self.k_lbl.move(20, 25)

        self.k = QLineEdit(self)
        self.k.move(self.k_lbl.x() + 25, self.k_lbl.y() + 3)
        self.k.resize(100, 23)

        self.n_lbl = QLabel('N =', self)
        self.n_lbl.move(self.k.x() + self.k.width() + 10, self.k_lbl.y())

        self.n = QLineEdit(self)
        self.n.move(self.n_lbl.x() + 25, self.n_lbl.y() + 3)
        self.n.resize(100, 23)

        self.a = 200
        self.coords = 150, 150

        self.draw = QPushButton('Рисовать', self)
        self.draw.move(self.n.x() + self.n.width() + 10, self.n_lbl.y())

        self.painted = False

        self.draw.clicked.connect(self.paint)

        self.color = QColor(255, 0, 0)

    def paint(self):
        self.painted = True
        self.update()

    def paintEvent(self, event):
        if self.painted:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_polygons(qp)
            qp.end()

    def draw_polygons(self, qp):
        self.koff = float(self.k.text()) if self.k.text() else 0.8
        self.rang = int(self.n.text()) if self.n.text() else 20
        polygons = []
        # Квадрат
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Square2()
    window.show()
    sys.exit(app.exec())
