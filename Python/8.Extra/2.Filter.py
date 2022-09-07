#Filter lists according to condition


# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a
# sequence true or not.
# sequence: sequence which needs to be filtered, it can
# be sets, lists, tuples, or containers of any iterators.
# Returns:
# returns an iterator that is already filtered.




# def check_even (numb):
#     return numb%2==0 # return true value only

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(filter(check_even,numbers))#filter() method returns filter_object
# even = list(filter(check_even,numbers)) # casting filter_object into list
# print(even)


# def check_even (numb):
#     if numb%2==0: # return true value only
#         return True
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(filter(check_even,numbers))#filter() method returns filter_object
# even = list(filter(check_even,numbers)) # casting filter_object into list
# print(even)



# #filter with lambda .....................................
# numbers = [1,2,3,4,5,6,7,8,9,10]
# check_even = filter(lambda numb : numb%2==0,numbers)
# print(list(check_even))


# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda numb : numb%2==0,numbers)))



#when ever we want to filter/select item in sequence we use filter()
