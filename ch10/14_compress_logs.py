import os, stat
import shutil
import subprocess

def backup_filename(prefix):
    '백업파일에 쓰일 파일명 반환'
    from datetime import datetime
    now = datetime.now()
    return prefix + now.strftime('%Y%m%d_%H%M')

backup_fname = backup_filename('backup_')
root_dir = os.path.expanduser('.')
shutil.make_archive(backup_fname, 'zip', root_dir=root_dir)
