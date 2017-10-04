try:
    f = open('mylog.txt','w')
    f.write("Message1 \n")
    f.close()
   # raise RuntimeError('this silly error')
    f = open ('mylog2.txt','r')
    for item in f:
        print(item)    
except RuntimeError:
    print("Error for Control M ")




