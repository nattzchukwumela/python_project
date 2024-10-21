from fileinput import filename

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QFileDialog, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from functools import partial
from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageEnhance, ImageFilter
from module import btn_style, img_ext

# Initialise App
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('photo mill')
main_window.resize(1000, 600)

# Create Layout / App Widgets & Designs
# function buttons 🡓
folder = QPushButton('Select Folder')
img_list = QListWidget()

# Image Box
img_box = QLabel('Image will appear here')
img_box.setStyleSheet('text-align: center; border-style: solid; border-color: blue; border-width: 2px; color: green; font-size: 32px;')
img_box.setAlignment(Qt.AlignCenter)

class PhotoMill:
    def __init__(self):
        self.filename = None
        self.original = None
        self.image = None
        self.save_folder = 'edits/'
        self.save_filename = None

    def load_image(self, file_name):
        self.filename = file_name
        fullname = os.path.join(img_directory, file_name)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_img(self):
        path = os.path.join(img_directory, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        file_name = os.path.join(path, self.filename)
        self.image.save(file_name)

    def show_image(self, path):
        img_box.hide()
        display_img = QPixmap(path)
        width, height = img_box.width(), img_box.height()
        display_img.scaled(width, height, Qt.KeepAspectRatio)
        img_box.setPixmap(display_img)
        img_box.show()

    def original_img(self, path):
        image = QPixmap(path)
        w, h = img_box.width(), img_box.height()
        image.scaled(w, h, Qt.KeepAspectRatio)
        img_box.setPixmap(self.original)
        img_box.show()

    def edit_img(self, transformation):
        """
           'left', 'right', 'mirror',
    'contrast', 'sharpen', 'color',
    'saturation', 'blur', 'grey'
        """
        transformations = {
            'left': lambda image: image.transpose(Image.ROTATE_90),
            'right': lambda image: image.transpose(Image.ROTATE_270),
            'mirror': lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
            'sharpen': lambda image: image.filter(ImageFilter.SHARPEN),
            'saturation': lambda image: ImageEnhance.Color(image).enhance(1.2),
            'blur': lambda image: image.filter(ImageFilter.BLUR),
            'grey': lambda image: image.convert('L'),
            'contrast': lambda image: ImageEnhance.Contrast(image).enhance(1.2),
            'original': lambda : self.original_img()
        }
        get_transform = transformations.get(transformation)
        if get_transform:
            self.image = get_transform(self.image)
            self.save_img()
            img_path = os.path.join(img_directory, self.save_folder, self.filename)
            self.show_image(img_path)


# Layout Containers
main_layout = QVBoxLayout()
grid = QGridLayout()
img_container = QHBoxLayout()
container1 = QHBoxLayout()
img_list_con = QVBoxLayout()
buttons = [
    'left', 'right', 'mirror',
    'contrast', 'sharpen', 'original',
    'saturation', 'blur', 'grey'
]
row = 0
col = 0

btn_styles = ""
for key, value in btn_style.items():
    btn_styles += f"{key}: {value};"
for button_text in buttons:
    button = QPushButton(button_text)
    button.setStyleSheet(btn_styles)
    button.clicked.connect(lambda: main.edit_img(button.sender().text()))
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
img_directory = ""
def filter_img(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results

# get working directory for images
def get_work_directory():
    global img_directory
    img_directory = QFileDialog.getExistingDirectory()
    if img_directory:
        img_names = filter_img(os.listdir(img_directory), img_ext)
        img_list.clear()
        for imgName in img_names:
            img_list.addItem(imgName)

def display_image():
  global img_directory
  if img_list.currentRow() >= 0:
      file_name = img_list.currentItem().text()
      main.load_image(file_name)
      main.show_image(os.path.join(img_directory, main.filename))

main = PhotoMill()



print(buttons)
# for button in buttons:
#     button_text = button.text()
#     button.clicked.connect(popup_message)

# button events
folder.clicked.connect(get_work_directory)
img_list.currentRowChanged.connect(display_image)
# managing layouts
main_layout.addLayout(img_container, 80)
main_layout.addLayout(container1, 20)
main_window.setLayout(main_layout)

# Execute App
main_window.show()
app.exec_()
