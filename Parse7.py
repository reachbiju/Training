name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dc =dict()
for line in handle:
    wds=line.split()
    if len(wds) < 1 : continue # Skip Empty lines
    if not wds[0].startswith('From'): continue # Skip all except From

    if len(wds[1]) > 0: #Skip empty words
        #Retrieve, Create and Update Dictionay
        dc[wds[1]]=dc.get(wds[1],0)+1

largest = -1
common = None
for k,v in dc.items():
    print(k,v)
    if v > largest:
        largest = v
        common = k


print(dc)
print ("------")
print(largest,common)
