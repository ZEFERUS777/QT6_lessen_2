import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, \
    QGroupBox
from PyQt6.QtGui import QImage, QPixmap, QTransform
from PyQt6.QtCore import Qt


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyPillow")
        self.curr_image = None

        # Create layout
        main_layout = QVBoxLayout()
        self.central_widget = QLabel()
        main_layout.addWidget(self.central_widget)

        # Create channel buttons
        channel_buttons_layout = QHBoxLayout()
        channel_buttons_group = QGroupBox("channelButtons")
        red_button = QPushButton("Red")
        green_button = QPushButton("Green")
        blue_button = QPushButton("Blue")
        channel_buttons_layout.addWidget(red_button)
        channel_buttons_layout.addWidget(green_button)
        channel_buttons_layout.addWidget(blue_button)
        channel_buttons_group.setLayout(channel_buttons_layout)
        main_layout.addWidget(channel_buttons_group)

        # Create rotate buttons
        rotate_buttons_layout = QHBoxLayout()
        rotate_buttons_group = QGroupBox("rotateButtons")
        rotate_left_button = QPushButton("Left")
        rotate_right_button = QPushButton("Right")
        rotate_buttons_layout.addWidget(rotate_left_button)
        rotate_buttons_layout.addWidget(rotate_right_button)
        rotate_buttons_group.setLayout(rotate_buttons_layout)
        main_layout.addWidget(rotate_buttons_group)

        self.central_widget.setLayout(main_layout)

        # Connect button clicks to functions
        red_button.clicked.connect(self.show_red_channel)
        green_button.clicked.connect(self.show_green_channel)
        blue_button.clicked.connect(self.show_blue_channel)
        rotate_left_button.clicked.connect(self.rotate_left)
        rotate_right_button.clicked.connect(self.rotate_right)

        # Open file dialog to choose image
        self.load_image()

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.curr_image = QImage(file_path)
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image))

    def show_red_channel(self):
        if self.curr_image:
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image.createHeuristicMask()))

    def show_green_channel(self):
        if self.curr_image:
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image.createAlphaMask()))

    def show_blue_channel(self):
        if self.curr_image:
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image.createHeuristicMask()))

    def rotate_left(self):
        if self.curr_image:
            transform = QTransform()
            transform.rotate(-90)
            self.curr_image = self.curr_image.transformed(transform)
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image))

    def rotate_right(self):
        if self.curr_image:
            transform = QTransform()
            transform.rotate(90)
            self.curr_image = self.curr_image.transformed(transform)
            self.central_widget.setPixmap(QPixmap.fromImage(self.curr_image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPillow()
    window.show()
    sys.exit(app.exec())
