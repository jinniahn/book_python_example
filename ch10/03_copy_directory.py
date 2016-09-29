import os
import os.path
import shutil

# 목적 디렉토리가 기존에 없어야 한다.
if os.path.exists('dst'):
    if os.path.isdir('dst'):
        # 디렉토리이면 rmtree로 제거
        shutil.rmtree('dst')
    else:
        # 파일이면 unlink로 제거
        os.unlink('dst')

# 제외한 파일 패턴        
ignore=shutil.ignore_patterns(['*.txt', '~*'])

# 디렉토리 복사
shutil.copytree('../../../src_dir', 'dst', ignore=ignore)
