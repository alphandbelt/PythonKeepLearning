import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def button_click():
    print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)



    window = QWidget()

    button = QPushButton("点击一下", window)
    button.clicked.connect(button_click)
    window.show()

    sys.exit(app.exec_())
