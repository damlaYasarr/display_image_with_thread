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
        self.setGeometry( 500, 500,1000, 1000)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("placed screen!")
        self.label.move(50, 90)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("my cuttiest perspective!")
        
        self.label1.size(10)
        #self.label1.setFont
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("shot pic!")
        self.b1.move(10,40)
        self.b2 = QtWidgets.QPushButton(self)   
        self.b2.setText("record video!")  
        self.b2.move(120,40)  
        self.b3 = QtWidgets.QPushButton(self)   
        self.b3.setText("setting!")  
        self.b3.move(880,40) 

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