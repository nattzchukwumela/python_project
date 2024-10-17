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
folder = QPushButton('Select Folder')
img_list = QListWidget()
btn_left = QPushButton('left')
btn_right = QPushButton('right')
btn_mirror = QPushButton('mirror')

# class photoMill():
#     def __init__(self):
#         self.filename = None
#         self.original = None
#         self.image = None
#         self.save_folder = 'edits/'
#         self.save_filename = None

# Execute Code
main_window.setLayout()
main_window.show()
app.exec_()
