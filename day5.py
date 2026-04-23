#NumPy Joining Array | Concatenate & Stack 
import numpy as np
a=np.array([1,2,3,4])
b=np.array([6,7,8,9])
c=np.concatenate((a,b))
print(c)


#joining 2D array along with axis axis =1
a=np.array([[1,2],[3,4]])
b=np.array([[6,7],[8,9]])
c=np.concatenate((a,b),axis=1)
print(c)
