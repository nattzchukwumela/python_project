import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        buttons = [
            "Button (0,0)", "Button (0,1)", "Button (0,2)",
            "Button (1,0)", "Button (1,1)", "Button (1,2)",
            "Button (2,0)", "Button (2,1)", "Button (2,2)"
        ]

        row = 0
        col = 0

        for button_text in buttons:
            button = QPushButton(button_text)
            grid.addWidget(button, row, col)

            col += 1
            if col > 2:
                col = 0
                row += 1

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QGridLayout')
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
