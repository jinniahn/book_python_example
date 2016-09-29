import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication

class LayoutExample1(QMainWindow):

    def __init__(self):
        super().__init__()

        lbl1 = QLabel('This is', self)
        lbl1.move(20, 50)                       #<---- 1

        lbl2 = QLabel('Not Layout Example', self)
        lbl2.move(50, 70)                       #<---- 2

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Layout Example')    
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayoutExample1()
    sys.exit(app.exec_())
