import os
cwd = os.getcwd()
print(cwd)

path_to = os.path.exists('/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/output.txt')
print(path_to)

path_to = os.path.isfile('/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/output.txt')
print(path_to)

in_dir = os.listdir('/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/')
print(in_dir)
