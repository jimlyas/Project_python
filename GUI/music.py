# Author = J I M L Y
import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class Music(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer(self)
        self.filename = []
        self.pausindex = None
        self.setup()
        self.show()

    def setup(self):
        self.setFixedSize(400, 450)
        self.setWindowTitle('Music Player')
        self.setWindowIcon(QIcon('musicc.ico'))

        #Pengaturan tampilan Menu Bar
        menu = QMenuBar()
        menu.adjustSize()
        menu.setFixedHeight(20)
        #Pengaturan tampilan sub menu
        file = menu.addMenu('File')
        self.open = QAction('Open File', self)
        self.open.setShortcut('CTRL+O')
        self.open.triggered.connect(self.openfile)
        file.addAction(self.open)

        #Pengaturan tampilan slider dan judul dari player
        self.slide = QSlider(Qt.Horizontal)
        self.judul = QLabel('<font color= white>Play Your Music Here!')
        self.judul.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.judul.setFixedHeight(50)
        self.judul.setAlignment(Qt.AlignCenter)
        self.judul.setStyleSheet("QLabel {background-color: grey; color:white}")
        self.judul.setFont(QFont('Verdana', 11))

        #Pengaturan tampilan tombol-tombol
        self.play = QPushButton('Play')
        self.play.setShortcut('CTRL+E')
        self.play.setToolTip('Memutar lagu')
        self.paus = QPushButton('Pause')
        self.paus.setShortcut('CTRL+R')
        self.paus.setToolTip('Menjeda lagu')
        self.next = QPushButton('Next')
        self.next.setShortcut('CTRL+T')
        self.next.setToolTip('Memutar lagu selanjutnya')
        self.prev = QPushButton('Prev')
        self.prev.setShortcut('CTRL+Q')
        self.prev.setToolTip('Memutar lagu sebelumnya')
        self.stop = QPushButton('Stop')
        self.stop.setShortcut('CTRL+W')
        self.stop.setToolTip('Memberhentikan lagu')

        hb = QHBoxLayout()
        hb.addWidget(self.prev)
        hb.addWidget(self.stop)
        hb.addWidget(self.play)
        hb.addWidget(self.paus)
        hb.addWidget(self.next)

        #Pengaturan tampilan list player
        self.list = QListWidget()
        self.list.setSpacing(10)
        self.list.mouseDoubleClickEvent= lambda event: self.listclick()

        #Pengaturan Layout dari widgets
        vb = QVBoxLayout()
        vb.addWidget(menu)
        vb.addWidget(self.judul)
        vb.addWidget(self.slide)
        vb.addLayout(hb)
        vb.addWidget(self.list)
        self.setLayout(vb)

        #Menghubungkan method-method dengan tombol
        self.play.clicked.connect(self.playclick)
        self.paus.clicked.connect(self.pauseclick)
        self.stop.clicked.connect(self.stopclick)
        self.next.clicked.connect(self.nextclick)
        self.prev.clicked.connect(self.prevclick)

        #Sinkronisasi antara slider dengan player
        self.slide.sliderMoved.connect(self.slidemove)

        self.player.positionChanged.connect(self.playerchange)
        self.player.durationChanged.connect(self.durationchange)
        self.player.mediaStatusChanged.connect(self.repeat)

    def repeat(self, state):
        if state == QMediaPlayer.EndOfMedia:
            self.nextclick()

    def mode(self, kondisi):
        if kondisi:
            self.play.setEnabled(False)
            self.paus.setEnabled(True)
            self.stop.setEnabled(True)
        else:
            self.play.setEnabled(True)
            self.paus.setEnabled(False)
            self.stop.setEnabled(False)

    def openfile(self):
        filename = QFileDialog.getOpenFileNames(self, 'Open File', 'D:\\', 'MP3 Files (*.mp3)')
        if not filename[0]: return
        for a in range(len(filename[0])):
            self.filename.append(filename[0][a])
            (dirname, nama) = os.path.split(filename[0][a])
            self.list.addItem(nama[:len(nama)-4])
            print('Adding '+nama[:len(nama)-4])

    def playclick(self):
        try:
            if self.player.state()!=QMediaPlayer.PausedState:
                if self.list.currentRow()==-1:
                    self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[0])))
                    self.list.setCurrentRow(0)
                else:
                    self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
                print('Playing ' + self.list.currentItem().text())
                self.judul.setText(self.list.currentItem().text())
            else:
                self.list.setCurrentRow(self.pausindex)
                print('Playing '+self.judul.text()+' at %d' %self.player.position())
            self.player.play()
            self.mode(True)
        except:
            print('Media is not defined')

    def listclick(self):
        try:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
            print('Playing ' + self.list.currentItem().text())
            self.judul.setText(self.list.currentItem().text())
            self.player.play()
            self.mode(True)
        except:
            print('Media is not defined')

    def pauseclick(self):
        print('Pause at %d' %self.player.position())
        self.pausindex = self.list.currentRow()
        self.player.pause()
        self.mode(False)

    def stopclick(self):
        print('Stop')
        self.player.stop()
        self.mode(False)

    def nextclick(self):
        try:
            self.list.setCurrentRow(self.list.currentRow()+1)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
            self.player.play()
            self.judul.setText(self.list.currentItem().text())
            print('Next, playing ' + self.list.currentItem().text())
        except:
            print('End of Playlist')
            self.player.stop()
            self.mode(False)

    def prevclick(self):
        try:
            self.list.setCurrentRow(self.list.currentRow()-1)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
            self.player.play()
            self.judul.setText(self.list.currentItem().text())
            print('Prev, Playing '+self.list.currentItem().text())
        except:
            print('Start of Playlist')
            self.player.stop()
            self.mode(False)

    def slidemove(self):
        self.player.setPosition(self.slide.value())
        print(self.slide.value())

    def slideclick(self, position):
        self.player.setPosition(position)

    def playerchange(self, position):
        self.slide.setValue(position)

    def durationchange(self, position):
        self.slide.setMaximum(position)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    a.setStyle(QStyleFactory.create('Windows'))
    b = Music()
    a.exec_()