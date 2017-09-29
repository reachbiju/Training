<<<<<<< HEAD

members=['biju','rincy','nora']
for item in range(len(members)):
    name=members[item]
    print("Happy Birthday: ", name)
=======
fname = input("Enter file name: ")
eMail = open(fname)
for item in eMail:
    itemx= item.split()
    if not item.startswith('To'): continue
    print(itemx[0])
>>>>>>> bf1d056c3ee05568fa22485c1ebe95a21cdee56a
