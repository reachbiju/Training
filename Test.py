fname = input("Enter file name: ")
eMail = open(fname)
for item in eMail:
    itemx= item.split()
    if not item.startswith('To'): continue
    print(itemx[0])
