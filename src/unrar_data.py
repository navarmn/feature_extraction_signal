import os
import sys

# add source code to this python path
sys.path.insert(0, '../src/')

folderIn = '../data/raw/'
folderOut = '../data/interim/'

files = []
for (dirpath, dirnames, filenames) in os.walk(folderIn):
    files.extend(filenames)

for file in files:
    input_path = '../data/raw/' + file
    command = 'unrar x -o+ {} {}'.format(input_path, folderOut)
    print(command)
    os.system(command)
