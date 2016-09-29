import shutil
import os
import os.path

# dst 디렉토리가 없으면 생성
if not os.path.exists('dst'):
    os.makedirs('dst')

# 파일을 dst 디렉토리에 복사
shutil.copy2('sample.py', 'dst')
