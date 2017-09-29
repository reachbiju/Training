fname = "Romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    for l in line.split():
        print(l)
    #lst.sort()
    #print(lst)
