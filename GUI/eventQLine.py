import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class iseng(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(250, 150)
        self.setWindowIcon(QIcon('icco.ico'))
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Penasaran?')

        self.label = QLabel('<font color=red>Aplikasi pencari jodoh')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('TimesNewRoman',13))
        self.label.setParent(self)

        self.label2 = QLabel('Nama')
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setParent(self)
        self.text = QLineEdit('Your Name')
        self.text.mousePressEvent= lambda event: self.text.clear() if self.text.text()=='Your Name' else None
        self.text.keyReleaseEvent= lambda event: self.setWindowTitle(self.text.text())

        self.tombol = QPushButton('Cari')
        self.tombol.setParent(self)
        self.tombol.setToolTip('Klik untuk mencari <b>jodoh anda</b>')
        self.tombol.clicked.connect(self.close)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.label2, 1, 0)
        self.layout.addWidget(self.text, 2, 0)
        self.layout.addWidget(self.tombol, 3, 0)
        self.setLayout(self.layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = iseng()

    form.show()
    a.exec()