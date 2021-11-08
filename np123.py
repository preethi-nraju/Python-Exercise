#"""1)Create a numpy array 4x4 with all True"""

import numpy as np

fourdarray = np.ones((4,4),dtype=bool)
print(fourdarray)

#"""2)Replace all odd numbers from the array with -1"""

b = np.arange(15)
b[b%2!=0] = -1
print(b)

#"""3) Find max and min from a matrix"""

mat = np.matrix('1,2,23;5,8,89;12,5,9')
print("max element is "+str(np.max(mat))+"\nmin element is "+str(np.min(mat)))