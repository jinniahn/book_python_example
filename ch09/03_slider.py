#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 가로 슬라에더 생성
        self.slider = QSlider(Qt.Horizontal, self)  #<---- 1
        self.slider.setMaximum(1000)                #<---- 2
        self.slider.setMinimum(0)                   #<---- 3

        # 위치와 크기
        self.slider.setGeometry(30, 40, 100, 30)

        # 시그널 연결
        self.slider.valueChanged[int].connect(self.changeValue)  #<---- 4

        # 라벨 생성
        self.label = QLabel("current : 0", self)    #<----- 5
        self.label.setGeometry(30,70, 100, 30)

        # 윈도우 위치
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider Example')
        self.show()


    def changeValue(self, value):                  #<----- 6
        "슬라이더 값 출력"
        self.label.setText("current : {}".format(value))  #<----- 7


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
