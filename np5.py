#"""5)a = np.array([1,2,3,4,5]) b = np.array([5,6,7,8,9]) Remove all values from b if present in a"""

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(b, a))
