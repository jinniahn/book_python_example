import os
import os.path

def get_all_files(target_dir):
    ret = []
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            # 절대 파일명
            cur_file = os.path.abspath(os.path.join(root, f))
            file_size = os.path.getsize(cur_file)

            # 비교를 위해서 target_dir과의 상태 경로를 계산
            relpath = os.path.relpath(cur_file, target_dir)
            ret.append((relpath, file_size))
    return ret
    
def show_diff_files(dir1, dir2):
    # 경로를 키로 하고 파일 사이즈를 값으로는 사전을 만든다.
    files1 = dict(get_all_files(dir1))
    files2 = dict(get_all_files(dir2))

    # 일단 파일명이 완전히 다른 파일명들을 출력한다.
    for k in set(files1.keys()) - set(files2.keys()):
        print(" - {}".format(k))
    for k in set(files2.keys()) - set(files1.keys()):
        print(" - {}".format(k))
    # 파일명은 동일한데 사이즈가 다른 경우
    for k in set(files1.keys()) & set(files2.keys()):
        if files1[k] != files2[k]:
            print(" - {}".format(k))


# 테스트로 두개의 디렉토리를 만들어 확인하자.
show_diff_files('test_dir1', 'test_dir2')
