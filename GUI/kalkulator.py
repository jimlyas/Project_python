import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):
        self.setFixedSize(200, 200)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Kalkulator')

        self.entry = QLineEdit()
        self.entry.setAlignment(Qt.AlignRight)
        self.entry.setFont(QFont('SansSerif', 14))
        self.entry.setDisabled(True)
        self.entry.setToolTip('Menampilkan operasi yang dilakukan')

        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button0 = QPushButton('0')
        self.plusbutton = QPushButton('+')
        self.minbutton = QPushButton('-')
        self.divbutton = QPushButton('/')
        self.mulbutton = QPushButton('x')
        self.clrbutton = QPushButton('CLR')
        self.dotbutton = QPushButton('.')
        self.calbutton = QPushButton('=')

        layout = QGridLayout()
        layout.addWidget(self.entry, 0, 0, 1, 4)
        layout.addWidget(self.button7, 1, 0)
        layout.addWidget(self.button8, 1, 1)
        layout.addWidget(self.button9, 1, 2)
        layout.addWidget(self.clrbutton, 1, 3)
        layout.addWidget(self.button4, 2, 0)
        layout.addWidget(self.button5, 2, 1)
        layout.addWidget(self.button6, 2, 2)
        layout.addWidget(self.mulbutton, 2, 3)
        layout.addWidget(self.button1, 3, 0)
        layout.addWidget(self.button2, 3, 1)
        layout.addWidget(self.button3, 3, 2)
        layout.addWidget(self.divbutton, 3, 3)
        layout.addWidget(self.button0, 4, 0)
        layout.addWidget(self.dotbutton, 4, 1)
        layout.addWidget(self.minbutton, 4, 2)
        layout.addWidget(self.plusbutton, 4, 3)
        layout.addWidget(self.calbutton, 5, 0, 1, 4)
        self.setLayout(layout)

        self.button1.clicked.connect(lambda: self.tulisdigit(1))
        self.button2.clicked.connect(lambda: self.tulisdigit(2))
        self.button3.clicked.connect(lambda: self.tulisdigit(3))
        self.button4.clicked.connect(lambda: self.tulisdigit(4))
        self.button5.clicked.connect(lambda: self.tulisdigit(5))
        self.button6.clicked.connect(lambda: self.tulisdigit(6))
        self.button7.clicked.connect(lambda: self.tulisdigit(7))
        self.button8.clicked.connect(lambda: self.tulisdigit(8))
        self.button9.clicked.connect(lambda: self.tulisdigit(9))
        self.button0.clicked.connect(lambda: self.tulisdigit(0))
        self.mulbutton.clicked.connect(lambda: self.tulisoperator('*'))
        self.divbutton.clicked.connect(lambda: self.tulisoperator('/'))
        self.minbutton.clicked.connect(lambda: self.tulisoperator('-'))
        self.plusbutton.clicked.connect(lambda: self.tulisoperator('+'))
        self.dotbutton.clicked.connect(self.writepoint)
        self.clrbutton.clicked.connect(self.entry.clear)
        self.calbutton.clicked.connect(self.calculate)

    def tulisdigit(self, digit):
        if digit in range(0, 10):
            self.entry.setText(self.entry.text()+str(digit))

    def tulisoperator(self, operasi):
        if len(self.entry.text())==0:
            return
        else:
            if operasi in ['*', '/', '+', '-']:
                if self.entry.text()[-1] in ['*', '/', '+', '-']:
                    self.entry.setText(self.entry.text()[-1]+operasi)
                else:
                    self.entry.setText(self.entry.text()+operasi)

    def writepoint(self):
        if len(self.entry.text())==0 or self.entry.text()[-1] in ['*', '/', '+', '-']:
            return
        else:
            self.entry.setText(self.entry.text()+'.')

    def calculate(self):
        baris = self.entry.text()
        if len(baris)==0:
            return
        else:
            try:
                hasil = eval(baris)
                self.entry.setText(str(hasil))
            except:
                self.entry.setText('ERROR')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = kalkulator()
    form.show()
    a.exec()