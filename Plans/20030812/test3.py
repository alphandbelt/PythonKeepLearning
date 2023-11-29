import sys
import math
import random
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPainter, QColor, QBrush, QPainterPath
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Fireworks(QWidget):
    def __init__(self):
        super().__init__()

        self.background_symbols = []  # 用于存储背景符号的列表
        self.fireworks = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFireworks)
        self.timer.start(1000 // 60)  # 60 FPS
        self.generateBackgroundSymbols()  # 生成背景符号

    def generateBackgroundSymbols(self):
        for _ in range(50):  # 背景中随机生成一些心形和五角星
            choice = random.choice(["heart", "star"])
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            self.background_symbols.append((choice, x, y))

    def paintEvent(self, event):
        painter = QPainter(self)

        for symbol in self.background_symbols:
            choice, x, y = symbol
            if choice == "heart":
                self.drawHeart(painter, x, y, 20)
            elif choice == "star":
                self.drawStar(painter, x, y, 20)

        for firework in self.fireworks:
            firework.draw(painter)

    def updateFireworks(self):
        for firework in self.fireworks:
            firework.update()

        self.fireworks = [fw for fw in self.fireworks if not fw.isFinished()]
        self.repaint()

        if random.random() < 0.1:
            self.addRandomFirework()

    def addRandomFirework(self):
        choice = random.choice(
            ["heart", "star", "circle", "triangle", "square", "flower", "burst", "ring", "double_circle"])
        if random.random() < 0.2:  # 20% 的概率选择心形
            choice = "heart"
        self.fireworks.append(Firework(self.width(), self.height(), choice))

        # # 播放音效
        # pygame.mixer.music.load("firework_sound.wav")  # 替换为您的音效文件路径
        # pygame.mixer.music.play()


class Particle:
    def __init__(self, x, y, color, shape="circle"):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.uniform(1, 5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 5)
        self.gravity = 0.05
        self.alpha = 255
        self.shape = shape

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed
        self.speed -= self.gravity
        self.alpha -= 5

    def isFinished(self):
        return self.alpha <= 0


class Firework:
    def __init__(self, width, height, shape):
        self.x = random.randint(0, width)
        self.y = random.randint(height // 4, height // 2)  # 调整烟花位置
        self.color = QColor(
            random.randint(200, 255),
            random.randint(100, 200),
            random.randint(0, 100),
        )
        self.particles = []

        for _ in range(250):  # 增加粒子数量
            self.particles.append(Particle(self.x, self.y, self.color, "heart"))  # 生成心形粒子

        self.shape = shape

    def draw(self, painter):
        for particle in self.particles:
            painter.setBrush(
                QBrush(QColor(particle.color.red(), particle.color.green(), particle.color.blue(), particle.alpha)))

            self.drawHeart(painter, particle.x, particle.y, particle.size)  # 使用心形绘制粒子

    # ... (与之前代码相同)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fireworks with Various Shapes")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = Fireworks()
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: pink;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # pygame.mixer.init()  # 初始化音效
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
