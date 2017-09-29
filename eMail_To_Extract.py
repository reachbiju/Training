#Code Snippet to extract email receipients
fname="Workshop.txt"
eMail = open(fname)
for item in eMail:
    itemx= item.split(":")
    if not itemx[0].startswith('To'): continue
    itemy=itemx[1].split(";")
    for i in itemy:
        print(i.lstrip())
