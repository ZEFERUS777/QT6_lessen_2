import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QPushButton


class Square2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.k_lbl = QLabel('K =', self)
        self.k_lbl.move(20, 10)

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
            k_value = float(self.k.text()) if self.k.text() else 1
            n_value = int(self.n.text()) if self.n.text().isdigit() else 0
            if k_value < 1 and n_value > 0:
                self.draw_polygons(k_value, n_value)

    def draw_polygons(self, k_value, n_value):
        base_size = 200
        center = QPointF(150, 150)

        def create_square(center, size):
            half_size = size / 2
            return QPolygonF([QPointF(center.x() - half_size, center.y() - half_size),
                              QPointF(center.x() + half_size, center.y() - half_size),
                              QPointF(center.x() + half_size, center.y() + half_size),
                              QPointF(center.x() - half_size, center.y() + half_size)])

        painter = QPainter(self)
        painter.setPen(self.color)

        size = base_size
        for _ in range(n_value):
            square = create_square(center, size)
            painter.drawPolygon(square)
            size *= k_value
            center = QPointF(center.x(), center.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Square2()
    window.show()
    sys.exit(app.exec())
