def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if __name__ == '__main__':
    print(linecount('/Users/hejtor/PycharmProjects/ThinkPython2/p173_wc.py'))
