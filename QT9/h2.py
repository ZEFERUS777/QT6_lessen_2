import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt, QPoint


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Машинка')
        self.setGeometry(100, 100, 300, 300)

        self.pixmap = QPixmap('car1.png')
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.car_images = ['car1.png', 'car2.png', 'car3.png']
        self.current_image_index = 0

        self.setMouseTracking(True)
        self.show()

    def mouseMoveEvent(self, event):
        cursor_pos = QCursor.pos()
        widget_pos = self.mapFromGlobal(cursor_pos)
        x, y = widget_pos.x(), widget_pos.y()

        # Ограничение движения машины внутри окна
        if x < 0:
            x = 0
        elif x > 250:
            x = 250

        if y < 0:
            y = 0
        elif y > 250:
            y = 250

        self.lbl.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.current_image_index = (self.current_image_index + 1) % len(self.car_images)
            self.pixmap = QPixmap(self.car_images[self.current_image_index])
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    sys.exit(app.exec())
