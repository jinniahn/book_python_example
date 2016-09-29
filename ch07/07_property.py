class Rectangle(object):
    def __init__(self, w, h):
        self._width = w
        self._height = h

    def getArea(self):
        return self._width * self._height

    @property            #<---- 1
    def width(self):     #<---- 2
        return self._width   #<---- 3

    @width.setter        #<---- 4
    def width(self, w):  #<---- 5
        self._width = max( 10, min(100, self._width) )

    @property  
    def height(self): 
        return self._height

    @height.setter
    def height(self, h):
        self._height = max( 10, min(100, self._height) )
        
r1 = Rectangle(10, 10)

r1.width = 100        #<--- 6
print("rectangle({}, {})".format(r1.width, r1.height)) #<---- 7

print("area : {}".format(r1.getArea()))
