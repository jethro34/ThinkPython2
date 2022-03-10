
import os
import hashlib


def md5(filename):
    """ Returns the md5sum of a file.
        Output: hex string """
    print('generating md5 for', filename)
    with open(filename, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


def create_paths_list(directory, suffix):
    """ Creates a list of suffix-ending files in directory and its subdirectories."""

    temp = os.walk(directory)
    for direct, _, filenames in temp:
        for file in filenames:
            if suffix in file:
                abs_path = os.path.join(direct, file)
                files.append((abs_path, md5(abs_path)))
    print('paths list created')


def take_sec(item):
    return item[1]


def search4dup(liste):
    """ Searches for duplicate files in a list of filepaths. """

    print('searching for duplicate files...')
    temp = sorted(liste, key=take_sec)
    for i in range(len(temp) - 1):
        if temp[i][1] == temp[i + 1][1]:
            dupl_files.setdefault(temp[i][1], {temp[i][0]}).add(temp[i + 1][0])


files = []
dupl_files = {}

path = '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/Pictures'
create_paths_list(path, '.jpg')
search4dup(files)
if dupl_files:
    for values in dupl_files.values():
        print(values)
else:
    print('no duplicate files found.')
