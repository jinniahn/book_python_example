import shutil

# 파일 이름 변경
shutil.move('filename', 'new_filename')   #<---- 1

# 디렉토리 이동
# dir_a 디렉토리를 상위 디렉토리로 이동한다.
shutil.move('dir_a', '../dir_a')          #<---- 2
