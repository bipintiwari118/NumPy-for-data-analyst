#NumPy Data Types
#data types in NumPy are used to define the type of data that can be stored in an array. NumPy supports a wide range of data types, including integers, floats, booleans, and complex numbers. The data type of an array can be specified when creating the array or can be inferred from the data.
# i for integer, f for float, b for boolean, c for complex numbers. The data type of an array can be changed using the astype method. The astype method takes a data type as an argument and returns a new array with the specified data type. The astype method does not change the data in the array, it only changes the data type of the array.
# m for timedelta, M for datetime, O for object, S for string, U for unicode string, V for void. The data type of an array can be changed using the astype method. The astype method takes a data type as an argument and returns a new array with the specified data type. The astype method does not change the data in the array, it only changes the data type of the array.

# o for object, S for string, U for unicode string, V for void. The data type of an array can be changed using the astype method. The astype method takes a data type as an argument and returns a new array with the specified data type. The astype method does not change the data in the array, it only changes the data type of the array.

# u for unicode string, V for void. The data type of an array can be changed using the astype method. The astype method takes a data type as an argument and returns a new array with the specified data type. The astype method does not change the data in the array, it only changes the data type of the array.

import numpy as np


#checking the data type of an array
x=np.array([1, 2, 3, 4, 5])
print(x.dtype)


s=np.array(['a', 'b', 'c', 'd', 'e'])
print(s.dtype)


bipin=np.array(['kathmandu', 'pokhara', 'biratnagar', 'butwal', 'dharan'])
bipin1=bipin.astype('int32')
print(bipin1.dtype)
print(bipin.dtype)

x=np.array([1, 2, 3, 4, 5], dtype='U')
print(x.dtype)