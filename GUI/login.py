import sys, cx_Oracle
from PyQt5.QtWidgets import *

class login(QWidget):
    con = cx_Oracle.connect('jimlyas', 'shafira', 'localhost:1521/XE')
    cur = con.cursor()

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(200,200)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowTitle('LOGIN')

        self.label1 = QLabel('Username')
        self.entryuser = QLineEdit()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.entryuser)

        self.label2 = QLabel('Password')
        self.entrypass = QLineEdit()
        self.entrypass.setEchoMode(QLineEdit.Password)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.entrypass)

        self.button = QPushButton('LOGIN')
        self.button.setDefault(True)
        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.masuk)

    def masuk(self):
        user = self.entryuser.text()
        passw = self.entrypass.text()
        query = 'select * from akun'
        login.cur.execute(query)
        for row in enumerate(login.cur):
            if row[1][0]==user and row[1][1]==passw:
                msg = QMessageBox()
                msg.setWindowTitle('Berhasil!')
                msg.setText('Akun ditemukan')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.entryuser.clear()
                self.entrypass.clear()
                return
            elif row[1][0]==user:
                msg = QMessageBox()
                msg.setWindowTitle('Gagal!')
                msg.setText('Password anda salah')
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                self.entrypass.clear()
                return
        msg = QMessageBox()
        msg.setWindowTitle('Gagal!')
        msg.setText('Akun tidak ditemukan')
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        self.entryuser.clear()
        self.entrypass.clear()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    f = login()
    f.show()
    a.exec_()