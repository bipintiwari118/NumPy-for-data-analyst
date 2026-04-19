# NumPy Array Copy and View
# In NumPy, there are two ways to create a new array from an existing array: copy and view. A copy creates a new array with the same data as the original array, while a view creates a new array that shares the same data as the original array. The difference between a copy and a view is that a copy is independent of the original array, while a view is dependent on the original array. When you modify a copy, it does not affect the original array, but when you modify a view, it affects the original array.

import numpy as np

x=np.array([1, 2, 3, 4, 5])
print(x)
y=x.copy()
print(y)

z=x.view()
print(z)
x[0]=101
print(x)
print(z)
print(y)




#NumPy Array Shape
# The shape of an array is the number of elements in each dimension of the array. The shape of an array can be accessed using the shape attribute. The shape of an array can be changed using the reshape method. The reshape method takes a tuple as an argument and returns a new array with the specified shape. The reshape method does not change the data in the array, it only changes the shape of the array.

x=np.array([1, 2, 3, 4, 5])
print(x.shape)


y=np.array([[1, 2, 3], [4, 5, 6]])
print(y.shape)


z=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(z.shape)


p=np.array([[[1, 2, 3, 4, 5], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26]]])
print(p.shape)