import sys
from PyQt5.QtWidgets import *


class kirimSMS(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(350, 200)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Kirim SMS')

        self.label1 = QLabel('No. HP ')
        self.entryhape = QLabel('Kosong')
        self.entryhape.mousePressEvent=lambda event: self.pilihhape()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.entryhape)

        self.label2 = QLabel('Isi Pesan')
        self.entrypesan = QTextEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.entrypesan)

        self.Okbutton = QPushButton('&Kirim Pesan')
        self.cancelbutton = QPushButton('&Batal')
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.Okbutton)
        hbox2.addWidget(self.cancelbutton)

        garis = QFrame()
        garis.setFrameShape(QFrame.HLine)
        garis.setFrameShadow(QFrame.Sunken)

        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        layout.addLayout(vbox1)
        layout.addWidget(garis)
        layout.addLayout(hbox2)
        self.setLayout(layout)

        self.Okbutton.clicked.connect(self.okclick)
        self.cancelbutton.clicked.connect(self.close)

    def okclick(self):
        # Untuk konversi teks dokumen menjadi string
        print(self.entrypesan.document().toPlainText())

        msg = QMessageBox()
        msg.setText('Pesan telah terkirim')
        msg.setInformativeText('Pesan yang anda ketikkan telah dikirim ke nomor '+str(self.entryhape.text()))
        msg.setDetailedText(self.entrypesan.document().toPlainText())
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Berhasil!')
        msg.exec_()
        self.close()

    def pilihhape(self):
        if self.entryhape.text()!='Kosong':
            text, ok = QInputDialog.getText(self, 'Input nomor', 'Masukkan nomor HP tujuan :', QLineEdit.Normal, self.entryhape.text())
        else:
            text, ok = QInputDialog.getText(self, 'Input nomor', 'Masukkan nomor HP tujuan :')

        if ok:
            self.entryhape.setText(str(text))

if __name__ == '__main__':
    a= QApplication(sys.argv)
    f = kirimSMS()
    f.show()
    a.exec_()