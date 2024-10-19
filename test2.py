import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication(sys.argv)

# Create main window
window = QWidget()

# Create horizontal layout
hbox = QHBoxLayout()

# Create buttons
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")

# Add buttons to horizontal layout
hbox.addWidget(button1)
hbox.addWidget(button2)
hbox.addWidget(button3)

# Set horizontal layout for main window
window.setLayout(hbox)

window.show()
sys.exit(app.exec_())
