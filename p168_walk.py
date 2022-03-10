# print names of files and subdirectories in a given directory

import os

directory = '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS'

root, dirs, files = next(os.walk(directory))                            # getting first item for generator
subdirs = [os.path.join(root, sd) for sd in dirs if sd]
infiles = [os.path.join(root, file) for file in files if file and file != '.DS_Store']

print('directory:')
print('\t', directory)

print('subdirectories:')
for sd in subdirs:
    print('\t', sd)

print('files:')
for file in infiles:
    print('\t', file)
