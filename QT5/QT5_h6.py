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
        self.repaint()

    def paintEvent(self, event):
        if self.painted:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            coords = [
                (150, 150),
                (350, 150),
                (350, 350),
                (150, 350)
            ]
            n = int(self.n.text())
            k = float(self.k.text())
            for _ in range(n):
                polygon = QPolygonF()
                for point in coords:
                    polygon.append(QPointF(point[0], point[1]))
                qp.drawPolygon(polygon)
                new_coords = []
                for i in range(len(coords)):
                    point = (
                        k * coords[i][0] + (1 - k) * coords[(i + 1) % len(coords)][0],
                        k * coords[i][1] + (1 - k) * coords[(i + 1) % len(coords)][1]
                    )
                    new_coords.append(point)
                coords = new_coords
            qp.end()
            self.painted = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Square2()
    window.show()
    sys.exit(app.exec())
