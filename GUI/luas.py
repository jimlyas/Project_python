import sys
from PyQt5.QtWidgets import *


class Luas(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton(self)
        self.hmmh = QLineEdit(self)
        self.setup()
        self.show()

    def setup(self):
        self.setWindowTitle('Hitung Luas')
        self.setFixedSize(400, 150)

        self.hmmh.setPlaceholderText('Masukkan jari-jari lingkaran')
        self.button.setText('Hitung')
        self.button.clicked.connect(self.hitung)

        hb = QHBoxLayout(self)
        hb.addWidget(self.hmmh)
        hb.addWidget(self.button)
        self.setLayout(hb)

    def hitung(self):
        result = 3.14 * (int(self.hmmh.text()) * 2)
        dlg = QMessageBox()
        dlg.setWindowTitle('Hasil Perhitungan')
        dlg.setText('Hasilnya adalah %f' % result)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec_()
        self.hmmh.setText('')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    # noinspection PyCallByClass
    a.setStyle(QStyleFactory.create('Windows'))
    b = Luas()
    a.exec()
