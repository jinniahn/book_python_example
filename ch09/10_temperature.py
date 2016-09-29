import random
from PyQt5.QtCore import pyqtSignal, QObject

class Temperature(QObject):
    # 정의
    changed = pyqtSignal(float, name='temperatureChanged')

    def __init__(self):
        super().__init__()

    def measure(self):
        # 이벤트 발생
        rand_temp = random.randint(10,50)
        self.changed.emit(rand_temp)



# 핸들러 연결:
def print_temperature(val):
    print('current temperature : {}'.format(val))

t = Temperature()
t.changed.connect(print_temperature)


# 온도 측정
t.measure()
t.measure()
