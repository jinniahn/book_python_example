class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def getArea(self):
        return self.width * self.height

    def setWidth(self, w):
        self.width = max( 10, min(100, self.width) )
     
r1 = Rectangle(10, 10)

r1.setWidth(1000)            #<---- 1

print("area : {}".format(r1.getArea()))
