import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
import random

class DrawingWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(400, 400)
		self.circles = []  # List to hold circle data (x, y, radius)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setPen(QtGui.QColor("yellow"))

		for (x, y, radius) in self.circles:
			painter.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)

	def add_circle(self):
		x = random.randint(0, self.width())
		y = random.randint(0, self.height())
		radius = random.randint(10, 50)
		self.circles.append((x, y, radius))
		self.update()


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		uic.load_ui.loadUi("UI.ui", self)
		self.dw = DrawingWidget()
		self.pushButton.clicked.connect(self.dw.add_circle)
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.dw)
		layout.addWidget(self.pushButton)

		container = QtWidgets.QWidget()
		container.setLayout(layout)
		
		self.setCentralWidget(container)

	def paint_event(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setBrush(QtGui.QColor(0, 255, 255))
		qp.drawEllipse(QtCore.QPoint(randint(0, 800), randint(0, 600)), (a := randint(2, 25)), a)
		qp.end()

	def on_clicked(self):
		self.update()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()