# # 1
# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_outer_list = []
# for inner_list in original:
#     copied_inner_list = []
#     for item in inner_list: #manual acumulation
#         copied_inner_list.append(item)
#     copied_outer_list.append(copied_inner_list)
# print(copied_outer_list)
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_outer_list)


# # 2
# # Assuming that you don’t want to have aliased lists inside of your nested list, then you’ll need to perform nested iteration.
# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_outer_list = []
# for inner_list in original:
#     copied_inner_list = []
#     for item in inner_list:
#         copied_inner_list.append(item)
#     copied_outer_list.append(copied_inner_list)
# print(copied_outer_list)
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_outer_list)

# # Previously I should you that a shallow copy it can lead to some confusions because the same inner lists is included in multiple outer lists. What would we do if we wanted to make a copy that it was completely independent of the original list? So that no change anywhere, even to a inner list to which change the copied version. That's what's called a deep copy. We can do it with nested iteration, accumulating a copy of each inner list.
# # Play video starting at 31 seconds and follow transcript0:31
# # So let's take a look at this code.
# # Play video starting at 34 seconds and follow transcript0:34
# # I have the same original list from before, it has two inner lists. The first one, dogs and puppies, the second one, cats and kittens.
# # Play video starting at 45 seconds and follow transcript0:45
# # I'm going to use our old friend, the accumulation pattern. I start by making copied_outer_list be an empty list, so this is our accumulator variable. I iterate through the sequence original by loop variable or iterator variable I'm calling, inner list. And then I'm doing this nested iteration. And I'm doing a nested accumulation here. So I make another accumulated variable, copied_inner_list, and it's set to be empty. I iterate through the items in inner list. Here my second iterator variable is called item. And I append it, I append item, to the copied_inne_list. So copied_inner_list starts as an empty list, and we keep adding additional items to it. When we're done with the inner list, copied_inner_list has all of the same elements that it had. And so we then take copied_inner_ list, and we append it to the outer list.
# # Play video starting at 1 minute 51 seconds and follow transcript1:51
# # Let's run that and see what happens.
# # Play video starting at 1 minute 59 seconds and follow transcript1:59
# # At the end of lines 337, we have copied_outer_ list as this deep copy. If we print it, it looks like it has the same contents as original. Because this is a deep copy, even if I append canines to the end of the first inner list in the original list, as I'm doing on line 9, it's not going to have any impact on the deep copy of the copied outer list. So, we print original, and it does the same thing that happened in our previous example. But when I print the copied outer list, there's no canines here
# # Play video starting at 2 minutes 44 seconds and follow transcript2:44
# # The reason is that I have made a deep copy. So let's just make the reference diagram that'll go with this. We have original,
# # Play video starting at 2 minutes 57 seconds and follow transcript2:57
# # It's a list of two things.
# # Play video starting at 3 minutes 2 seconds and follow transcript3:02
# # And one is the Dogs and puppies.
# # Play video starting at 3 minutes 15 seconds and follow transcript3:15
# # The other is the cats and kittens.
# # Play video starting at 3 minutes 27 seconds and follow transcript3:27
# # When we make a copied_outer_list,
# # Play video starting at 3 minutes 36 seconds and follow transcript3:36
# # We end up again with a list of two items. But the first item is now not pointing to dogs and puppies, it's pointing to a copy of it.
# # Play video starting at 3 minutes 54 seconds and follow transcript3:54
# # With the same contents, And it's a different list. So then on line 9, when I append something here, there's an extra item with the canines in it.
# # Play video starting at 4 minutes 16 seconds and follow transcript4:16
# # It does not have any effect on the inner list from copied outer list. Doesn't change anything in the deep copies. So we have successfully managed to make copiedouter list be a deep copy that is completely independent from the original list. Even if I change something deep inside the original list, it has no impact on the copied outer list.


# # 3
# # Or, equivalently, you could take advantage of the slice operator to do the copying of the inner list.
# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_outer_list = []
# for inner_list in original:
#     copied_inner_list = inner_list[:]
#     copied_outer_list.append(copied_inner_list)
# print(copied_outer_list)
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_outer_list)


# # 4
# import copy
# original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

# shallow_copy_version = original[:] 
# # the original and the shallow copy diverge, because the original gets Hi there at the end. So we appended to the top level list, and there 
# # the original is different than the shallow copy. So Hi there got appended to original, did not get appended to shallow copy.

