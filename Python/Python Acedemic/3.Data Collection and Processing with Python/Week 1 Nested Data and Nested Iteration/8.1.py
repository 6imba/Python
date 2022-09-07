# import json 
  
# # initializing string  
# test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}' 
  
# # printing original string  
# print("The original string : " + test_string) 
  
# # using json.loads() 
# # convert dictionary string to dictionary 
# res = json.loads(test_string) 
  
# # print result 
# print(res)

# print(type(res))
# print("The converted dictionary : " + str(res))


# jsfile = open ('8.1.Json.File.txt')
# text = jsfile.read()
# print(text)
# print(type(text))


# jsfile = open ('8.1.Json.File.txt')
# text = jsfile.read()
# print(text)
# print(type(text))
# a=dict(text)
# print(a)
# print(type(a))



# import json 
# test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}' 
# print("The original string : " + test_string) 
# res = json.loads(test_string) 
# print(res)
# print(type(res))
# print("The converted dictionary : " + str(res))




jsfile = open ('8.1.Json.File.txt')
text = jsfile.read()
print(text)
print(type(text))

import json
jsfile = json.loads(text) # convert str file to json/dictiony file
print(jsfile)
print(type(jsfile))

