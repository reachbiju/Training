
fname = "Romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    for l in line.split():
        #print(l)
        if l not in lst:
            print("Append")
            lst.append(l)

    lst.sort()
    print(lst)
