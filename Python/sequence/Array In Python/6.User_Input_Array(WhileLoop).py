# # Insert array element inputed by users using while loop:

from array import array
arr2 = array('i',[])

arr2_len = int(input('Enter the size that you want array to be : '))

accum = 0
while accum < arr2_len:
    element = int(input('Enter element of array : '))
    arr2.append(element)
    accum += 1


print('....................................................................................................................')

print(arr2)

print('....................................................................................................................')

index_accum = 0
while index_accum < len(arr2):
    print(arr2[index_accum])
    index_accum += 1
