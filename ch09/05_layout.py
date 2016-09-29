import sys
from PyQt5.QtWidgets import ( QWidget, QMainWindow, QLabel,QApplication,
                              QPushButton, QHBoxLayout, QVBoxLayout )

class LayoutExample2(QMainWindow):

    def __init__(self):
        super().__init__()

        # 사용한 위젯들을 생성
        lbl1 = QLabel('This is')          #<---- 1
        lbl2 = QLabel('Layout Example')

        okButton = QPushButton("OK")   
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()      #<---- 2
        hbox.addStretch(1)        #<---- 3
        hbox.addWidget(okButton)  #<---- 4
        hbox.addWidget(cancelButton)  #<---- 5

        vbox = QVBoxLayout()      #<---- 6
        vbox.addWidget(lbl1)      #<---- 7
        vbox.addWidget(lbl2)      #<---- 8
        vbox.addLayout(hbox)      #<---- 9

        window = QWidget()        #<---- 10
        window.setLayout(vbox)    #<---- 11
        self.setCentralWidget(window)  #<---- 12

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Layout Example')    
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayoutExample2()
    sys.exit(app.exec_())
