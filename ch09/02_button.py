q#!/usr/bin/python3
# -*- coding: utf-8

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        button = QPushButton('Push Me', self)    #<---- 1
        button.move(10, 10)                      
        button.clicked.connect(self.message)     #<---- 2
        button.clicked.connect(message2)         #<---- 3

        self.show()

    def message(self):                           #<---- 4
        msg = QMessageBox(self)
        msg.setText("You Push Me.")
        msg.show()

def message2():                                  
    print("push me")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
