
import os
import sys


# Script based on code
# https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python

def get_size(start_path):
    size = 0
    for paths, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(paths, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):   
                filename, file_extension = os.path.splitext(fp)
                if file_extension.lower() == ".md":
                    size += os.path.getsize(fp)
    return size


for i in range(1, len(sys.argv)):
    name = sys.argv[i].split("/")
    if name[len(name)-1] != "":
        print('folder name:', name[len(name)-1], '-', get_size(sys.argv[i]), 'bytes')
    else:
        print('folder name:', name[len(name)-2], '-', get_size(sys.argv[i]), 'bytes')


