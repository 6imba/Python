# 1

# You've now learned about the map and filter functions which perform particularly common accumulation patterns. 
# With map, you pass in a transformer function which takes one item and transforms it into its new value. 
# With filter, you pass in a filtration function which takes an item and returns a boolean. 
# True if the item should be included, false if the item should be filtered out. 
# Here's an apocryphal story about a filter that Socrates applied to gossip. 
# In ancient Greece as you may know, Socrates was widely lauded for his wisdom. 
# One day, the great philosopher came upon an acquaintance who ran up to him excitedly and said, 
# "Socrates, do you know what I just heard about one of your students Plato?" "Wait a moment," 
# Socrates replied." "Before you tell, me I'd like you to pass a little test. I call it the triple filter test" "What? Triple filter?" "That's right" Socrates continued. 
# "Before you talk to me about what Plato did, let's take a moment to filter what you're going to say. The first filter is truth. Have you made absolutely sure that what you're about to tell me as true?" 
# Named X, X is true." "No." The man said, "Actually, I just heard about it and," "All right," said Socrates. "So, you don't really know whether it's true or not"."
# Let's try the second filter. The filter of goodness. Is what you're about to tell me about Plato, is that something good, named X, X is good" " No, on the contrary.
# " So, Socrates continued. "You want to tell me something bad about Plato even though you're not certain it's true?
# " The man shrugged a little embarrassed. Socrates continued. "Well, let's try the third filter, the filter of usefulness. 
# Is what you want to tell me about Plato going to be useful to me?" Named X, X is useful." "No, not really." "Well, " 
# concluded Socrates. "If what you want to tell me is neither true, nor good, nor even useful, why tell it to me at all?" 
# The man was defeated and ashamed. This is the reason why Socrates was a great philosopher and held in such high esteem. 
# It also explains why Socrates never found out that Plato is sleeping with his wife. I'll see you next time.


# # 2
# # Manual_Accumulation
# def quard(numb_list1):
#     numb_list2 = []
#     for numb in numb_list1:
#         numb_list2.append(numb*4)
#     return numb_list2

# numb_list = [3, 4, 6, 7, 0, 1]
# print(list(quard(numb_list)))


# #2
# # Manual_Accumulation
# def quard(numbs):
#     numb_list2 = []
#     for numb in numbs:
#         numb_list2.append(numb*4)
#     return numb_list2

# numb_list = [3, 4, 6, 7, 0, 1]
# print(list(quard(numb_list)))


# # 2
# # Mapping
# numb_list = [3, 4, 6, 7, 0, 1]
# quard = map((lambda numb: 4*numb), numb_list)
# print(list(quard))


# # 3
# # Filter
# numb_list = [3, 4, 6, 7, 0, 1]
# even_seqs = filter(lambda numb : numb%2 ==0 , numb_list)
# print(list(even_seqs))


# # 4
# # Manual_Accumulation
# # Let’s revisit the accumulator pattern. 
# # We have frequently taken a list and produced another list from it that contains either a subset of the items or a transformed version of each item. 
# # When each item is transformed we say that the operation is a mapping, or just a map of the original list.
# # When some items are omitted, we call it a filter.


# 5
# # Map_Function
# # the map function, that makes it more clear what the overall structure of the computation is.
# # map takes two arguments, a function and a sequence. The function is the mapper that transforms items. 
# # It is automatically applied to each item in the sequence. 
# # You don’t have to initialize an accumulator or iterate with a for loop at all.


# # 6
# # Filter_Function
# # So, unlike with map where the function was a transformer that was taking the input and transforming it into something else, 
# # here we're not transforming the input. We're just making a binary decision about it. (1 or 0) , (True or False) , (Yes or No)
# # Is it true? Meaning keep it in, or is it false? Meaning filter it out. 
# # So, the next thing to notice is what's actually in this Lambda expression. 
# # We're saying Lambda num: num percent two equals zero. This num percent two equal equals zero, 
# # that's our same filtration expression that we saw before when we were doing the manual accumulation.

