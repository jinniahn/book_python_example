import os
import os.path

target_dir = os.path.expanduser('~/local')   #<---- 1

# 최종 크기
dir_size = 0

# 모든 디렉토리를 다 조회한다.
for root, dirs, files in os.walk(target_dir):   #<---- 2
    for f in files:

        # 파일 경로를 만든다.
        fpath = os.path.join(root, f)           #<---- 3

        # 파일이면 파일크기 구함
        if os.path.isfile(fpath):               #<---- 4
            dir_size += os.path.getsize(fpath)  #<---- 5


# 크기를 MiB 단위로 출력
print("{} : {} MiB".format(target_dir, round(dir_size / 1024 / 1024)))
