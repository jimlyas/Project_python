import sys
from GUI.bukusatu import *

class bukudua(QWidget):
    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):
        self.setFixedSize(450, 350)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Library Manager')

        self.add = QPushButton('Add')
        self.edit = QPushButton('Edit')
        self.delete = QPushButton('Delete')
        self.clear = QPushButton('Clear')

        hbox = QHBoxLayout()
        hbox.addWidget(self.add)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.delete)
        hbox.addWidget(self.clear)

        self.daftar = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.daftar)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.add.clicked.connect(self.addclick)
        self.edit.clicked.connect(self.editclick)
        self.delete.clicked.connect(self.deleteclick)
        self.clear.clicked.connect(self.daftar.clear)

    def addclick(self):
        self.entry = bukusatu()
        self.entry.Okbutton.setText('Add')
        self.entry.exec_()
        if self.entry.result()==1:
            self.daftar.addItem(self.entry.Entrynama.text() +', ' + self.entry.Entrybuku.text())

    def editclick(self):
        if self.daftar.currentRow()<0:
            return
        else:
            self.entry = bukusatu()
            self.entry.Okbutton.setText('Edit')
            text = str(self.daftar.currentItem().text())
            index = text.index(',')
            self.entry.Entrynama.setText(text[:(index)])
            self.entry.Entrybuku.setText(text[(index+2):])
            self.entry.exec_()
            if self.entry.result()==1:
                self.daftar.currentItem().setText(self.entry.Entrynama.text()+','+self.entry.Entrybuku.text())

    def deleteclick(self):
        row  = self.daftar.currentRow()
        self.daftar.takeItem(row)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    f = bukudua()
    f.show()
    a.exec()