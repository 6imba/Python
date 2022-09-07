# # 1
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page)


# # 2
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.text)  # print the all text_characters of given url


# # 3
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.text[:100]) # print the first 100 characters


# # 4
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(type(page))


# # 5
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.url) # print the url that was fetched


# # 6
# import requests
# import json
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.json())# turn page.text into a python object


# # 7
# import requests
# import json
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# x = page.json() # turn page.text into a python object
# print(type(x))


# # 8
# import requests
# import json
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# x = page.json() # turn page.text into a python object
# print(x)


# # 9
# import requests
# import json
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# x = page.json() # turn page.text into a python object
# print(x[0:1])
# print(x[:1])
# print(x[:5])


# # 10
# import requests
# import json

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.text[:5])  # print the first 5 characters
# print(type(page.text[:5]))
# print(page.json()[:5]) # turn page.text into a python object  # print the first 5 list
# print(type(page.json()[:5]))


# # 11
# import requests
# import json
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# x = page.json() # turn page.text into a python object
# print(x[:1])
# print(json.dumps(x[:1], indent=3)) # pretty print the results


# # 12
# import requests
# import json

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page)
# print(type(page))
# y= page
# print(y)
# print(type(y))
# print(page.text[:150]) # print the first 150 characters
# print(page.url) # print the url that was fetched
# print("------")
# x = page.json() # turn page.text into a python object  
# print(type(x))
# print("---first item in the list---")
# print(x[0])
# print("---the whole list, pretty printed---")
# print(json.dumps(x, indent=2)) # pretty print the results


# # 13
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page.text[:150]) # print the first 150 characters
# print(page.url) # print the url that was fetched


# # 14
# import requests
# kval_pairs = {'rel_rhy': 'funny'}
# page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
# print(page.text[:150]) # print the first 150 characters
# print(page.url) # print the url that was fetched

