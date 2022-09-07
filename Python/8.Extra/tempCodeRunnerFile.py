# sort list3 according to index[2] of list item
def clause_func (a_list):
    return a_list[2]

list3 = [[4,2,8],[11,6,3],[1,5,44],[20,1,13]]
list3.sort(key = clause_func)
print(list3)
