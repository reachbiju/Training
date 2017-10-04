fname = input("Enter file name: ")
fh = open(fname)
for item in fh:
    itemx= item.rstrip()
    print(itemx.upper())
