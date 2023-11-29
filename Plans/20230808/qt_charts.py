import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chart Example")

        self.chart_view = QChartView(self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setGeometry(50, 50, 800, 600)

        self.create_bar_chart()

    def create_bar_chart(self):
        chart = QChart()
        series = QBarSeries()

        bar_set = QBarSet("Values")
        bar_set.append([1, 2, 3, 4, 5])
        series.append(bar_set)
        chart.addSeries(series)

        chart.setTitle("Simple Bar Chart")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        self.chart_view.setChart(chart)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ChartWindow()
    window.show()

    sys.exit(app.exec_())
