import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)

# Create main window
window = QWidget()

# Create horizontal layout
hbox = QHBoxLayout()

# Create vertical layout for buttons
vbox_buttons = QVBoxLayout()
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")
vbox_buttons.addWidget(button1)
vbox_buttons.addWidget(button2)
vbox_buttons.addWidget(button3)

# Create vertical layout for empty field
vbox_empty = QVBoxLayout()
empty_field = QWidget()
empty_field.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
empty_field.setMinimumWidth(200)
empty_field.setMinimumHeight(100)
vbox_empty.addWidget(empty_field)

# Add vertical layouts to horizontal layout
hbox.addLayout(vbox_buttons)
hbox.addLayout(vbox_empty)

# Set horizontal layout for main window
window.setLayout(hbox)

window.show()
sys.exit(app.exec_())
