import sys

from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton,  QWidget
class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt加载网站示例")

        self.web_view = QWebEngineView()
        self.load_button = QPushButton("加载网站")
        self.load_button.clicked.connect(self.load_website)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.load_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def load_website(self):
        self.web_view.setUrl(QtCore.QUrl("https://www.google.com"))  # 使用QtCore.QUrl导入

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WebWindow()
    window.show()

    sys.exit(app.exec_())  #！！！ 重要 卡死
