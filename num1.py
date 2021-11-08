import time
import sys

import numpy as np

a = np.array([1,2,3])
print(a)
print(a[0])
print(a[1])

b = range(1000)
print(sys.getsizeof(5)*len(b))

c = np.arange(1000)
print(c.size*c.itemsize)

size = 100000
L1 = range(size)
L2 = range(size)
A1 = np.array(size)
A2 = np.array(size)
start = time.time()
result = [(x+y) for x,y in zip(L1, L2)]
print(result)
print("python list took:", (time.time()-start)*1000)

size = 100000
L1 = range(size)
L2 = range(size)
B1 = np.array(size)
B2 = np.array(size)
start = time.time()
result = B1 + B2
print("numpy array took:", (time.time()-start)*1000)