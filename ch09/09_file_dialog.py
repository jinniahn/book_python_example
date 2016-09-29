#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QTextEdit, QFileDialog,
                             QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('Dialog', self)              #<---- 1
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)           #<---- 2

        self.textEdit = QTextEdit(self)                     #<---- 3
        self.textEdit.setGeometry(20, 60, 450, 180) 
        
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Dialog')
        self.show()
        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')  #<---- 4
        # return : ('<filename>', '') 
        if fname[0]:                                        #<---- 5
            with open(fname[0], 'r') as f:                  #<---- 6
                data = f.read()
                self.textEdit.setText(data)                 #<---- 7
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
