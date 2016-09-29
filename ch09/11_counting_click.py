#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, qApp

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 카우팅을 위해 변수 초기화
        self.click_count = 0

        # 라벨로 현재 카운팅 값 표시
        self.lbl_count = QLabel('Click : 0', self)
        self.lbl_count.move(20, 50)

        # 윈도우를 표시한다.
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Count Click')
        self.show()

    def update(self):
        # setText() 메소드를 써야지 화면에 표시됨
        self.lbl_count.setText('Click : {}'.format(self.click_count))

    # 마우스를 누르면 closeApp 이벤트 발생
    def mousePressEvent(self, event):
        self.click_count += 1
        self.update();
        print(self.click_count)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
