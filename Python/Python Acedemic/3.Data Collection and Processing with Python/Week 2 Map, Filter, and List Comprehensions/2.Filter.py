# # 1
# def keep_evens(nums):
#     new_list = []
#     for num in nums: # manual_accumulation
#         if num % 2 == 0:
#             new_list.append(num)
#     return new_list
# print(keep_evens([3, 4, 6, 7, 0, 1]))


# # Again, this pattern of computation is so common that Python offers a more compact and general way to do it,
# # the filter function. filter takes two arguments, a function and a sequence. 
# # The function takes one item and return True if the item should. 
# # It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.


# # Now consider another common pattern: going through a list and keeping only those items that meet certain criteria. This is called a filter.

# def even_filter(numbs1):
#     even_list1 = filter(lambda numb:numb%2 == 0 , numbs1)
#     print(even_list1)
#     print(type(even_list1))
#     return even_list1

# numbs = [3, 4, 6, 7, 0, 1]
# even_list = even_filter(numbs)
# print(list(even_list))

# def even_filter(numbs1):
#     even_list1 = map(lambda numb:numb%2 == 0 , numbs1)
#     print(even_list1)
#     print(type(even_list1))
#     return even_list1


# def keep_evens(nums):
#     new_list = []
#     for num in nums: # manual_accumulation
#         if num % 2 == 0:
#             new_list.append(num)
#     return new_list
# print(keep_evens([3, 4, 6, 7, 0, 1]))


# # So, unlike with map where the function was a transformer that was taking the input and transforming it into something else, 
# # here we're not transforming the input. We're just making a binary decision about it. 
# # Is it true? Meaning keep it in, or is it false? Meaning filter it out. 
# # So, the next thing to notice is what's actually in this Lambda expression. 
# # We're saying Lambda num: num percent two equals zero. This num percent two equal equals zero, 
# # that's our same filtration expression that we saw before when we were doing the manual accumulation.



# def keep_evens(nums):
#     new_seq = filter(lambda num: num % 2 == 0, nums)
#     return list(new_seq)

# print(keep_evens([3, 4, 6, 7, 0, 1]))



# numb_list = [3, 4, 6, 7, 0, 1]
# even_seqs = filter(lambda numb : numb%2 ==0 , numb_list)
# print(list(even_seqs))


# 1. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.

# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

# def w_check_filter(lst_check1):
#     w_list = filter(lambda word : 'w' in word , lst_check1)
#     return list(w_list)

# filter_testing = w_check_filter(lst_check)
# print(filter_testing)
#  passing list to the filter_function inside w_check_filter function

# #oneline_code
#  lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
#  filter_testing = list(filter(lambda item:if 'w' in item,lst_check))
#  print(filter_testing)


# # simply
# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# filter_testing = filter(lambda word : 'w' in word , lst_check)
# print(list(filter_testing))
# #  passing list directly to the filter_function


# # In[9]:


# # 2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.

# lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

# def o_filter(lst1):
#     o_list = filter(lambda word : 'o' in word , lst1)
#     return o_list
    
# lst2 = list(o_filter(lst))
# print(lst2)

