import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class textHTML(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 150)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Contoh Teks')

        self.label1 = QLabel('<h1 style=background-color:green><font color=Cornsilk>Hello <font color=red>PyQt5</font></h1>')
        self.label1.move(10, 10)

        QToolTip.setFont(QFont('TimesNewRoman', 10))

        self.label2 = QLabel('<p style=background-color:Black><font color=red>Teks ini dibuat dengan tag HTML. dapat dibuat menjadi'
                             '<b> tebal</b> atau <i>miring</i> bahkan <u>bergaris bawah</u></p>')
        self.label2.setWordWrap(True)
        self.label2.move(10, 50)
        self.label2.setToolTip('<b>Ini</b> bukan <i>apa-apa</i> kok')

        self.button = QPushButton('GANTI')
        self.button.move(150,120)
        self.button.setToolTip('Klik untuk pindah ke <b>form kedua<b/>')
        self.button.clicked.connect(self.close)

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 0, 1)
        layout.addWidget(self.button, 1, 0, 1, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = textHTML()
    form.show()
    a.exec()