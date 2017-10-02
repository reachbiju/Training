
#fname = input("Enter file name: ")
fname=""
if len(fname) < 1 : fname = "mbox-short.txt"
eMail = open(fname)
count = 0
lst =  list()
for line in eMail:
    wds=line.split()
    if (len(wds)) < 1 : continue #Guardian logic to protect error space
    if not wds[0].startswith('From'): continue
    if wds[1] not in lst:
        lst.append(wds[1])
        count = count + 1
print(lst)
print("There were", count, "lines in the file with From as the first word")
