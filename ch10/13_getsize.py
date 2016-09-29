import os
import os.path

def get_all_files(target_dir):
    '주어진 디렉토리의 모든 파일 목록과 파일 사이즈를 반환한다.'
    ret = []
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            # 파일명
            cur_file = os.path.join(root, f)
            # 파일 사이즈
            file_size = os.path.getsize(cur_file)
            ret.append((cur_file, file_size))
    # 결과 반환
    return ret

for item in get_all_files('.'):
    print("{} : {} Bytes".format(item[0], item[1]))
