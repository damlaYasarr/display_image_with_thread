import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
import sys
import threading


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def button_clicked(self, load_image):
        print("clicked")

        self.lb = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(load_image)
        height_of_label = 200
        self.lb.resize(self.width(), height_of_label)
        self.lb.setPixmap(pixmap)
        self.lb.show()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")

        self.b1.clicked.connect(self.button_clicked)


def thread():
    sr = "/home/damlayasarr/threadExample/images/bisi.png"
    img_thread = threading.Thread(target=MyWindow.button_clicked, args=(sr,))
    img_thread.start()
    while img_thread.is_alive():
        print(f"doing some other stuff while the thread does its thing")
        time.sleep(1)
    img_thread.join()

def window():
    thread()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()

    sys.exit(app.exec_())


window()