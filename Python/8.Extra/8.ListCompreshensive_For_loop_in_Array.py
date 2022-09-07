# # 1
# # List_comperhension_Map
# # [<transformer-expression> for <variable_name> in <sequense>]
# numbs_list = [1,2,3,4,5,6,7]
# double_list_compre = [numb*2 for numb in numbs_list] # List_comperhension
# print(double_list_compre)

# # [numbs*2 for numbs in numbs_list]
# # [<transformer-expression> for <variable_name> in <sequense>]

# numbs_list = [1,2,3,4,5,6,7]
# double_list_compre = [numbs*2 for numbs in numbs_list] # List_comperhension
# double_list_map = map(lambda numbs : numbs*2 , numbs_list) # Map



# # 2
# # Proper List_comperhension_Filter
# numbs_list = [1,2,3,4,5,6,7]
# even_list_compre = [numbs for numbs in numbs_list if numbs%2==0] # List_comperhension  for filtering
# print(even_list_compre)
# # This variable [numbs gives output as value of variable if this [numbs%2==0 filteration_expression is true for that numb

# # # List_comperhension & Filter
# numbs_list = [1,2,3,4,5,6,7]
# even_list_compre = [numbs for numbs in numbs_list if numbs%2==0] # List_comperhension  for filtering
# even_list_filter = filter(lambda numbs:numbs%2==0 , numbs_list) # Filter

# print(even_list_compre)
# print(even_list_filter)
# print(list(even_list_filter))
