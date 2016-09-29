class OwnerError(Exception):        #<---- 1
    def __init__(self, message):    #<---- 2
        self.message = message      #<---- 3

class MyError(Exception): pass      #<---- 4

try:
    raise OwnerError("조용히 하세요.")

except OwnerError as e:             #<---- 5
    print("사장님 말씀 : ", e.message)  #<---- 6
