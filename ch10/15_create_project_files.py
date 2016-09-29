import os
import shutil

# LICENSE 파일 생성
open('LICENSE','w').close()
with open('README.md','w') as f:
    f.write("This is readme.md file")

os.makedirs('doc')
os.makedirs('src')

open('doc/README.md','w').close()
open('src/app.py','w').close()
