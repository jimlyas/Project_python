from PyQt5.QtWidgets import *

class bukusatu(QDialog):
    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):
        self.setFixedSize(300, 100)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Form Data')

        self.Okbutton = QPushButton('None')
        self.Cancelbutton = QPushButton('Batal')

        self.label1 = QLabel('Nama Penulis')
        self.Entrynama = QLineEdit()
        self.label2 = QLabel('Nama Buku')
        self.Entrybuku = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.Entrynama, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.Entrybuku, 1, 1)
        layout.addWidget(self.Okbutton, 2, 0)
        layout.addWidget(self.Cancelbutton, 2, 1)
        self.setLayout(layout)

        self.Okbutton.clicked.connect(self.accept)
        self.Cancelbutton.clicked.connect(self.reject)