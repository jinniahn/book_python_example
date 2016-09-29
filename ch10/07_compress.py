import os, stat
import shutil
import subprocess

def backup_filename(prefix):
    '''백업 파일 이름 생성.

    파일 형식: <prefix>_날짜

    Usage:
    >>> backup_filename('test')
    test_20160101
    '''

    from datetime import date
    today = date.today()
    return prefix + today.strftime('_%Y%m%d')

backup_fname = backup_filename('nginx-log')  <---- 1
root_dir = os.path.expanduser('~/logs')      <---- 2
shutil.make_archive(backup_fname, 'gztar'
, root_dir=root_dir
, base_dir='nginx/') #<---- 3

# 생성된 tar 파일 목록 보기
print('file name : ', backup_fname)  
subprocess.call('tar -tzvf {}.tar.gz'.format(backup_fname)
                , shell=True) #<--- 4
