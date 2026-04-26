#NumPy Splitting Array || np.array_split ||
#it is reverse to joining


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6]) 

newarr = np.array_split(arr, 3)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])





#searching array  

a=np.array([1,2,5,6,8,9,6,7,5])
b=np.where(a==6)
print(b)


# find even indexes
bipin=np.array([1,2,3,4,5,6,7,8,9,12,14])
c=np.where(bipin%2==0)
print("this is even indexes:", c)


tiwari=np.array([1,2,16,4,5,6,7,8,9,12,14])
d=np.where(tiwari%2==1)
print("this is odd indexes:", d)




#SEARCHSORTED ARRAY
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)


#NOW we search from the right side
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)


#how to search for more than one value in an array
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, [2, 4, 6, 8])
print(x)