import sys
from PyQt6 import uic
from PyQt6.QtGui import QBrush, QColor, QPainter, QMouseEvent, QAction, QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget


class BrushPoint:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)


class Line:
    def __init__(self, sx, sy, ex, ey):
        self.sx = int(sx)
        self.sy = int(sy)
        self.ex = int(ex)
        self.ey = int(ey)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:
    def __init__(self, cx, cy, x, y):
        self.cx = int(cx)
        self.cy = int(cy)
        self.x = int(x)
        self.y = int(y)

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
        painter.setPen(QColor(0, 0, 0))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, 2 * radius, 2 * radius)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []
        self.instrument = 'brush'

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        if self.instrument == "brush":
            self.objects.append(BrushPoint(event.position().x(), event.position().y()))
        elif self.instrument == "line":
            self.objects.append(
                Line(event.position().x(), event.position().y(), event.position().x(), event.position().y()))
        elif self.instrument == "circle":
            self.objects.append(
                Circle(event.position().x(), event.position().y(), event.position().x(), event.position().y()))
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.instrument == "brush":
            self.objects.append(BrushPoint(event.position().x(), event.position().y()))
        elif self.instrument == "line":
            self.objects[-1].ex = int(event.position().x())
            self.objects[-1].ey = int(event.position().y())
        elif self.instrument == "circle":
            self.objects[-1].x = int(event.position().x())
            self.objects[-1].y = int(event.position().y())
        self.update()

    def setBrush(self):
        self.instrument = 'brush'

    def setLine(self):
        self.instrument = 'line'

    def setCircle(self):
        self.instrument = "circle"

    def clean(self):
        self.objects = []
        self.update()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.uip', self)
        self.setCentralWidget(Canvas())
        self.actionbrush: QAction
        self.actionline: QAction
        self.actioncircle: QAction
        self.actionbrush.triggered.connect(self.centralWidget().setBrush)
        self.actionline.triggered.connect(self.centralWidget().setLine)
        self.actioncircle.triggered.connect(self.centralWidget().setCircle)

    def keyPressEvent(self, event: QKeyEvent):
        if event.text() == ' ':
            self.centralWidget().clean()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