# deeply_copied_version = copy.deepcopy(original)

# original.append("Hi there")
# original[0].append(["marsupials"])
# print("-------- Original -----------")
# print(original)
# print("-------- deep copy -----------")
# print(deeply_copied_version)
# print("-------- shallow copy -----------")
# print(shallow_copy_version)
# # the original and the shallow copy diverge, because the original gets Hi there at the end. So we appended to the top level list, and there the original is different than the shallow copy. So Hi there got appended to original, did not get appended to shallow copy.


# # 5
# import copy
# original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
# shallow_copy_version = original[:]
# deeply_copied_version = copy.deepcopy(original)
# original.append("Hi there")
# original[0].append(["marsupials"])
# print("-------- Original -----------")
# print(original)
# print("-------- deep copy -----------")
# print(deeply_copied_version)
# print("-------- shallow copy -----------")
# print(shallow_copy_version)


# # Nested iteration is where we copy each of the inner list, works fine for making deep copies, if we know how many levels of nesting we have. And we have a parallel structure everywhere with the same levels of nesting.
# # Play video starting at 5 minutes 43 seconds and follow transcript5:43
# # But what about this one? There are three levels in some places but not everywhere.
# # Play video starting at 5 minutes 50 seconds and follow transcript5:50
# # We've got an outer list which has as its first element this inner list. But this inner list has a string canines as its first element, but a third level of a list as its second element. So how would you make a deep copy of this one? This is a case where a technique called recursion will allow us to write fairly elegant code, but we are not going to teach recursion in this. It turns out you can get pretty far in writing the applications and data analysis programs without learning recursion, because in the most common cases where it's useful, there is built in function available to use that will do the recursion behind the scenes. This is one of those cases, there's a built in function called deep copy, and a module called copy. So I've imported the module called copy, and inside the copy module there is a deep copy function, and it just takes the sequence as its value. And it produces a deep copy where as many levels of nesting as there are, it goes in and always copies things, it never shares an inner list between the original and the deep copy. So I have my original version.
# # Play video starting at 7 minutes 13 seconds and follow transcript7:13
# # I have a shallow copied version,
# # Play video starting at 7 minutes 21 seconds and follow transcript7:21
# # And I have a deeply copied version.
# # Play video starting at 7 minutes 30 seconds and follow transcript7:30
# # And if I were to print those out, they would all look the same. But now I'm going to append to the original an extra string at the very end, so it's going to have another item at the end. And then I'm also on line 6 going to the first
# # Play video starting at 7 minutes 55 seconds and follow transcript7:55
# # In our list, and I'm appending the list marsupials to it. At this point we're going to have original deep copy and shallow copy all have different values. And let's see what those are.
# # Play video starting at 8 minutes 13 seconds and follow transcript8:13
# # So you can see now that original has canines, dogs, puppies, and an extra element, marsupials. That happened because unlike 6, we appended the list marsupials to the end of its first inner list. The shallow copy because it only did the one level of copying, also was changed, it got marsupials as well. But in the deep copy, no marsupials.
# # Play video starting at 8 minutes 49 seconds and follow transcript8:49
# # The other difference we can see is that the original and the shallow copy diverge, because the original gets Hi there at the end. So we appended to the top level list, and there the original is different than the shallow copy. So Hi there got appended to original, did not get appended to shallow copy.
# # Play video starting at 9 minutes 13 seconds and follow transcript9:13
# # I encourage you to really work through this in detail. Make a reference diagram. Go through it in code lens. Make sure you understand why these things are coming out with three different printouts at the end. If you can follow it, you'll be able to reason your way through lot of things where you get puzzling answers, and you'll be able to debug your code. So to summarize, a deep copy of a list not only makes a copy of the outer list, but also makes copies of all the inner lists. And their inner list all the way down. A deep copy is completely decoupled from the original. You can make a deep copy with your own code if the structure is simple enough, or use the built in deep copy function in the copy module. See you next time.


# 7
#Shallow and deep copy
import copy
list1 = [[2,4],['a','b']]
print(list1)# orginal

list2 = list1 # shallow copy
list3 = list1[:] # deep copy 
list4 = copy.deepcopy(list1)# deep copy  with deepcopy() method of copy module
list1.append(666666)
list1[0].append(6)

print(list1)# orginal
print(list2)# shallow copy
print(list3)# deeper copy
print(list4)# deeper copy

