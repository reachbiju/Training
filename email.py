fname = input("Enter file name: ")
eMail = open(fname)
for item in eMail:
    itemx= item.rstrip()
    print(itemx)
