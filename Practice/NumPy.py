#CODE PRACTICE FOLLOWING: "Numpy.org Numpy Quickstart Guide"

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
import numpy as np
a = np.array([1,2,3,4])
print(a)
print(type(a))
print(a.dtype)#each array entry is a 64 bit integer
b = np.array([1.2,3.3])
print(type(b))
print(b.dtype)#each array entry is a 64-bit float
#64-bit elements can only represent integers up to 2^64
#signed: up to 2^63 - 1, because 2^63 has 63 digits after the first
#2^n bits requires n+1 bits to represent

#np.array takes one sequence as an argument

#array turns sequence of sequence into 2D array
c = np.array([(1,2),(1.1,2.2)])
print(c)
#turned each entry into a float
#commas between sequences because I used print()
d= np.array([1,2], dtype=np.complex128)
print(d)
#dtype = type of output and how many bits
#default dtype = float64

zero = np.zeros((3,4))
ones = np.ones ((3,4))
empty = np.empty((3,4))
#takes in type argument with dimensions (# sequences, sequence length)

#arrange function like range in Python
#[initial, final, increment] where final is exclusive
arange = np.arange(10, 30, 5)
print(arange)
#range doesn't have an output, arange output is an array

#using arange with floats: can't predict \
#number of elements (floating point precision is finite)
#to arange floats: linspace argument; choose number of elements
from numpy import pi
float_arange = np.linspace(0,2,10)
print(float_arange)
print(float_arange.dtype)
#dtype is an atribute of the numpy array object/instance in class numpy.ndarray

print(type(float_arange))
#DOT NOTATION for OBJECT-ORIENTED PROGRAMMING:
# object.attribute (data on an instance of a class)
# object.method() (function on an instance)
# module.something (accessing something in a module)
#     ex. numpy.ndarray = module.class
# class.something (accessing something defined on a class)
#     for attributes/methods belonging to a class and not a specific instance

#python uses OOP because everything in python is an object
#since objects are defined as an instance of a class, everything in python is an instance of a class
    #function 'type()' tells you the class something is an instance of
    #classes: int/float/str/list/builtin fn or method/module
    #'instance' = 'object'

#linspace to evaluate function at point:
x = np.linspace(0,2*pi, 100)#100 values within a range
f = np.sin(x) #sin() is a function of the np module
#print(f)
print(type(x),type(f))
#sin is a function of the np module, it performs sin on each element of an array
#sin(array)
#example of VECTORIZATION: np.sin() takes in an array and applies the funtion element-wise
    #means you avoid iteration yourself

# %%
#PRINTING ARRAYS
#similar to nested lists but there are differences
#all axes printed top to bottom, last axis printed left to right

#1d, 2d, and 3d arrays:

