import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 초기화
        self.initUI()                           #<---- 1

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)    #<---- 2
        self.setWindowTitle('HelloWindow')      #<---- 3
        self.show()                             #<---- 4

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWindow()                          #<---- 5
    sys.exit(app.exec_())                       #<---- 6
