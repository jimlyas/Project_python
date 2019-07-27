import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Class for pop up dialog
class Dlg(QDialog):
    def __init__(self, judul):
        super().__init__()
        self.cancelButton = QPushButton('CANCEL')
        self.okButton = QPushButton('OK')
        self.entrykelas = QLineEdit()
        self.lab2 = QLabel('Kelas ')
        self.entrynama = QLineEdit()
        self.lab1 = QLabel('Nama')
        self.setup(judul)

    def setup(self, judul):
        self.setFixedSize(300, 250)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle(judul)

        layout = QGridLayout()
        layout.addWidget(self.lab1, 0, 0)
        layout.addWidget(self.entrynama, 0, 1)
        layout.addWidget(self.lab2, 1, 0)
        layout.addWidget(self.entrykelas, 1, 1)
        layout.addWidget(self.okButton, 2, 0)
        layout.addWidget(self.cancelButton, 2, 1)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


# Class for main window
class Utama(QWidget):
    terindeks = -1
    keys = []

    def __init__(self):
        super().__init__()
        self.cred = credentials.Certificate('services.json')
        firebase_admin.initialize_app(self.cred, {'databaseURL': 'https://delia-weather.firebaseio.com'})
        self.databaseRef = db.reference('/examples')
        self.msg = QMessageBox()
        self.editButton = QPushButton('Edit')
        self.deleteButton = QPushButton('Hapus')
        self.addButton = QPushButton('Tambah')
        self.tabel = QTableWidget()

        self.setup()
        self.showdata()

    def setup(self):
        self.setFixedSize(500, 350)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Data Kelas')

        self.tabel.setRowCount(0)
        self.tabel.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabel.setColumnCount(2)
        self.tabel.setColumnWidth(0, 250)
        self.tabel.setColumnWidth(1, 100)
        self.tabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabel.verticalHeader().hide()
        self.tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabel.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        column = ['Nama Lengkap', 'Kelas']
        self.tabel.setHorizontalHeaderLabels(column)

        vbox = QVBoxLayout()
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.editButton)
        vbox.addStretch()
        vbox.addWidget(self.deleteButton)

        layout = QHBoxLayout()
        layout.addWidget(self.tabel)
        layout.addLayout(vbox)
        self.setLayout(layout)

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.deleteButton.clicked.connect(self.delete)

    def showdata(self):
        snap = self.databaseRef.get()
        if snap is not None:
            for key, val in snap.items():
                self.terindeks+=1
                self.tabel.setRowCount(self.tabel.rowCount()+1)
                self.keys.append(key)
                self.tabel.setItem(self.tabel.rowCount()-1, 0, QTableWidgetItem(val['nama']))
                self.tabel.setItem(self.tabel.rowCount()-1, 1, QTableWidgetItem(val['kelas']))

    def displaypopupmessage(self, nama, judul):
        self.msg.setWindowTitle('Berhasil!')
        self.msg.setText('Data {0} berhasil di{1}'.format(nama, judul))
        self.msg.setIcon(QMessageBox.Information)
        self.msg.exec_()

    def add(self):
        self.terindeks+=1
        self.tabel.setRowCount(self.tabel.rowCount()+1)
        form = Dlg('Tambah')
        form.exec_()
        if form.result()==1:
            nama = form.entrynama.text()
            kelas = form.entrykelas.text()
            data = [nama, kelas]
            for index in range(2):
                item = QTableWidgetItem()
                item.setText(data[index])
                self.tabel.setItem(self.terindeks, index, item)
            self.displaypopupmessage(nama, 'input')

            new_key = self.databaseRef.push().key
            self.keys.append(new_key)
            self.databaseRef.child(new_key).set({'nama': nama, 'kelas': kelas})

    def edit(self):
        baris = self.tabel.currentIndex().row()
        form = Dlg('Edit')
        nama = self.tabel.item(baris, 0).text()
        kelas = self.tabel.item(baris, 1).text()
        form.entrynama.setText(nama)
        form.entrynama.setReadOnly(True)
        form.entrykelas.setText(kelas)
        form.exec_()
        if form.result()==1:
            nama = form.entrynama.text()
            kelas = form.entrykelas.text()
            data = [nama, kelas]
            for index in range(2):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                item.setText(data[index])
                self.tabel.setItem(baris, index, item)
            self.displaypopupmessage(nama, 'perbaharui')
            self.databaseRef.child(self.keys.__getitem__(baris)).set({'nama': nama, 'kelas': kelas})

    def delete(self):
        self.terindeks-=1
        baris = self.tabel.currentIndex().row()
        nama = self.tabel.item(baris, 0).text()
        self.databaseRef.child(self.keys.__getitem__(baris)).delete()
        self.keys.remove(self.keys.__getitem__(baris))
        self.tabel.removeRow(self.tabel.currentRow())
        self.displaypopupmessage(nama, 'hapus')


if __name__ == '__main__':
    p = QApplication(sys.argv)
    b = Utama()
    b.show()
    p.exec_()