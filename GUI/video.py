import sys, time
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class video(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer(self)
        self.setup()

    def setup(self):
        self.resize(1350, 690)
        self.setWindowTitle('Video Player')
        self.setWindowIcon(QIcon('video.ico'))

        self.splash = QSplashScreen(QPixmap('sadayo.png'), QtCore.Qt.WindowStaysOnTopHint)
        self.splash.show()
        time.sleep(5)
        self.splash.close()

        self.video = QVideoWidget()
        self.video.setCursor(QCursor(Qt.BlankCursor))

        self.player.setVideoOutput(self.video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setEnabled(False)

        self.menu = QMenuBar()
        self.menu.adjustSize()
        self.menu.setFixedHeight(20)
        file = self.menu.addMenu('File')
        open = QAction('Open File', self)
        open.setShortcut('CTRL+O')
        open.triggered.connect(self.buka)
        file.addAction(open)

        self.play = QPushButton('Play')
        self.play.setEnabled(False)
        self.play.setShortcut('E')
        self.play.setToolTip('Untuk memutar / memutar kembali video')
        self.pause = QPushButton('Pause')
        self.pause.setEnabled(False)
        self.pause.setShortcut('R')
        self.pause.setToolTip('Untuk menjeda video')
        self.stop = QPushButton('Stop')
        self.stop.setEnabled(False)
        self.stop.setShortcut('W')
        self.stop.setToolTip('Untuk menghentikan video')
        self.next = QPushButton('Next')
        self.next.setEnabled(True)
        self.next.setShortcut('T')
        self.next.setToolTip('Untuk memajukan 10 detik')
        self.prev = QPushButton('Prev')
        self.prev.setEnabled(True)
        self.prev.setShortcut('Q')
        self.prev.setToolTip('Untuk mengembalikan 10 detik')

        hbox = QHBoxLayout()
        hbox.addWidget(self.prev)
        hbox.addWidget(self.stop)
        hbox.addWidget(self.play)
        hbox.addWidget(self.pause)
        hbox.addWidget(self.next)
        hbox.addStretch()

        layout = QGridLayout()
        layout.addWidget(self.menu, 0, 0)
        layout.addWidget(self.video, 1, 0)
        layout.addWidget(self.slider, 2, 0)
        layout.addLayout(hbox, 3, 0)
        self.setLayout(layout)

        self.play.clicked.connect(self.played)
        self.pause.clicked.connect(self.paused)
        self.stop.clicked.connect(self.stoped)
        self.next.clicked.connect(self.nexted)
        self.prev.clicked.connect(self.preved)

        self.slider.sliderMoved.connect(self.moved)
        self.player.positionChanged.connect(self.playposition)
        self.player.durationChanged.connect(self.playduration)


    def setmode(self, mode):
        if mode:
            self.play.setEnabled(False)
            self.pause.setEnabled(True)
            self.stop.setEnabled(True)
        else:
            self.play.setEnabled(True)
            self.pause.setEnabled(False)
            self.stop.setEnabled(False)

    def buka(self):
        nama = QFileDialog.getOpenFileName(self, 'Pilih File', 'D:\\', 'MP4 Files (*.mp4);; AVI Files (*.avi);; MKV Files (*.mkv)')
        if len(nama[0])>0:
            self.slider.setEnabled(True)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(nama[0])))
            if self.player.state()== QMediaPlayer.PlayingState:
                self.player.stop()
            self.played()

    def played(self):
        self.player.play()
        print('Play')
        self.setmode(True)

    def paused(self):
        self.player.pause()
        print('Pause')
        self.setmode(False)

    def stoped(self):
        self.player.stop()
        print('Stop')
        self.setmode(False)

    def nexted(self):
        self.player.setPosition(self.player.position()+10000)
        print('Next')

    def preved(self):
        self.player.setPosition(self.player.position()-10000)
        print('Prev')

    def moved(self):
        self.player.setPosition(self.slider.value())
        print('Moved')

    def playposition(self, position):
        self.slider.setValue(position)

    def playduration(self, duration):
        self.slider.setMaximum(duration)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = video()
    b.show()
    a.exec_()