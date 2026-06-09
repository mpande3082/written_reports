
# %%
import numpy as np
#ATTRIBUTES OF AN ARRAY
a = np.arange(15).reshape(3,5)
print(a)

b = np.arange(17) #doesn't include the number itself
print(b)

print(a.shape)
print(a.ndim)#how are the axes defined

print(a.dtype.name)#one element = int64
print(a.itemsize)#64 bits per element/8 = 8
print(a.size)# number of elements (shape entries multiplied)

print(type(a)) #in class numpy it's an ndarray
#since ndarray is also a class, is this a class in a class

c = np.array([6,7,8])
print(c)

print(type(c))

#%%
#CREATING ARRAYS



