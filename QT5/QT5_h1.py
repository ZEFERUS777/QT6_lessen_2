import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog, QApplication, QButtonGroup, QPushButton, QHBoxLayout, \
    QVBoxLayout


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)

        self.file = QFileDialog()
        self.file.adjustSize()  # to fit the window
        self.curr_image = QImage(self.file.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")[0])
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.resized_pix = self.pixmap.scaled(280, 270)
        self.lbl_image = QLabel(self)
        self.lbl_image.setPixmap(self.resized_pix)
        self.channelButtons = QButtonGroup(self)
        self.red_color_btn = QPushButton("R", self)
        self.green_color_btn = QPushButton("G", self)
        self.blue_color_btn = QPushButton("B", self)

        self.channelButtons.addButton(self.red_color_btn)
        self.channelButtons.addButton(self.green_color_btn)
        self.channelButtons.addButton(self.blue_color_btn)

        self.red_color_btn.move(10, 50)
        self.green_color_btn.move(10, self.red_color_btn.y() + self.red_color_btn.height() + 50)
        self.blue_color_btn.move(10, self.green_color_btn.y() + self.green_color_btn.height() + 50)

        self.red_color_btn.resize(150, 25)
        self.green_color_btn.resize(150, 25)
        self.blue_color_btn.resize(150, 25)

        self.lbl_image.move(self.red_color_btn.x() + 200, self.red_color_btn.y() - 20)
        self.lbl_image.resize(280, 270)

        self.rotateButtons = QButtonGroup(self)

        self.rotate_btn = QPushButton("По часовой стрелке", self)
        self.rotate_btn.resize(200, 25)
        self.rotateButtons.addButton(self.rotate_btn)

        self.rotate_btn.move(10, self.green_color_btn.y() + self.green_color_btn.height() + 180)

        self.rotate_2_btn = QPushButton("Против часовой стрелке", self)
        self.rotate_2_btn.resize(200, 25)
        self.rotateButtons.addButton(self.rotate_2_btn)
        self.rotate_2_btn.move(self.rotate_btn.x() + self.rotate_btn.width() + 10, self.rotate_btn.y())

        self.red_color_btn.clicked.connect(lambda checked, c='red': self.change_channel(c))
        self.green_color_btn.clicked.connect(lambda: self.change_channel(Qt.GlobalColor.green))
        self.blue_color_btn.clicked.connect(lambda: self.change_channel(Qt.GlobalColor.blue))

    def change_channel(self, color):
        if self.curr_image:
            img = self.curr_image.copy()
            for c in [Qt.GlobalColor.red, Qt.GlobalColor.green, Qt.GlobalColor.blue]:
                img.setColor(c, 0 if c != color else 255)
            self.curr_image = img
            self.update_image()

    def update_image(self):
        if self.curr_image:
            pixmap = QPixmap.fromImage(self.curr_image)
            self.lbl_image.setPixmap(pixmap.scaled(self.lbl_image.size(), Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyPillow()
    window.show()
    sys.exit(app.exec())

