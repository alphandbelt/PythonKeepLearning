import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextBrowser, QWidget


class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Example")

        self.web_view = QWebEngineView()
        self.load_button = QPushButton("Load Website")
        self.load_button.clicked.connect(self.load_website)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.load_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_website(self):
        self.web_view.setUrl(QUrl("https://www.example.com"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebWindow()
    window.show()
    sys.exit(app.exec_())
