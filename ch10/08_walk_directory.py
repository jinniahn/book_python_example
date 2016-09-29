import os
import os.path

# ~/logs 디렉토리를 조회하겠다.
root_dir = os.path.expanduser("~/logs")

# walk 결과는 현재 디렉토리, 내부 디렉토리명들, 파일명들 임.
for root, dirs, files in os.walk(root_dir):     #<---- 1
    # 디렉토리들
    for d in dirs:                              #<---- 2
        print("[D] {}/{}".format(root, d))      #<---- 3
    # 파일들
    for f in files:                             #<---- 4
        print("[F] {}/{}".format(root, f))      #<---- 5
