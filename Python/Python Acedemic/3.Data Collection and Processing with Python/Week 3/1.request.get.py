#generating urls with requests.get
#fetching page using request.get module

# #1
# import requests
# page = requests.get("https://www.datamuse.com/api/")
# print(page)
# print(page.text)


# #2
# import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# print(page)
# print(page.text)

# #3
# import requests
# argument_parameter = {'rel_rhy':'funny'}
# page = requests.get("https://api.datamuse.com/words",argument_parameter)
# print(page)
# print("\n .............................. \n")
# print(page.text)
# print("\n .............................. \n")
# print(page.text[:150])
# print("\n .............................. \n")
# print(page.url)


# #4
# import requests
# argument_parameter = {'q':'violins and guitars','tbm':'isch'}
# page = requests.get("https://google.com/search", argument_parameter)
# print(page)
# print(page.url)
#  # you can use this url https://www.google.com/search?q=violins+and+guitars&tbm=isch in browser


# #5
# import requests
# argument_parameter = {'a':'john cena','tbm':'isch'} #a
# page = requests.get("https://google.com/search", argument_parameter)
# print(page)
# print(page.url)


# #6
# import requests
# argument_parameter = {'q':'john cena','tbm':'isch'}
# page = requests.get("https://google.com/search", argument_parameter)
# print(page)
# print(page.url)


# #7
# import requests
# argument_parameter = {'q':'john cena'}
# page = requests.get("https://google.com/search", argument_parameter)
# print(page)
# print(page.url)


#8
import requests
argument_parameter = {'ml':'breakfast','rel_rhy':'grape'}
page = requests.get("https://api.datamuse.com/words", argument_parameter)
print(page)
print(page.url)

#go and see this url ===> https://www.datamuse.com/api/

# #9 just try
# import requests
# argument_parameter = {'q':'john cena','tbm':'vedio'}
# page = requests.get("https://google.com/search", argument_parameter)
# print(page)
# print(page.url)
