import sys
from PyQt5.QtWidgets import *

class b(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(300, 250)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Percobaan')

        self.label1 = QLabel('Nama  ')
        self.entrynama = QLineEdit()
        hbox1 =QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.entrynama)

        self.label2 = QLabel('Alamat')
        self.entryalamat = QLineEdit()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.entryalamat)

        self.laki = QRadioButton('Laki-Laki')
        self.pere = QRadioButton('Perempuan')
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.laki)
        hbox3.addWidget(self.pere)

        self.grup = QButtonGroup()
        self.grup.addButton(self.laki)
        self.grup.addButton(self.pere)

        self.ch = QCheckBox('Menikah')

        self.label3 = QLabel('Pendidikan')
        self.pend = QComboBox()
        self.pend.addItem('SD')
        self.pend.addItem('SMP')
        self.pend.addItem('SMA')
        self.pend.addItem('Perguruan Tinggi')
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.label3)
        hbox4.addWidget(self.pend)

        self.label4 = QLabel('Umur')
        self.umur = QSpinBox()
        self.umur.setRange(1, 30)
        self.umur.setValue(10)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.label4)
        hbox5.addWidget(self.umur)

        self.button = QPushButton('Hasilnya')
        garis = QFrame()
        garis.setFrameShape(QFrame.HLine)
        garis.setFrameShadow(QFrame.Sunken)

        layout = QGridLayout()
        layout.addLayout(hbox1, 0, 0)
        layout.addLayout(hbox2, 1, 0)
        layout.addLayout(hbox3, 2, 0)
        layout.addWidget(self.ch, 3, 0)
        layout.addLayout(hbox4, 4, 0)
        layout.addLayout(hbox5,5, 0)
        layout.addWidget(garis, 6, 0)
        layout.addWidget(self.button, 7, 0)
        self.setLayout(layout)

        self.button.clicked.connect(self.calculte)

    def calculte(self):
        if self.grup.checkedButton():
            print(self.grup.checkedButton().text())
            if not self.ch.isChecked():
                print(self.entrynama.text()+' belum menikah')
            else:
                print(self.entrynama.text()+' sudah menikah')
            print(self.pend.currentText())
            print('%d'%self.umur.value()+' tahun')
        else:
            print('gagal')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    f = b()
    f.show()
    a.exec_()