largest = None
smallest = None
while True:
    num1 = input("Enter a number: ")

    if num1 == "done" : break
    try:

        num=int(num1)
    except:
        print("Invalid Input")
        continue
    # Setting smallest
    if smallest is None:
        smallest = num
    else:
        if num < smallest:
            smallest = num
    #Setting largeset
    if largest is None:
        largest = num
    else:
        if num > largest:
            largest = num
    #print(largest)


print("Maximum", largest)
print("Minimum", smallest)
