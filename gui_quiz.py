# Line 2-7 = Import modul yang diperlukan
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from fungsi import frame1, frame2, frame3, frame4, grid #Import fungsi.py


app = QApplication(sys.argv) #Inisialisasi aplikasi GUI

# Line 13-26 = Basic setting untuk display window
window = QWidget()
window.setWindowTitle("UAS Game Development - Tanzil R.K")
window.setFixedWidth(1000)

window.setStyleSheet("background: #161219;")

frame1() #Display frame 1

window.setLayout(grid)

window.show()
sys.exit(app.exec()) #Terminate app
