
def sed(pattern_str, replacem_str, file1, file2):
    """ Reads strings from file1 and writes them in file2 (created/modified).
        The written string has all occurrences of pattern_str replaced with replacem_str."""

    try:                                                    # catching & handling an exception
        fin = open(file1)
    except:
        print(f'unable to open {file1}. ending program.')
        return

    fin = open(file1, 'r')
    fout = open(file2, 'w')

    for line in fin:                                        # reading, replacing, & writing line by line
        line = line.replace(pattern_str, replacem_str)
        fout.write(line)

    fin.close()
    fout.close()
    print('data transferred successfully.')


file_in = '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/mother.txt'
file_out = '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/daughter.txt'
sed('ll', 'r', file_in, file_out)
