
import sys
from PyQt5.QtCore import QCoreApplication, QTimer
import time
def timer_callback():
    print("Timer ticked!",time.time())

if __name__ == "__main__":

    # sys.argv 输入的参数

    app = QCoreApplication(sys.argv)

    timer = QTimer() # 实例化

    timer.timeout.connect(timer_callback)
    timer.start(1000)  # 1000 milliseconds (1 second)

    # 程序的退出
    sys.exit(app.exec_())

