from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import sys


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.resize(670,600)
        self.setWindowTitle("Renk Ayarı")
        self.bg =QLabel(self)
        self.bg.setGeometry(QtCore.QRect(0,0,1000,601))
        self.bg.setStyleSheet("background-color: rgb(200,200,200);")
        self.qslider1 = QScrollBar()
        self.qslider2 = QScrollBar()
        self.qslider3 = QScrollBar()
        self.qslider4 = QScrollBar()
        self.qslider5 = QScrollBar()
        self.yazi = QLabel("BLA BLA BLA")
        self.yazi.setAlignment(Qt.AlignCenter)
        self.renkodu= QLabel("")
        self.boyut= QFont("")
        self.yazi.setFont(QFont("Impact", 26, QFont.Bold))
        self.renkodu.setFont(QFont("Impact", 26, QFont.Bold))
        self.red_lbl = QLabel("Red")
        self.red_lbl.setFont(QFont("Impact", 16, QFont.Bold))
        self.red_lbl.setStyleSheet("background-color: rgb(255,0, 0, 200);")
        self.green_lbl =QLabel("Green")
        self.green_lbl.setFont(QFont("Impact", 16, QFont.Bold))
        self.green_lbl.setStyleSheet("background-color: rgb(0, 255, 0, 200);")
        self.blue_lbl = QLabel("Blue")
        self.blue_lbl.setFont(QFont("Impact", 16, QFont.Bold))
        self.blue_lbl.setStyleSheet("background-color: rgb(0,0,255);")
        self.transparan_lbl = QLabel("Transparan")
        self.transparan_lbl.setFont(QFont("Impact", 16, QFont.Bold))
        self.transparan_lbl.setStyleSheet("background-color: rgb(255,255,255,150);")
        self.yazi_boyut_lbl = QLabel ("Yazı Boyutu")
        self.yazi_boyut_lbl.setFont(QFont("Impact", 16, QFont.Bold))
        self.yazi_boyut_lbl.setStyleSheet("background-color: rgb(55,255,255,150);")






        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.renkodu)




        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.red_lbl)
        h_box2.addWidget(self.green_lbl)
        h_box2.addWidget(self.blue_lbl)
        h_box2.addWidget(self.transparan_lbl)
        h_box2.addWidget(self.yazi_boyut_lbl)


        v_box.addLayout(h_box2)

        h_box = QHBoxLayout()


        self.qslider1.setMaximum(255)
        self.qslider2.setMaximum(255)
        self.qslider3.setMaximum(255)
        self.qslider4.setMaximum(255)
        self.qslider5.setMaximum(100)

        h_box.addWidget(self.qslider1)
        h_box.addWidget(self.qslider2)
        h_box.addWidget(self.qslider3)
        h_box.addWidget(self.qslider4)
        h_box.addWidget(self.qslider5)

        v_box.addLayout(h_box)

        self.qslider1.sliderMoved.connect(self.yap)
        self.qslider2.sliderMoved.connect(self.yap)
        self.qslider3.sliderMoved.connect(self.yap)
        self.qslider4.sliderMoved.connect(self.yap)
        self.qslider5.sliderMoved.connect(self.yap)


        self.setLayout(v_box)
        self.show()

    def yap(self):
        self.renkodu.setText("RGB KODU : ( {}, {} ,{} , {} ) ".format(self.qslider1.value(), self.qslider2.value(),self.qslider3.value(), self.qslider4.value()))
        palette = QPalette()
        c = QColor(self.qslider1.value(), self.qslider2.value(), self.qslider3.value(), self.qslider4.value())
        palette.setColor(QPalette.Foreground, c)
        self.yazi.setPalette(palette)
        boy = self.qslider5.value()
        fontsize=self.qslider5.value()
        font = QFont("zaman", fontsize)
        self.yazi.setFont(font)






def main():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()






