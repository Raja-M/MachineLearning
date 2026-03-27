import numpy as np

print ("Hello Numpy")

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr=np.array([1,2,3],ndmin=5)
print(arr)
print("number of dimensions :",arr.ndim)

print(arr[0])
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print("=======")
original_arr=np.array([1,2,3,4])
x=original_arr.copy()
y=original_arr.view()
original_arr[0]=3
y[1]=3
print(original_arr)
print(x)
print(y)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)#convert array to 1D
print(newarr)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):#iterations 
  print(x)
#join
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2), axis=1)
arr = np.stack((arr1, arr2), axis=1)
arr = np.hstack((arr1, arr2))#to stack along rows.
arr = np.vstack((arr1, arr2)) #to stack along columns.
arr = np.dstack((arr1, arr2))#to stack along height, which is the same as depth.
#split
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.hsplit(arr, 3)
print(newarr)
x = np.where(arr%2 == 0)#array elements satisfy this condition return indexes
print(x)
#search
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
#sort
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
#filter
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

  # arr0204 = np.array([
#     [1, 2, 3, 4], 
#     [5, 6, 7, 8], 
#     [9, 10, 11, 12]])
# print(arr0204)
# print(arr0204[1,3])

# print( arr0204.shape)

# print ( np.empty(2))
# print ( np.arange(5))

# print (np.linspace(0, 10, num=5))

# print ( np.sort(np.array([2, 1, 5, 3, 7, 4, 6, 8]))   )

# arrayb = np.arange(12).reshape(3, 4)

# print (arrayb)

# print( arrayb.sum(axis=0))
# print( arrayb.sum(axis=1))

# a = np.array([1, 2, 3, 4, 5, 6] )

# print(a)

# a2 = a[np.newaxis, :]

# print(a2.shape)   

# arrayr = np.arange(25).reshape(5, 5)

# print(arrayr)

# print(arrayr[1:4, 3:5])


# arrayexp = np.arange(12)**2 

# print(arrayexp)

# palette = np.array([[0, 0, 0],         # black
#                     [255, 0, 0],       # red
#                     [0, 255, 0],       # green
#                     [0, 0, 255],       # blue
#                     [255, 255, 255]]) 

# image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
#                   [0, 3, 4, 0]])


# print( palette[image] ) 


# a = np.arange(12).reshape(3, 4)

# i = np.array([[0, 1],  # indices for the first dim of `a`
#               [1, 2]])

# j = np.array([[2, 1],  # indices for the second dim
#               [3, 3]])

# print(a) 

# print (a[i, j])



# a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 5]])

# print(a_2d)
# unique_values = np.unique(a_2d)

# print(unique_values)

# unique_rows = np.unique(a_2d, axis=0)

# print(unique_rows)

# unique_rows, indices, occurrence_count = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
# print(unique_rows)
# print(indices)
# print(occurrence_count)


# unique_rows, indices, occurrence_count = np.unique(a_2d, axis=1, return_counts=True, return_index=True)
# print(unique_rows)
# print(indices)
# print(occurrence_count)

# np.unique(a_2d, axis=0, return_counts=True, return_index=True)

a = np.arange(15).reshape(3, 5)
print(a)
print( a.transpose())

 