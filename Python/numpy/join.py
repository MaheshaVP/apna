import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9])
arr3 = np.concatenate((arr1 , arr2))
print(arr3)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1,arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1,arr2))
print(arr)

arr = np.vstack((arr1,arr2))
print(arr)
print('\n')

#split
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr,3)
print(newarr)

# search 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 1)
print(x)

# sort
import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([5,2,3,8,10])
print(np.sort(arr))

#filtering
import numpy as np
arr = np.array([1,2,3,4])
x = [True,False,True,False]
newarr = arr[x]
print(newarr)


arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
    
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []

for elem in arr:
    if elem % 2 == 0:
        filter_arr.append(True)
        
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

filter_arr = arr % 2 == 0
print(filter_arr)