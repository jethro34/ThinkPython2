fout = open('/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/output.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)

x = 52
fout.write(str(x))

camels_number = 42

fout.write('%d\n' % camels_number)

fout.write("I have spotted %d camels.\n" % camels_number)

fout.write("In %d years I have spotted %g %s." % (3, 0.1, 'camels'))


fout.close()
