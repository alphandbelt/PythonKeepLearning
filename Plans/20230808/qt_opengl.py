import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

class OpenGLWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenGL Example")

        self.gl_widget = GLWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.gl_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class GLWidget(QGLWidget):
    def __init__(self):
        super().__init__()
        self.rotation = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(20)

    def initializeGL(self):
        pass

    def resizeGL(self, width, height):
        pass

    def paintGL(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 0, 0))

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        painter.setWindow(-50, -50, 100, 100)

        painter.rotate(self.rotation)
        painter.drawRect(-10, -10, 20, 20)

    def update_rotation(self):
        self.rotation += 1
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpenGLWindow()
    window.show()
    sys.exit(app.exec_())
