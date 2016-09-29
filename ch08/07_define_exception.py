#예외정의
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

      
try:
    #예외발생
    raise MyException(‘예외 발생’)
except MyException as e:
    print(e.msg)
