import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# Start
import numpy 

arr = numpy.array(['a','b','c','d','e'])
print(arr)
print('\n')

import numpy as np

arr = np.array([1,2,3])
print(arr)
print(type(arr))

print(np.__version__)
print('\n')
#creation

arr1 = np.array((4,5,6))
print(arr1)

# 0D array
arr = np.array(42)
print(arr)

# 1D array
arr = np.array([12,13,14,15,16])
print(arr)

# 2d

arr = np.array(((1,2,3),(4,5,6)))
print(arr)

# 3d
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)

#howw many D
a = np.array(42)
b = np.array([12,13,14,15,16])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print('\n')

#indexing
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[2] + arr[4])


import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2nd element on the first row : ",arr[0,1])
print("5nd element on the first row : ",arr[1,4])

print(arr[1,-1])


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0,1,2])



