import sys
from PyQt5.QtWidgets import *

class shortcut(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
        self.fungsiclick()

    def setup(self):
        self.resize(300, 150)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Shortcut')

        self.label1 = QLabel('Bilangan Pertama')
        self.entry1 = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.entry1)

        self.label2 = QLabel('Bilangan Kedua')
        self.entry2 = QLineEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.entry2)

        self.label3 = QLabel('Hasil Perhitungan')
        self.hasil = QLineEdit()
        self.hasil.setReadOnly(True)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.label3)
        vbox3.addWidget(self.hasil)

        vbox = QVBoxLayout()
        vbox.addLayout(vbox1)
        vbox.addLayout(vbox2)
        vbox.addLayout(vbox3)

        self.add = QPushButton('&Tambah')
        self.min = QPushButton('&Kurang')
        self.div = QPushButton('&Bagi')
        self.mul = QPushButton('K&ali')
        self.clr = QPushButton('&Clear')
        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.add)
        vbox5.addWidget(self.min)
        vbox5.addWidget(self.div)
        vbox5.addWidget(self.mul)
        vbox5.addWidget(self.clr)

        layout = QHBoxLayout()
        layout.addLayout(vbox)
        garis = QFrame()
        garis.setFrameShape(QFrame.VLine)
        garis.setFrameShadow(QFrame.Sunken)
        layout.addWidget(garis)
        layout.addLayout(vbox5)
        self.setLayout(layout)

    def fungsiclick(self):
        self.add.clicked.connect(lambda: self.cal('+'))
        self.min.clicked.connect(lambda: self.cal('-'))
        self.mul.clicked.connect(lambda: self.cal('*'))
        self.div.clicked.connect(lambda: self.cal('/'))
        self.clr.clicked.connect(lambda: self.clear())

    def cal(self, operasi):
        if not isinstance(self.entry1.text(), str) or not isinstance(self.entry2.text(), str):
            self.clear()
            msg = QMessageBox()
            msg.setWindowTitle('ERROR')
            msg.setText('Input anda salah')
            msg.exec_()
        else:
            a = float(self.entry1.text())
            b = float(self.entry2.text())
            if operasi=='+': c = a + b
            elif operasi=='-': c = a - b
            elif operasi=='/': c = a / b
            else: c = a * b
            self.hasil.setText(str(c))

    def clear(self):
        self.entry1.clear()
        self.entry2.clear()
        self.hasil.clear()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = shortcut()
    b.show()
    a.exec_()
