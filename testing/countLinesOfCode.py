import sys
import os

def get_wordcount(start_path):
    count = 0
    for paths, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(paths, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                f = open(fp, "r")
                for line in f:
                    count += 1
    return count

for i in range(1, len(sys.argv)):
    name = sys.argv[i].split("/")
    if name[len(name)-1] != "":
        print('folder name:', name[len(name)-1], '-', get_wordcount(sys.argv[i]), 'lines')
    else:
        print('folder name:', name[len(name)-2], '-', get_wordcount(sys.argv[i]), 'lines')
