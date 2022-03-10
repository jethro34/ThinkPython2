import os


def walk(directory, level=4):
    in_dir = os.listdir(directory)
    files = []
    subdirs = []
    if in_dir:
        for smth in in_dir:
            if os.path.isfile(directory + '/' + smth):
                files.append(smth)
            else:
                subdirs.append(smth)
        if files:
            print(" " * level + "files in" + directory + ":")
            for file in files:
                print(" " * level * 2 + file)
        if subdirs:
            print(" " * level + "directories in" + directory + ":")
            for subdir in subdirs:
                print(" " * level * 2 + subdir)
                level += 4
                walk(directory + "/" + subdir, level)
                level -= 4
    else:
        print(" " * level + directory, "is empty!")
    return None


path = '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS'
walk(path)
