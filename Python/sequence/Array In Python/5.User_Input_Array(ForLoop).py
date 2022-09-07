# # Insert array element inputed by users using for loop:

from array import array
arr1 = array('i', []) #empty array
arr1_len = int(input('Enter the size that you want an array to be : ')) # size of array
for n in range(arr1_len):
    element = int(input('Input an element into array : '))
    arr1.append(element)


print('....................................................................................................................')


#print created array :
print('Finally arr1 holds : ',arr1)

print('....................................................................................................................')


for element in arr1:
    print(element)

print('....................................................................................................................')

for index in range(len(arr1)):
    print(arr1[index])


