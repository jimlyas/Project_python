import sys, cx_Oracle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Dlg(QDialog):
    def __init__(self, judul):
        super().__init__()
        self.setup(judul)

    def setup(self, judul):
        self.setFixedSize(250, 150)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle(judul)

        self.lab1 = QLabel('Nama')
        self.entrynama = QLineEdit()

        self.lab2 = QLabel('Kelas ')
        self.entrykelas = QLineEdit()

        self.ok = QPushButton('OK')
        self.ca = QPushButton('CANCEL')

        layout = QGridLayout()
        layout.addWidget(self.lab1, 0, 0)
        layout.addWidget(self.entrynama, 0, 1)
        layout.addWidget(self.lab2, 1, 0)
        layout.addWidget(self.entrykelas, 1, 1)
        layout.addWidget(self.ok, 2, 0)
        layout.addWidget(self.ca, 2, 1)
        self.setLayout(layout)

        self.ok.clicked.connect(self.accept)
        self.ca.clicked.connect(self.reject)


class Utama(QWidget):
    terindeks = -1
    con = cx_Oracle.connect('jimlyas', 'shafira', 'localhost:1521/XE')
    cur = con.cursor()

    def __init__(self):
        super().__init__()
        self.setup()
        self.showdata()

    def setup(self):
        self.setFixedSize(450, 300)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('Data Kelas')

        self.tabel = QTableWidget()
        self.tabel.setRowCount(0)
        self.tabel.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabel.setColumnCount(2)
        self.tabel.setColumnWidth(0, 229)
        self.tabel.setColumnWidth(1, 100)
        self.tabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabel.verticalHeader().hide()
        self.tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabel.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        column = ['Nama Lengkap', 'Kelas']
        self.tabel.setHorizontalHeaderLabels(column)

        self.add = QPushButton('Tambah')
        self.dele = QPushButton('Hapus')
        self.edi = QPushButton('Edit')

        vbox = QVBoxLayout()
        vbox.addWidget(self.add)
        vbox.addWidget(self.edi)
        vbox.addStretch()
        vbox.addWidget(self.dele)

        layout = QHBoxLayout()
        layout.addWidget(self.tabel)
        layout.addLayout(vbox)
        self.setLayout(layout)

        self.add.clicked.connect(self.tambah)
        self.edi.clicked.connect(self.edit)
        self.dele.clicked.connect(self.delete)

    def showdata(self):
        Utama.cur.execute('select * from data')
        for row, form in enumerate(Utama.cur):
            Utama.terindeks+=1
            self.tabel.setRowCount(self.tabel.rowCount()+1)
            for column, item in enumerate(form):
                data = QTableWidgetItem()
                data.setFlags(Qt.ItemIsEnabled)
                data.setText(str(item))
                self.tabel.setItem(row, column, data)
        self.tabel.sortByColumn(0, Qt.AscendingOrder)

    def informasi(self, judul):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Berhasil!')
        self.msg.setText('Data berhasil di'+judul)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.exec_()

    def tambah(self):
        Utama.terindeks+=1
        self.tabel.setRowCount(self.tabel.rowCount()+1)
        form = Dlg('Tambah')
        form.exec_()
        if form.result()==1:
            nama = form.entrynama.text()
            kelas = form.entrykelas.text()
            query = 'insert into data values (:2, :3)'
            Utama.cur.execute(query, (nama, kelas))
            Utama.con.commit()
            data = [nama, kelas]
            for index in range(2):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                item.setText(data[index])
                self.tabel.setItem(Utama.terindeks, index, item)
            self.informasi('input')
        self.tabel.sortByColumn(0, Qt.AscendingOrder)

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
            query = 'update data set kelas=:2 where nama=:3'
            Utama.cur.execute(query, (kelas, nama))
            Utama.con.commit()
            data = [nama, kelas]
            for index in range(2):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                item.setText(data[index])
                self.tabel.setItem(baris, index, item)
            self.informasi('perbaharui')
        self.tabel.sortByColumn(0, Qt.AscendingOrder)

    def delete(self):
        Utama.terindeks-=1
        nama = self.tabel.item(self.tabel.currentRow(), 0).text()
        query = 'delete from data where nama=\''+nama+'\''
        Utama.cur.execute(query)
        Utama.con.commit()
        self.tabel.removeRow(self.tabel.currentRow())
        self.informasi('hapus')
        self.tabel.sortByColumn(0, Qt.AscendingOrder)

if __name__ == '__main__':
    p = QApplication(sys.argv)
    b = Utama()
    b.show()
    p.exec_()