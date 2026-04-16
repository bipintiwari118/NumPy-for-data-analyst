#NumPy - Creating Arrays with Dimensions
#the shape of an array is the number of elements in each dimension. The shape of an array is represented as a tuple of integers. The number of dimensions is called the rank of the array. The size of an array is the total number of elements in the array. The size of an array can be calculated by multiplying the dimensions together.
#the array object in numpy is called ndarray. The ndarray object has a method called shape that returns the shape of the array. The shape of an array can be changed using the reshape method. The reshape method takes a tuple of integers as an argument and returns a new array with the specified shape. The reshape method does not change the data in the array, it only changes the shape of the array.
import numpy as np


x=np.array([1, 2, 3, 4, 5])
print(x)
print(type(x))


y=np.array((1, 2, 3, 4, 5))
print(y)
print(type(y))



#2-D Array
a=np.array([[1, 2, 3], [4, 5, 6]])
print(a)


# 3-D Array
b=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(b)


print("dimensions of x:", x.ndim)
print("dimensions of a:", a.ndim)
print("dimensions of b:", b.ndim)



#Indexing, Accessing Array Elements
#In NumPy, you can access elements of an array using indexing. The indexing starts from 0. You can access elements of a 1-D array using a single index, elements of a 2-D array using two indices, and elements of a 3-D array using three indices.

#1-D Array
print(x[0]) #accessing the first element of the array
print(x[1]) #accessing the second element of the array
print(x[2]) #accessing the third element of the array


#2-D Array
print(a[0,0]) #accessing the first element of the first row
print(a[0,1]) #accessing the second element of the first row
print(a[0,2]) #accessing the third element of the first row
print(a[1,0]) #accessing the first element of the second row
print(a[1,1]) #accessing the second element of the second row
print(a[1,2]) #accessing the third element of the second row

#3-D Array
print(b[0,0,0]) #accessing the first element of the first row of the first layer
print(b[0,0,1]) #accessing the second element of the first row of the first layer
print(b[0,0,2]) #accessing the third element of the first row of the first layer
print(b[0,1,0]) #accessing the first element of the second row of the first layer
print(b[0,1,1]) #accessing the second element of the second row of the first layer
print(b[0,1,2]) #accessing the third element of the second row of the first layer
print(b[1,0,0]) #accessing the first element of the first row of the second layer
print(b[1,0,1]) #accessing the second element of the first row of the second layer
print(b[1,0,2]) #accessing the third element of the first row of the second layer
print(b[1,1,0]) #accessing the first element of the second row of the second layer
print(b[1,1,1]) #accessing the second element of the second row of the second layer
print(b[1,1,2]) #accessing the third element of the second row of the second layer

print(b[1,1,2]) #accessing the third element of the second row of the second layer using a single index