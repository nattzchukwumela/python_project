from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QFileDialog, QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageEnhance, ImageFilter
from module import btn_style, img_ext

# Initialise App
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('photomill')
main_window.resize(1000, 600)

# Create Layout / App Widgets & Designs
# function buttons 🡓
folder = QPushButton('Select Folder')
img_list = QListWidget()

# Image Box
img_box = QLabel('Image will appear here')
img_box.setStyleSheet('text-align: center; border-style: solid; border-color: blue; border-width: 2px; color: green; font-size: 32px;')
img_box.setAlignment(Qt.AlignCenter)

# Layout Containers
main_layout = QVBoxLayout()
grid = QGridLayout()
img_container = QHBoxLayout()
container1 = QHBoxLayout()
img_list_con = QVBoxLayout()
buttons = [
    'left', 'right', 'mirror',
    'contrast', 'sharpness', 'color',
    'sharpen', 'blur', 'grey'
]
row = 0
col = 0

btn_styles = ""
for key, value in btn_style.items():
    btn_styles += f"{key}: {value};"
for button_text in buttons:
    button = QPushButton(button_text)
    button.setStyleSheet(btn_styles)
    grid.addWidget(button, row, col)

    col += 1
    if col > 2:
        col = 0
        row += 1

# layout spacings
grid.setContentsMargins(5, 10, 5, 10)

#layout widgets
img_container.addWidget(img_box)
img_list_con.addWidget(folder)
img_list_con.addWidget(img_list)
container1.addLayout(grid, 70)
container1.addLayout(img_list_con, 30)

# getting directory functionality
imgDirectory = ""
def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results

# get working directory for images
def getWorkDirectory():
    global imgDirectory
    imgSelectedDirectory = QFileDialog.getExistingDirectory()
    imgNames = filter(os.listdir(imgSelectedDirectory), img_ext)
    img_list.clear()
    for imgName in imgNames:
        img_list.addItem(imgName)


class photoMill():
    def __init__(self):
        self.filename = None
        self.original = None
        self.image = None
        self.save_folder = 'edits/'
        self.save_filename = None

folder.clicked.connect(getWorkDirectory)
main_layout.addLayout(img_container, 80)
main_layout.addLayout(container1, 20)
# Execute Code
main_window.setLayout(main_layout)
main_window.show()
app.exec_()
