import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MultimediaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multimedia Example")

        self.media_player = QMediaPlayer()
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_audio)

        layout = QVBoxLayout()
        layout.addWidget(self.play_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def play_audio(self):
        media_content = QMediaContent.fromUrl(QUrl.fromLocalFile("./audio.mp3"))
        self.media_player.setMedia(media_content)
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultimediaWindow()
    window.show()
    sys.exit(app.exec_())
