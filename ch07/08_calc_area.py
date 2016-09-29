import math

class Shape(object):
    """도형

    도형의 넓이를 구하는 공통 API를 갖는다.
    """
    def __init__(self, name):
        self.name = name

    def calcArea(self):
        '넓이를 구하는 API. 상속 클래스에서 각각 구현해야 함'
        raise NotImplemented


class Circle(Shape):

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r 

    def calcArea(self):
        return self.r * self.r * math.pi

class Quadrangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calcArea(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calcArea(self):
        return self.width * self.height / 2


def main():

    # 원, 사각형, 삼각형들을 리스트로 만든다.
    shapes = [ Circle('원', 2)
               , Quadrangle('사각형', 2,2)
               , Triangle('삼각형', 2,2) ]

    # 각 도형의 넓이를 구한다
    for s in shapes:
        print('{} : {}'.format(s.name, s.calcArea()))

main()
