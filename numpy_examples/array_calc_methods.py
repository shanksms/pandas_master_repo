import numpy as np
a = np.arange(1, 7).reshape(2, 3)
print(a.ndim)
print(a)

# add all the elements of the array
print(np.sum(a))

# sum along 0 axis
print(np.sum(a, axis=0))
# sum along 1 axis
print(np.sum(a, axis=1))

