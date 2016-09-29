import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit,
                             QPushButton,QGridLayout, QApplication)


class GridExample(QMainWindow):

    def __init__(self):
        super().__init__()

        # 라벨들
        title   = QLabel('Title')
        writer  = QLabel('Writer')
        comment = QLabel('Comment')

        # 데이터 입력하는 위쳇들
        titleEdit   = QLineEdit()
        writerEdit  = QLineEdit()
        commentEdit = QTextEdit()

        # 버튼
        confirm     = QPushButton("Confirm")

        # Layout
        grid = QGridLayout()                  #<---- 1
        grid.setSpacing(10)                   #<---- 2 

        grid.addWidget(title, 0, 0)           #<---- 3
        grid.addWidget(titleEdit, 0, 1)       #<---- 4

        grid.addWidget(writer, 1, 0)
        grid.addWidget(writerEdit, 1, 1)

        grid.addWidget(comment, 2, 0)
        grid.addWidget(commentEdit, 2, 1, 4, 1)

        grid.addWidget(confirm, 6,0)

        window = QWidget() 
        window.setLayout(grid)
        self.setCentralWidget(window)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())
