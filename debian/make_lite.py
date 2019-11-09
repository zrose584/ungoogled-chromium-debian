#!/usr/bin/env python3

import os
import sys
import shutil

lines = open(sys.path[0] + '/make_lite_list.txt').read().splitlines()

me = 'debian/' + os.path.basename(__file__)

print("[{}] deleting {} unnecessary files/directories ...".format(me, len(lines)))

n_files = 0
n_dirs = 0

for file in lines:
    if file[0] == '#':
        continue

    abs_file = sys.path[0] + '/../' + file

    if os.path.isfile(abs_file):
        n_files += 1
        os.remove(abs_file)
        print("removed file: {}".format(file))
    elif os.path.isdir(abs_file):
        n_dirs += 1
        shutil.rmtree(abs_file)
        print("removed directory: {}".format(file))
    #else:
    #    print("[{}] no such file: {}".format(me, file))

print("[{}] deleted {} directories and {} files".format(me, n_dirs, n_files))
