from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QMouseEvent, QAction, QKeyEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys


class BrushPoint:
    def __init__(self, x, y):
        self.x, self.y = int(x), int(y)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 255)))
        painter.setPen(QColor(0, 0, 255))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)


class Line:
    def __init__(self, sx, sy, ex, ey):
        self.sx = int(sx)
        self.sy = int(sy)
        self.ex = int(ex)
        self.ey = int(ey)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 255)))
        painter.setPen(QColor(0, 0, 255))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:
    def __init__(self, cx, cy, x, y):
        self.cx, self.cy = int(cx), int(cy)
        self.x, self.y = int(x), int(y)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
        painter.setPen(QColor(0, 0, 255))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, radius * 2, radius * 2)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []
        self.tool = 'brush'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        if self.tool == "brush":
            self.objects.append(BrushPoint(event.position().x(), event.position().y()))
        elif self.tool == "line":
            self.objects.append(
                Line(event.position().x(), event.position().y(), event.position().x(), event.position().y()))
        elif self.tool == "circle":
            self.objects.append(
                Circle(event.position().x(), event.position().y(), event.position().x(), event.position().y()))
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.tool == "brush":
            self.objects.append(BrushPoint(event.position().x(), event.position().y()))
        elif self.tool == "line":
            self.objects[-1].ex = int(event.position().x())
            self.objects[-1].ey = int(event.position().y())
        elif self.tool == "circle":
            self.objects[-1].x = int(event.position().x())
            self.objects[-1].y = int(event.position().y())
        self.update()

    def setBrush(self):
        self.tool = 'brush'

    def setLine(self):
        self.tool = 'line'

    def setCircle(self):
        self.tool = 'circle'

    def clear(self):
        self.objects = []
        self.update()


class Paint(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('paint.ui', self)
        self.setCentralWidget(Canvas())

        self.action_brush: QAction
        self.action_line: QAction
        self.action_circle: QAction

        self.action_brush.triggered.connect(self.centralWidget().setBrush)
        self.action_line.triggered.connect(self.centralWidget().setLine)
        self.action_circle.triggered.connect(self.centralWidget().setCircle)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.centralWidget().clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Paint()
    ex.show()
    sys.exit(app.exec())
