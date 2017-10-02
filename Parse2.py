#Slicing
x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters

x[-1] #return the last element of the string.
x[-4:-2] #  return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
x[:3] # slice from the beginning of the string and stopping before the 3rd element.
x[3:] #this is a slice starting from the 4th element of the string and going all the way to the end.

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list


