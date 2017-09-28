# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos1=line.find(":")
    pos2=line.find("\n")
    line2= float(line[pos1+1:pos2])
    count=count+1
    tot= tot+ line2
#    print(line)
#    print(line2)
avg=tot/count
avg1=str(avg)
print("Average spam confidence: " + avg1)
#print("Done")
