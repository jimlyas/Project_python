import sys, subprocess, os, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class fontdialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(250, 100)
        self.setWindowTitle('Format Font')
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QIcon('code.ico'))

        self.label1 = QLabel('Jenis Font')
        self.label2 = QLabel('Ukuran Font')

        self.fonttext = QFontComboBox()
        self.fonttext.setEditable(False)
        self.ukuran = QSpinBox()
        self.ukuran.setMinimum(1)
        self.ukuran.setMaximum(30)

        self.ok = QPushButton('OK')
        self.cancel = QPushButton('Cancel')
        hbox = QHBoxLayout()
        hbox.addWidget(self.ok)
        hbox.addWidget(self.cancel)

        lay = QGridLayout()
        lay.addWidget(self.label1, 0, 0)
        lay.addWidget(self.fonttext, 0, 1)
        lay.addWidget(self.label2, 1, 0)
        lay.addWidget(self.ukuran, 1, 1)
        lay.addLayout(hbox, 2, 0)
        self.setLayout(lay)

        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)

class edit(QWidget):
    def __init__(self):
        super().__init__()
        self.current = ''
        self.setup()

    def setup(self):
        self.setFixedSize(650, 690)
        self.setWindowTitle('Code Editor')
        self.move(350, 0)
        self.setWindowIcon(QIcon('code.ico'))

        self.menu = QMenuBar()
        self.menu.adjustSize()
        self.menu.setFixedHeight(20)

        file = self.menu.addMenu('&File')
        open = QAction('Open File', self)
        open.setShortcut('CTRL+O')
        open.triggered.connect(self.openfile)
        save = QAction('Save File', self)
        save.setShortcut('CTRL+S')
        save.triggered.connect(self.save)
        saveas = QAction('Save As', self)
        saveas.setShortcut('ALT+A')
        saveas.triggered.connect(self.saveas)
        new = QAction('New File', self)
        new.setShortcut('CTRL+N')
        new.triggered.connect(self.newfile)
        run = QAction('Run File', self)
        run.setShortcut('CTRL+R')
        run.triggered.connect(self.runn)
        file.addAction(open)
        file.addAction(new)
        file.addAction(save)
        file.addAction(saveas)
        file.addAction(run)

        format = self.menu.addMenu('Format')
        font = QAction('Format Font', self)
        font.setShortcut('CTRL+F')
        font.triggered.connect(self.fontsetting)
        format.addAction(font)

        self.entry = QTextEdit()
        self.entry.setFont(QFont('Windows Command Prompt', 12))
        self.jenis = 'Windows Command Prompt'
        self.ukur = 12

        vbox = QVBoxLayout()
        vbox.addWidget(self.menu)
        vbox.addWidget(self.entry)
        self.setLayout(vbox)

    def runn(self):
        if self.current[len(self.current)-3:]=='.py':
            subprocess.call(['python', self.current])
        elif self.current[len(self.current)-5:]=='.java':
            subprocess.call(['javac', self.current])
            time.sleep(5)
            (dirname, filename) = os.path.split(self.current)
            subprocess.call(['java', filename[:len(filename)-5]])

    def confirm(self):
        if self.entry.document().isModified():
            respond = QMessageBox.question(self, 'Konfimasi', 'Teks belum disimpan, Simpan terlebih dahulu?')
            print(QMessageBox.Yes)
            if respond == QMessageBox.Yes:
                self.saveas()

    def newfile(self):
        self.confirm()
        self.entry.document().clear()
        self.current=''
        self.setWindowTitle('Code Editor : Untitled')

    def openfile(self):
        self.confirm()
        nama = QFileDialog.getOpenFileName(self, 'Pilih File', 'D:\\', 'File text (*.txt);; Java File (*.java);; Python File (*.py)')
        if not nama[0]: return
        self.current = nama[0]
        self.setWindowTitle('Code Editor : '+self.current)
        handel = QFile(nama[0])
        if not handel.open(QIODevice.ReadOnly): return
        stream = QTextStream(handel)
        self.entry.setPlainText(stream.readAll())
        handel.close()

    def tulis(self):
        handel = QFile(self.current)
        if not handel.open(QIODevice.WriteOnly): return
        stream = QTextStream(handel)
        stream << self.entry.document().toPlainText()
        stream.flush()
        handel.close()
        self.entry.document().setModified(False)

    def save(self):
        if self.current=='':
            self.saveas()
        else:
            self.tulis()

    def saveas(self):
        nama = QFileDialog.getSaveFileName(self, 'Simpan File', 'D:\\', 'File text (*.txt);; Java File (*.java);; Python File (*.py)')
        if not nama[0]: return
        self.current = nama[0]
        self.setWindowTitle('Code Editor : '+self.current)
        self.tulis()

    def fontsetting(self):
        a = fontdialog()
        a.fonttext.setCurrentText(self.jenis)
        a.ukuran.setValue(self.ukur)
        a.exec_()
        if a.result()==1:
            self.entry.setFont(QFont(a.fonttext.currentText(), a.ukuran.value()))
            self.jenis = a.fonttext.currentText()
            self.ukur = a.ukuran.value()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = edit()
    b.show()
    a.exec_()