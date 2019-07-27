import sys
from GUI.bukusatu import *


class BukuDua(QWidget):
    def __init__(self):
        super().__init__()
        self.entry = BukuSatu()
        self.daftar = QListWidget()
        self.clear = QPushButton('Clear')
        self.delete = QPushButton('Delete')
        self.edit = QPushButton('Edit')
        self.add = QPushButton('Add')
        self.setupui()

    def setupui(self):
        self.setFixedSize(450, 350)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Library Manager')

        hbox = QHBoxLayout()
        hbox.addWidget(self.add)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.delete)
        hbox.addWidget(self.clear)

        layout = QVBoxLayout()
        layout.addWidget(self.daftar)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.add.clicked.connect(self.addclick)
        self.edit.clicked.connect(self.editclick)
        self.delete.clicked.connect(self.deleteclick)
        self.clear.clicked.connect(self.daftar.clear)

    def addclick(self):
        self.entry.Okbutton.setText('Add')
        self.entry.exec_()
        if self.entry.result()==1:
            self.daftar.addItem(self.entry.Entrynama.text() +', ' + self.entry.Entrybuku.text())
        self.entry.Entrybuku.setText(None)
        self.entry.Entrynama.setText(None)

    def editclick(self):
        if self.daftar.currentRow()<0:
            return
        else:
            self.entry = BukuSatu()
            self.entry.Okbutton.setText('Edit')
            text = str(self.daftar.currentItem().text())
            index = text.index(',')
            self.entry.Entrynama.setText(text[:index])
            self.entry.Entrybuku.setText(text[(index+2):])
            self.entry.exec_()
            if self.entry.result()==1:
                self.daftar.currentItem().setText(self.entry.Entrynama.text()+','+self.entry.Entrybuku.text())

    def deleteclick(self):
        row = self.daftar.currentRow()
        self.daftar.takeItem(row)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    f = BukuDua()
    f.show()
    a.exec()