# from: http://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files

import os

for path, subdirs, files in os.walk('c:\\'):
    for name in files:
        print(os.path.join(path, name))

   