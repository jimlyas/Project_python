import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Tampilin(QWidget):
    timer = QTimer()
    check = False

    def __init__(self, nama):
        super().__init__()
        self.setup(nama)
        self.timer.timeout.connect(self.running)
        self.timer.start(250)

    def setup(self, nama):
        self.setWindowTitle('Menyapa '+nama)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QIcon('code.ico'))
        self.setFixedSize(760, 150)

        self.label = QLabel('Hai '+nama+', ini contoh program Python.     ')
        self.label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def running(self):
        if not self.check:
            time.sleep(2)
            self.check = True
        old = self.label.text()

        #Ini dari kanan ke kiri
        new = old[1:len(old)] + old[0]
        self.label.setText(new)


class Asknama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('Menanyakan nama')
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QIcon('code.ico'))
        self.setFixedSize(300, 200)
        self.setCentralWidget(QWidget(self))

        self.label = QLabel('Siapa Nama anda?')
        self.label.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(150)
        self.entry = QLineEdit()
        self.entry.setPlaceholderText('Nama Anda')
        self.entry.setFixedWidth(250)
        self.tombol = QPushButton('Submit')
        self.tombol.setFixedWidth(100)
        self.tombol.setDefault(True)
        self.tombol.clicked.connect(self.diklik)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.entry, 0, Qt.AlignCenter)
        vbox.addWidget(self.tombol, 0,  Qt.AlignCenter)
        self.centralWidget().setLayout(vbox)

    def diklik(self):
        if not self.entry.text():
            print('Nama belum ditentukan.')
        else:
            print('Nama yang diterima adalah ' + self.entry.text()+'.')
            self.run = Tampilin(self.entry.text())
            self.run.show()
            self.hide()

if __name__ == '__main__':
   a = QApplication(sys.argv)
   b = Asknama()
   b.show()
   a.exec_()