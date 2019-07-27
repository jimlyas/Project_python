# Author = J I M L Y
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *


class Music(QWidget):

    # Class Constructor
    def __init__(self):
        super().__init__()
        self.pauseButton = QPushButton('Pause')
        self.playButton = QPushButton('Play')
        self.list = QListWidget()
        self.stopButton = QPushButton('Stop')
        self.prevButton = QPushButton('Prev')
        self.nextButton = QPushButton('Next')
        self.judul = QLabel('<font color= white>Play Your Music Here!')
        self.slide = QSlider(Qt.Horizontal)
        self.open = QAction('Open File', self)
        self.player = QMediaPlayer(self)
        self.filename = []
        self.pausindex = None
        self.setup()
        self.show()

    def setup(self):
        self.setFixedSize(400, 450)
        self.setWindowTitle('Music Player')
        self.setWindowIcon(QIcon('musicc.ico'))

        # Pengaturan tampilan Menu Bar
        menu = QMenuBar()
        menu.adjustSize()
        menu.setFixedHeight(20)

        # Pengaturan tampilan sub menu
        file = menu.addMenu('File')
        self.open.setShortcut('CTRL+O')
        # CONTOH : bagaimana menggunakan parameter pada slot
        self.open.triggered.connect(lambda: self.openfile('Opening File Dialog'))
        file.addAction(self.open)

        # Pengaturan tampilan slider dan judul dari player
        self.judul.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.judul.setFixedHeight(50)
        self.judul.setAlignment(Qt.AlignCenter)
        self.judul.setStyleSheet("QLabel {background-color: grey; color:white}")
        self.judul.setFont(QFont('Verdana', 11))

        # Pengaturan tampilan tombol-tombol
        self.playButton.setShortcut('CTRL+E')
        self.playButton.setToolTip('Memutar lagu')
        self.pauseButton.setShortcut('CTRL+R')
        self.pauseButton.setToolTip('Menjeda lagu')
        self.nextButton.setShortcut('CTRL+T')
        self.nextButton.setToolTip('Memutar lagu selanjutnya')
        self.prevButton.setShortcut('CTRL+Q')
        self.prevButton.setToolTip('Memutar lagu sebelumnya')
        self.stopButton.setShortcut('CTRL+W')
        self.stopButton.setToolTip('Memberhentikan lagu')

        hb = QHBoxLayout()
        hb.addWidget(self.prevButton)
        hb.addWidget(self.stopButton)
        hb.addWidget(self.playButton)
        hb.addWidget(self.pauseButton)
        hb.addWidget(self.nextButton)

        # Pengaturan tampilan list player
        self.list.setSpacing(5)
        self.list.mouseDoubleClickEvent = lambda event: self.listclick()

        # Pengaturan Layout dari widgets
        vb = QVBoxLayout()
        vb.addWidget(menu)
        vb.addWidget(self.judul)
        vb.addWidget(self.slide)
        vb.addLayout(hb)
        vb.addWidget(self.list)
        self.setLayout(vb)

        # Menghubungkan method-method dengan tombol
        self.playButton.clicked.connect(self.playclick)
        self.pauseButton.clicked.connect(self.pauseclick)
        self.stopButton.clicked.connect(self.stopclick)
        self.nextButton.clicked.connect(self.nextclick)
        self.prevButton.clicked.connect(self.prevclick)

        # Sinkronisasi antara slider dengan player
        self.slide.sliderMoved.connect(self.slidemove)

        self.player.positionChanged.connect(self.playerchange)
        self.player.durationChanged.connect(self.durationchange)
        self.player.mediaStatusChanged.connect(self.repeat)

    def repeat(self, state):
        if state == QMediaPlayer.EndOfMedia:
            self.nextclick()

    def mode(self, kondisi):
        if kondisi:
            self.playButton.setEnabled(False)
            self.pauseButton.setEnabled(True)
            self.stopButton.setEnabled(True)
        else:
            self.playButton.setEnabled(True)
            self.pauseButton.setEnabled(False)
            self.stopButton.setEnabled(False)

    # noinspection PyCallByClass,PyTypeChecker
    def openfile(self, text):
        print(text)
        filename = QFileDialog.getOpenFileNames(self, 'Open File', '', 'MP3 Files (*.mp3)')
        if not filename[0]: return
        for index in range(len(filename[0])):
            self.filename.append(filename[0][index])
            (dirname, nama) = os.path.split(filename[0][index])
            self.list.addItem(nama[:len(nama) - 4])
            print('Adding ' + nama[:len(nama) - 4])

    def playclick(self):
        try:
            if self.player.state() != QMediaPlayer.PausedState:
                if self.list.currentRow() == -1:
                    self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[0])))
                    self.list.setCurrentRow(0)
                else:
                    self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
                print('Playing ' + self.list.currentItem().text())
                self.judul.setText(self.list.currentItem().text())
            else:
                self.list.setCurrentRow(self.pausindex)
                print('Playing ' + self.judul.text() + ' at %d' % self.player.position())
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
        print('Pause at %d' % self.player.position())
        self.pausindex = self.list.currentRow()
        self.player.pause()
        self.mode(False)

    def stopclick(self):
        print('Stop')
        self.player.stop()
        self.mode(False)

    def nextclick(self):
        try:
            self.list.setCurrentRow(self.list.currentRow() + 1)
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
            self.list.setCurrentRow(self.list.currentRow() - 1)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename[self.list.currentRow()])))
            self.player.play()
            self.judul.setText(self.list.currentItem().text())
            print('Prev, Playing ' + self.list.currentItem().text())
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
    # noinspection PyCallByClass
    # a.setStyle(QStyleFactory.create('Windows'))
    b = Music()
    a.exec_()