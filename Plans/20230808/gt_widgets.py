import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

def calculate():
    num1 = int(line_edit1.text())
    num2 = int(line_edit2.text())
    result = num1 + num2
    result_label.setText(f"计算加法的结果: {result}")

if __name__ == "__main__":
    # 1 定义一个app
    app = QApplication(sys.argv)


    # 窗口
    window = QWidget()
    layout = QVBoxLayout() # layout

    # 2 4个组件
    line_edit1 = QLineEdit()
    line_edit2 = QLineEdit()
    calculate_button = QPushButton("计算")
    result_label = QLabel("结果: ")

    calculate_button.clicked.connect(calculate)

    # 3  把组件添加到layout里面
    layout.addWidget(line_edit1)
    layout.addWidget(line_edit2)
    layout.addWidget(calculate_button)
    layout.addWidget(result_label)

    # 4 展示
    window.setLayout(layout)
    window.show()  #  展示

    # 程序退出
    sys.exit(app.exec_())
