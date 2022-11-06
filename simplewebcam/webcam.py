import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
import sys
import threading
import asyncio

class MyWebcam(QMainWindow):
    def __init__(self):
        super(MyWebcam, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")

        #self.b1.clicked.connect(self.button_clicked)

    def capturePhoto(self):
        pass
        
    def recordvideoo(self):
        pass
    
    def openrecords(self):
        pass
    def openPicture(self):
        pass
    
"""
def thread():
   #sr = "/home/damlayasarr/threadExample/images/bisi.png"
    img_thread = threading.Thread(target=MyWebcam.button_clicked, args=(sr,))
    img_thread.start()
    while img_thread.is_alive():
        print(f"doing some other stuff while the thread does its thing")
        time.sleep(1)
    img_thread.join()
"""
def window():
    #thread()
    app = QApplication(sys.argv)
    win = MyWebcam()
    win.show()

    sys.exit(app.exec_())


window()