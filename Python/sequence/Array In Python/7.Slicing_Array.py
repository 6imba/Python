# #slicing array
# # syntax : new_arr = org_arr[start : stop : stepsize]

from array import array

arr1 = array('i', [2,4,6,8,10,12,14,16,18])

# arr2 = arr1[2:5]
# arr2 = arr1[1:5]
# arr2 = arr1[0:5]
# arr2 = arr1[:5]
# arr2 = arr1[:]
# arr2 = arr1[0:8]
# arr2 = arr1[0:9]
# arr2 = arr1[::2]
# arr2 = arr1[3:7:2]
# arr2 = arr1[3:7:-1] #no element
arr2 = arr1[7:3:-1] #no element
# arr2 = arr1[::-1]

print(arr2)