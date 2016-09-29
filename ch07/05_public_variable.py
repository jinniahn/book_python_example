class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def getArea(self):
        return self.width * self.height

    
r1 = Rectangle(10, 10)
r1.width = 1000            #<---- 1

print("area : {}".format(r1.getArea()))
