class Book(object):
    """책 클래스.
    
    이 클래스는 책 정보를 위한 데이터이다.
    """

    def __init__(self, title, author):   #<---- 1
        """초기화.

        |name| 파라미터를 받아서 객체 맴버변수 name에 저장한다.
        """
        self.title = title               #<---- 2
        self.author = author
        self.borrowed = False

    def borrow(self):                    #<---- 3
        """책을 대여한다.

        책을 대여한다. 맴버변수 borrowed 변수에 
        현재 상태를 기록한다.
        """
        self.borrow = True               #<---- 4

    def takeBack(self):                  #<---- 5
        """책을 반납한다.
        """
        self.borrow = False

    def printInfo(self):                 #<---- 6
        log = []
        log.append("Book: ")
        log.append("   - title : {}".format(self.title))
        log.append("   - author : {}".format(self.author))
        log.append("   - borrowed : {}".format(self.borrowed))
        print('\n'.join(log))


b1 = Book(title="The Art of Computer Programming", author="도널드 크누스")  #<---- 7
b2 = Book(title="Design Patterns: Elements of Reusable Object-Oriented Software", author="The 'Gang of Four'")

b1.printInfo()  #<---- 8
