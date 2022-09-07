# # 1
# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_version = original[:]
# print(copied_version)
# print(copied_version is original) # we checked is copied_version the same object as original. And the answer to that is false. Copied_version is pointing to one object and Original is pointing to a different object.
# print(copied_version == original) # we check whether they have the same contents. The answer to that true. So original and copied are not the same object, they're different objects, but they're both list. They both have two elements, and those elements are these inner list,and those elements are these inner list, dog, puppies, and cats, kittens. It's true that they are equal, equal. It's not true that they are is each other. So copied_version is not original but it is equal to the original, it has the same contents.
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_version)


# # 2 
# # # Deep and Shallow Copies
# # # Earlier when we discussed cloning and aliasing lists we had mentioned that simply cloning a list using [:] would take care of any issues with having two lists unintentionally connected to each other. That was definitely true for making shallow copies (copying a list at the highest level), but as we get into nested data, and nested lists in particular, the rules become a bit more complicated. We can have second-level aliasing in these cases, which means we need to make deep copies.
# # # When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change. We can see this happen in the following nested list, which only has two levels.

# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_version = original[:]  # ==> original and copied_version are both different list_object at different address with same element
# print(copied_version) 
# print(copied_version is original) # ==> both different list_object at different address
# print(copied_version == original) # ==> with same element
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_version)



# # Welcome back. Earlier in this specialization, we took dive into aliasing, and the confusions that can occur when you mutate a list or a dictionary that has many aliases. Many different variable names pointing to the same list or dictionary.
# # Play video starting at 24 seconds and follow transcript0:24
# # The same thing is true if you have instead of variable names pointing to a single list, if you have a single list that is included as an element in multiple other lists.
# # Play video starting at 36 seconds and follow transcript0:36
# # If you mutate the inner list that is part of several outer lists, all those outer lists will look like the contents have changed.
# # Play video starting at 44 seconds and follow transcript0:44
# # The best to keep track of these confusing situations will be with the reference diagram, of course.
# # Play video starting at 52 seconds and follow transcript0:52
# # So let's took at example one way that you get a list included in multiple list by accident, and let's get this confusing situation is when you copy a list. As in this codes slip it, let's start by just running it.
# # Play video starting at 1 minute 9 seconds and follow transcript1:09
# # So you can see that on line1, we create a list called original, it's value is a nested list. The outer list has two inner lists as it's elements. Let's set ourselves up with a reference diagram. We're going to say that, Original,
# # Play video starting at 1 minute 34 seconds and follow transcript1:34
# # Is the variable name, and it's value is a list.
# # Play video starting at 1 minute 39 seconds and follow transcript1:39
# # That list has two items.
# # Play video starting at 1 minute 44 seconds and follow transcript1:44
# # The first item is itself a list, and that list has dogs,
# # Play video starting at 1 minute 54 seconds and follow transcript1:54
# # As an element, and it has puppies as an element.
# # Play video starting at 2 minutes 7 seconds and follow transcript2:07
# # The second element of original is another list,
# # Play video starting at 2 minutes 14 seconds and follow transcript2:14
# # Which is as it values cats and kittens.
# # Play video starting at 2 minutes 29 seconds and follow transcript2:29
# # So that's how it happens on line 1. On line 2, we make a copy of original. We use the slice operator, colon inside of square brackets. You may recall that always creates a slice. If I said, original[1:4], that would Make a slice beginning with the item at index one and going up to but not including position four. Of course, I can't do that for this list because it only has two items.
# # Play video starting at 3 minutes 8 seconds and follow transcript3:08
# # But if we leave off the value before the colon, we start at the beginning of the list. If we leave off the value after the colon we go all the way to the end of the list. So this says take a slice beginning at the beginning of original, and going to end of original.
# # Play video starting at 3 minutes 26 seconds and follow transcript3:26
# # So that makes a new list, and that new list has has its elements, the same elements that original had.
# # Play video starting at 3 minutes 38 seconds and follow transcript3:38
# # The first element is dogs and puppies, the second element is cats and kittens. And we assign that to a variable called copied_version.
# # Play video starting at 3 minutes 54 seconds and follow transcript3:54
# # That's what happens on line 2.
# # Play video starting at 3 minutes 58 seconds and follow transcript3:58
# # And just to show you what the output looks like.
# # Play video starting at 4 minutes 2 seconds and follow transcript4:02
# # On line 3, we print out copied _version and sure enough, it looks like it has exactly the same stuff that original has in it.
# # Play video starting at 4 minutes 12 seconds and follow transcript4:12
# # On line 4, we checked is copied_version the same object as original. And the answer to that is false. Copied_version is pointing to one object.
# # Play video starting at 4 minutes 24 seconds and follow transcript4:24
# # Original is pointing to a different object.
# # Play video starting at 4 minutes 28 seconds and follow transcript4:28
# # One line 5, we check whether they have the same contents. The answer to that true. So original and copied are not the same object, they're different objects, but they're both list. They both have two elements, and those elements are these inner list, dog, puppies, and cats, kittens. It's true that they are equal, equal. It's not true that they are is each other. So copied_version is not original but it is equal to the original, it has the same contents.
# # Play video starting at 5 minutes 4 seconds and follow transcript5:04
# # On line 6, we see where our confusions are going to happen when we have multiple outer list that point to the same inner list.
# # Play video starting at 5 minutes 13 seconds and follow transcript5:13
# # So original square bracket 0 is the first inner list, that's dog's puppies. And on line 6, we say, .append of canines. So that is going to append to the end of this list, another item. But notice that this item is canines in square brackets. So this item is actually another list.
# # Play video starting at 5 minutes 43 seconds and follow transcript5:43
# # That list has only one item, canines.
# # Play video starting at 5 minutes 53 seconds and follow transcript5:53
# # But it is a list, it's not just this string canines. So now on line 7, if we print original, We get this list here. Where the first element is dogs, puppies like before, but we've appended to the end of that list, the list canines.
# # Play video starting at 6 minutes 16 seconds and follow transcript6:16
# # And then the second element is still cats and kittens.
# # Play video starting at 6 minutes 25 seconds and follow transcript6:25
# # On line 9, we print the copied version.
# # Play video starting at 6 minutes 29 seconds and follow transcript6:29
# # Now on line 6, we just said to change original, we didn't say anything about changing copied_version. But on line 9, you can see
# # Play video starting at 6 minutes 39 seconds and follow transcript6:39
# # that this square bracket canines has magically appeared after dogs and puppies. And that's because copied_version, even though we didn't say to change it, copied_version has as its first element this list, and we mutated that list.
# # Play video starting at 6 minutes 59 seconds and follow transcript6:59
# # That's shallow copies for you. See you next time.

