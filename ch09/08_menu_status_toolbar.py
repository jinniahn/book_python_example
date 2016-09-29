#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import ( QMainWindow, QAction, qApp,
                              QApplication, QFileDialog )
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.click_count = 0               #<---- 1

        # Menu
        self.init_menu()                   #<---- 2
        self.init_toolbar()

        self.print_on_statusbar('.')
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Example')    
        self.show()

    def init_menu(self):                                      #<---- 3
        openFile = QAction(QIcon('open.png'), 'Open', self)   #<---- 4
        openFile.setShortcut('Ctrl+O')                        #<---- 5
        openFile.setStatusTip('Open new File')                #<---- 6
        openFile.triggered.connect(self.onShowDialog)         #<---- 7
        
        menubar = self.menuBar()                              #<---- 8
        fileMenu = menubar.addMenu('&File')                   #<---- 9
        fileMenu.addAction(openFile)                          #<---- 10

    def init_toolbar(self):
        #툴바 아이템 생성
        exitAction = QAction(QIcon('close.png'), 'Exit', self)  #<---- 11
        exitAction.setShortcut('Ctrl+Q')                        #<---- 12
        exitAction.triggered.connect(qApp.quit)                 #<---- 14

        printAction = QAction('Click', self)                    #<---- 15                  
        printAction.triggered.connect(self.onClickButton)

        # 툴바
        self.toolbar = self.addToolBar('Exit')                  #<---- 16
        self.toolbar.addAction(exitAction)                      #<---- 17
        self.toolbar.addAction(printAction)
    

    def print_on_statusbar(self, text):
        self.statusBar().showMessage(text)


    def onClickButton(self):
        self.click_count += 1
        self.statusBar().showMessage("clicked : {}".format(self.click_count))
        
    def onShowDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            self.print_on_statusbar('trying file : {}'.format(fname[0]))
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
