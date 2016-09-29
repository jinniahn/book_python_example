import subprocess
import fcntl               #<---- 1
import os
import time

# 10초간 ping 수행
cmd = ["ping","-t", "10", "www.google.com"]

# 프로세스 시작
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)  #<---- 2

# 파이프의 속성 값을 논블럭으로 설정
fd = p.stdout.fileno()                #<---- 3
fl = fcntl.fcntl(fd, fcntl.F_GETFL)   #<---- 4
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)  #<---- 5

# 프로세스가 종료할때까지 주기적으로 읽는다.
while(True):
    data = p.stdout.readline().decode()   #<---- 6
    if data:
        print(data)

    time.sleep(0.5)

    # 프로세스가 종료되었는지 확인
    if p.poll() != None:                  #<---- 7
        break;
