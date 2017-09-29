<<<<<<< HEAD
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
=======
fname = "Romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    for l in line.split():
        print(l)
    #lst.sort()
    #print(lst)
>>>>>>> aef20c5df7abd73c04769e8987f388a5188d0f91
