import numpy as np
#Create a list and convert it to a numpy array
mylist = [1,2,3]
x=np.array(mylist)
y=np.array([4,5,6]) #Or just pass in a list directly
m=np.array([[7,8,9],[10,11,12]]) # create a multidimensional array.
m.shape #find the dimensions of the array. (rows, columns)
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
n=n.reshape(3,5) #reshape returns an array with the same data with a new shape.
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
o.resize(3, 3) #resize changes the shape and size of array in-place
np.ones((3, 2)) #ones returns a new array of given shape and type, filled with ones
np.zeros((2, 3)) #zeros returns a new array of given shape and type, filled with zeros.
np.eye(3) #eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
np.diag(y) #diag extracts a diagonal
np.array([1, 2, 3] * 3) #Create an array using repeating list (or see np.tile)
p = np.ones([2, 3], int)
np.vstack([p, 2*p]) #Use vstack to stack arrays in sequence vertically (row wise).

