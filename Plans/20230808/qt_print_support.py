import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class PrintWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt打印示例")

        self.text_edit = QTextEdit()
        self.print_button = QPushButton("打印")
        self.print_button.clicked.connect(self.print_document)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.print_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def print_document(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.text_edit.print(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PrintWindow()
    window.show()

    sys.exit(app.exec_())
