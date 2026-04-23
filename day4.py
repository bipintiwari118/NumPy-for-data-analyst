# NumPy Array Reshaping 
# The reshape method is used to change the shape of an array. The reshape method takes a tuple as an argument and returns a new array with the specified shape. The reshape method does not change the data in the array, it only changes the shape of the array.

import numpy as np
#for example
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a1=a.reshape(4,3)
print(a1)

a2=a.reshape(3,2,2)
print(a2)




#itrating array
#itrate the 1D array

b=np.array([1,2,3,4,5,6])
for i in b:
    print(i)

#itrate the 2D array
c=np.array([[1,2,3],[4,5,6]])
for i in c:
    print(i)  
    
    

#iterating array using the nditer()
    d=np.array([[[5,6,7],[8,9,10],[11,12,13]]])
    for i in np.nditer(d):
        print(i)
