from os.path import isdir, isfile
import os
import shutil

dst = 'dst'

if isdir(dst):              #<---- 1
    shutil.rmtree(dst)      #<---- 2
elif isfile(dst):
    os.unlink(dst)
