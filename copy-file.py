# copyile() = copies the contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copied metadata

import shutil
# src.destination
shutil.copyfile('text.txt', 'copy.txt')