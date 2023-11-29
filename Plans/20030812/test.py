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

    def paintEvent(self, event):
        painter = QPainter(self)

        for firework in self.fireworks:
            firework.draw(painter)

    def updateFireworks(self):
        for firework in self.fireworks:
            firework.update()

        self.fireworks = [fw for fw in self.fireworks if not fw.isFinished()]
        self.repaint()

        if random.random() < 0.07:
            self.addRandomFirework()

    def addRandomFirework(self):
        choice = random.choice(
            ["heart", "star", "circle", "triangle", "square", "flower", "burst", "ring", "double_circle"])
        self.fireworks.append(Firework(self.width(), self.height(), choice))

    def drawHeart(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        path.moveTo(0, 0.3)
        path.cubicTo(-0.3, 0.75, -1, 0.5, 0, -1)
        path.cubicTo(1, 0.5, 0.3, 0.75, 0, 0.3)
        painter.fillPath(path, painter.brush())
        painter.restore()

    def drawStar(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        path.moveTo(0, -1)
        for _ in range(5):
            path.lineTo(math.cos(math.pi * 0.4) * 0.5, -math.sin(math.pi * 0.4) * 0.5)
            path.lineTo(0, -1)
            painter.rotate(72)
        path.closeSubpath()
        painter.fillPath(path, painter.brush())
        painter.restore()


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.uniform(1, 5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 5)
        self.gravity = 0.05
        self.alpha = 255

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
        self.y = random.randint(height // 4, height // 2)  # 烟花位置稍微提高
        self.color = QColor(
            random.randint(200, 255),
            random.randint(100, 200),
            random.randint(0, 100),
        )
        self.particles = []

        for _ in range(250):  # 增加粒子数量
            self.particles.append(Particle(self.x, self.y, self.color))

        self.shape = shape

    def draw(self, painter):
        for particle in self.particles:
            painter.setBrush(
                QBrush(QColor(particle.color.red(), particle.color.green(), particle.color.blue(), particle.alpha)))

            if self.shape == "heart":
                self.drawHeart(painter, particle.x, particle.y, particle.size)
            elif self.shape == "star":
                self.drawStar(painter, particle.x, particle.y, particle.size)
            elif self.shape == "flower":
                self.drawFlower(painter, particle.x, particle.y, particle.size)
            elif self.shape == "burst":
                self.drawBurst(painter, particle.x, particle.y, particle.size)
            elif self.shape == "ring":
                self.drawRing(painter, particle.x, particle.y, particle.size)
            elif self.shape == "double_circle":
                self.drawDoubleCircle(painter, particle.x, particle.y, particle.size)
            else:
                painter.drawEllipse(QPointF(particle.x, particle.y), particle.size / 2, particle.size / 2)

    def drawHeart(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        path.moveTo(0, 0.3)
        path.cubicTo(-0.3, 0.75, -1, 0.5, 0, -1)
        path.cubicTo(1, 0.5, 0.3, 0.75, 0, 0.3)
        painter.fillPath(path, painter.brush())
        painter.restore()

    def drawStar(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        path.moveTo(0, -1)
        for _ in range(5):
            path.lineTo(math.cos(math.pi * 0.4) * 0.5, -math.sin(math.pi * 0.4) * 0.5)
            path.lineTo(0, -1)
            painter.rotate(72)
        path.closeSubpath()
        painter.fillPath(path, painter.brush())
        painter.restore()

    def drawFlower(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        # ... 绘制花瓣 ...
        painter.fillPath(path, painter.brush())
        painter.restore()

    def drawBurst(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        # ... 绘制爆炸 ...
        painter.fillPath(path, painter.brush())
        painter.restore()

    def drawRing(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        # ... 绘制环 ...
        painter.strokePath(path, painter.pen())
        painter.restore()

    def drawDoubleCircle(self, painter, x, y, size):
        painter.save()
        painter.translate(x, y)
        painter.scale(size, size)
        path = QPainterPath()
        path.addEllipse(-0.6, -0.6, 1.2, 1.2)
        path.addEllipse(-0.3, -0.3, 0.6, 0.6)
        painter.strokePath(path, painter.pen())
        painter.restore()

    def update(self):
        for particle in self.particles:
            particle.update()

    def isFinished(self):
        return all(particle.isFinished() for particle in self.particles)


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
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
