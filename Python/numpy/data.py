import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1,2,3,4] , dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4] , dtype='i4')
print(arr)
print(arr.dtype)
print('\n')

#change type
arr = np.array([1,2,3,4,5])
newarr = arr.astype('f')
print(newarr)
print(newarr.dtype)


arr = np.array([1.1,1.2,2.2,3.3,4.4])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#copy and view
arr = np.array([5,6,7,8,9])

x = arr.copy()
y = arr.view()
arr[0] = 1

print(arr)
print(x)
print(y)

import numpy as np
arr = np.array([[1,2,3,4],[3,4,5,6]])
print(arr.shape)

import numpy as np
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print("shape :",arr.shape)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)

newarr = arr.reshape(6,2)
print(newarr)
print(newarr.ndim)
print('\n')

newarr = arr.reshape(2,3,2)
print(newarr)
print('\n')

#iteration
import numpy as np

arr = np.array([1,2,3,4])

for x in arr:
    print(x)
print('\n')

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

for x in arr:
    print(x)
    

arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    for y in x:
        print(y)
        

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print('x represents the 2d array')
    print(x)
    
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
print('\n')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):
    print(x)
print('\n')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx,x in np.ndenumerate(arr):
    print(idx,x)
    
