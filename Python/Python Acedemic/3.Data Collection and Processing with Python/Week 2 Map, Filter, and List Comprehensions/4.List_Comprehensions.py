# 1
# Hi everyone. I have to apologize because the previous lesson forced you to learn some pretty conceptually challenging
# stuff, passing a transformer function to the map function, and passing a filtration function to the filter function. 
# It turns out that you wont actually use them. Python Programmers rarely do. 
# It was just a pedagogical tool to give you a way to really think through the map and filter programming patterns. 
# In Python, there's actually a simpler syntax for doing the map and filter patterns and even for combining them. 
# It's called list comprehensions. Now that you understand what they're for, I think you're going to love them. 
# The syntax can be a little confusing because it reuses elements of the for loop syntax. 
# But with an understanding of what list comprehensions do based on the map and filter lesson, I think you'll find that it's pretty intuitive. 
# List comprehensions are how Python programmers typically write code that does transformation and filtration. 
# At the end of this lesson, you should be able to read and write list comprehensions, and you should be able to describe 
# a list comprehension in terms of the transformation and filtration operations that it's performing. 
# So, let's go see how they work. See you at the end.


# # 2
# # List_comperhension_Map
# # [<transformer-expression> for <variable_name> in <sequense>]
# numbs_list = [1,2,3,4,5,6,7]
# double_list_compre = [numb*2 for numb in numbs_list] # List_comperhension
# print(double_list_compre)

# # [numbs*2 for numbs in numbs_list]
# # [<transformer-expression> for <variable_name> in <sequense>]


# # 2
# # List_comperhension & Map
# numbs_list = [1,2,3,4,5,6,7]
# double_list_compre = [numbs*2 for numbs in numbs_list] # List_comperhension  for mapping
# double_list_map = map(lambda numbs : numbs*2 , numbs_list) # Map             
# print(double_list_compre)
# print(double_list_map)
# print(list(double_list_map))


# 3
# # List_comperhension_Filter
# numbs_list = [1,2,3,4,5,6,7]
# even_list_compre = [numbs%2==0 for numbs in numbs_list] # List_comperhension  for filtering
# print(even_list_compre)
# # This [numbs%2==0 filteration_expression gives output that  returns true or false


# # 4
# # Proper List_comperhension_Filter
# numbs_list = [1,2,3,4,5,6,7]
# even_list_compre = [numbs for numbs in numbs_list if numbs%2==0] # List_comperhension  for filtering
# print(even_list_compre)
# # This variable [numbs gives output as value of variable if this [numbs%2==0 filteration_expression is true for that numb

# # [numbs for numbs in numbs_list if numbs%2==0]
# # [<transformer-variable> for <iteration_variable> in <sequence> if <filteration_expression>]


# # 5
# # List_comperhension & Filter
# numbs_list = [1,2,3,4,5,6,7]
# even_list_compre = [numbs for numbs in numbs_list if numbs%2==0] # List_comperhension  for filtering
# even_list_filter = filter(lambda numbs:numbs%2==0 , numbs_list) # Filter

# print(even_list_compre)
# print(even_list_filter)
# print(list(even_list_filter))


# 6
# alist = [4,2,8,6,5]
# blist = [num*2 for num in alist if num%2==1]
# print(blist)



# # The transformer expression is value * 2. The item variable is value and the sequence is things. This is an alternative way to perform a mapping operation. As with map, each item in the sequence is transformed into an item in the new list. Instead of the iteration happening automatically, however, we have adopted the syntax of the for loop which may make it easier to understand.

# # Just as in a regular for loop, the part of the statement for value in things says to execute some code once for each item in things. Each time that code is executed, value is bound to one item from things. The code that is executed each time is the transformer expression, value * 2, rather than a block of code indented underneath the for statement. The other difference from a regular for loop is that each time the expression is evaluated, the resulting value is appended to a list. That happens automatically, without the programmer explicitly initializing an empty list or appending each item.

# # The if clause of a list comprehension can be used to do a filter operation. To perform a pure filter operation, the expression can be simply the variable that is bound to each item. For example, the following list comprehension will keep only the even numbers from the original list.

