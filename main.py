from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageEnhance, ImageFilter

# Initialise App
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('photomill')
main_window.resize(1000, 600)

# Create Layout / App Widgets & Designs
# function buttons 🡓
folder = QPushButton('Select Folder')
img_list = QListWidget()
btn_left = QPushButton('left')
btn_right = QPushButton('right')
btn_mirror = QPushButton('mirror')
btn_sharpness = QPushButton('sharpness')
btn_grey = QPushButton('b/w')
btn_contrast = QPushButton('contrast')
btn_blur = QPushButton('blur')
btn_color = QPushButton('color')
btn_brightness = QPushButton('brightness')


main_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

# create first row layout
row1.addWidget(img_list)
row1.addWidget(folder)
row1.addWidget(btn_left)
row1.addWidget(btn_right)
row1.addWidget(btn_mirror)
row1.addWidget(btn_blur)
row1.addWidget(btn_contrast)
row1.addWidget(btn_sharpness)
row1.addWidget(btn_brightness)

# Create Layout Format
main_layout.addLayout(row2, 80)
main_layout.addLayout(row1, 20)

# Execute Code
main_window.setLayout(main_layout)
main_window.show()
app.exec_()
