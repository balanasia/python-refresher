import os
import shutil

path = 'empty-folder'

try:
    os.rmdir(path)
    # can remove non-empty folder
    # shutil.rmtree(path)
except FileNotFoundError:
    print("file not found :c")
except PermissionError:
    print("you do not have permisison do remove that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
