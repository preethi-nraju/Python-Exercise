import numpy as np

a = np.array([[1,2], [3,4], [5,6]])
print(a.shape)
print(a.itemsize)
print(a)

a = np.array([[7,8], [9,10], [11,12]], dtype=np.float64)
print(a.shape)
print(a.itemsize)
print(a)

a = np.array([[1,2], [3,4], [5,6]], dtype=np.complex)
print(a)