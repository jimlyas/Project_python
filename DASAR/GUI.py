import sys
import time
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QSplashScreen

if __name__ == '__main__':
    a = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap('Python-Logo.png'), QtCore.Qt.WindowStaysOnTopHint)
    splash.show()
    time.sleep(2)
    splash.close()

    form = QWidget()
    form.setFixedSize(200, 100)
    form.move(QDesktopWidget().availableGeometry().center() - form.frameGeometry().center())
    form.setWindowTitle('Phyton GUI')


    label = QLabel('    HELLO WORLD    ')
    label.move(50, 40)
    label.setParent(form)
    def runningtext():
        old = label.text()
        #Ini dari kiri ke kanan
        new = old[len(old) - 1:] + old[0:len(old) - 1]
        label.setText(new)
    timer = QTimer()
    timer.timeout.connect(runningtext)
    timer.start(250)

    form.show()
    a.exec_()