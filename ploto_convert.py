
from sys import argv

with open(argv[1],'r') as file:
    lines = file.readlines()
    ignore = [i for i in range(len(lines))]
    ignore = ignore[::4]
    newlines = []
    for i in ignore[:-3]:
        for j in range(1,4):
            temp = lines[i+j].split()
            for vec in temp[:4]:
                newlines.append(vec+"\n")
    try:
        newfile = open("data/output_break_dp.txt",'w')
        newfile.writelines(newlines)
        newfile.close()
    except:
        print("error in writelines")

