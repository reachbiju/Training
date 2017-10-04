#Tuples are an immutable data structure (cannot be altered).
x = (1, 'a', 2, 'b')
type(x)

#Lists are a mutable data structure
x = [1, 'a', 2, 'b']
type(x)
#Use append to append an object to a list.
x.append(3.3)
print(x)
# how to loop through each item in the list.
for item in x:
    print(item)
#Use + to concatenate lists.    
[1,2] + [3,4]
#Use * to repeat lists
[1]*3

#Dictionaries associate keys with values.
x = {'Biju': 'boommen7@gmail.com', 'Rincy': 'rincy814@gmail.com'}
x['Biju'] # Retrieve a value by using the indexing operator
#Iterate over all of the keys:
for name in x:
    print(x[name])

#Iterate over all of the values:
for email in x.values():
    print(email)


