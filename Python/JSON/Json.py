# # https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/

# # JSON is the string representation of the data and dictionaries are the actual data structures in memory that are created when the program runs.
# # import json
# # json.function(argument)
# # loads() takes in a string and returns a json object.
# # dumps() takes in a json object and returns a string.




# # 1.1
# #python_dictionary
# prople_text = {'a':    2}
# print(type(prople_text))
# print(prople_text)

# # 1.2
# #python_string OR JSON_formate
# prople_text = "{'a':     2}"
# print(type(prople_text))
# print(prople_text)



# # 2.1
# #python string which has valid Json formate. Multi-line string with JSON format.
# python_string = '''
#     {
#         "people" : [
#             {
#                 "name":"Amir Shrestha",
#                 "phone":"986966605",
#                 "email":["simbaamir55@gmail.com","amirshrestha56@gmail.com"],
#                 "has_license":false
#             },
#             {
#                 "name":"John Cena",
#                 "phone":"1234567890",
#                 "email":null,
#                 "has_license":true
#             }
#         ]
#     }
# '''

# print(type(python_string))
# print(python_string)


# # 2.2
# #python string which has valid Json formate. Multi-line string with JSON format.
# python_dict = {"people" : [
#                             {
#                                 "name":"Amir Shrestha",
#                                 "phone":"986966605",
#                                 "email":["simbaamir55@gmail.com","amirshrestha56@gmail.com"],
#                                 "has_license":False
#                             },
#                             {
#                                 "name":"John Cena",
#                                 "phone":"1234567890",
#                                 "email":None,
#                                 "has_license":True
#                             }
#                         ]
#                 }

# print(type(python_dict))
# print(python_dict)


# # 3 Note:
# # 3.1 Python_string(JSON_Formate)
# # "has_license":false
# # "has_license":true
# # "email":null,

# # 3.2  Python_dictionary(Boolean_Formate)
# # "has_license":False
# # "has_license":True
# # "email":None,


# # 3.3 (load VS dumps)
# # false ===> loads() ==> False
# # False ===> dumps() ==> false


# # 4.1 Python_string(JSON_Formate)
# python_string = '{ "name":"John", "age":30, "city":"New York"}'
# print(type(python_string))

# # 4.2 Python_dictionary
# python_dict = { "name":"John", "age":30, "city":"New York"}
# print(type(python_dict))


# # 5.1 Python_string(JSON_Formate)
# import json
# python_string = '{ "name":"John", "age":30, "city":"New York"}'
# print(type(python_string))
# print(python_string)
# python_dict = json.loads(python_string)
# print(python_dict)
# print(type(python_dict))

# # 5.2 Python_dictionary
# import json
# python_dict = { "name":"John", "age":30, "city":"New York"}
# print(python_dict)
# print(type(python_dict))
# python_string1 = json.dumps(python_dict)
# print(python_string1)
# print(type(python_string1))
# python_string2 = json.dumps(python_dict, indent=0)
# print(python_string2)
# print(type(python_string2))
# python_string3 = json.dumps(python_dict, indent=4)
# print(python_string3)
# print(type(python_string3))



# #Load python_string into an python objects
# #So that we can work with data more easily.
# #So we can use json.loads meathod

# # JSON String to Python Dictionary

# import json #json module
# python_string = '{ "name":"John", "age":30, "city":"New York"}'
# data_obj = json.loads(python_string) #json.loads meathod load python_string into python_object as dictionary.
# print(type(data_obj))
# print(data_obj)

# #So when we load json into python object it uses following conversion table.
# # JSON                Python
# # object              dict
# # array               list
# # string              str
# # number(int)         int
# # number (real)       float
# # true                True
# # false               False
# # null                None




# # Python Dictionary to JSON String
# # here data_obj is python dictionary object

# python_multiline_json_string = json.dumps(data_obj)
# print(python_multiline_json_string)
# print(type(python_multiline_json_string))

# # True    true




# # Print JSON With Indentation ==>  json.dumps(python_dic_obj2, indent=0)
# import json
# python_dic_obj2 = {"name": "Nora", "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": False}
# # print(python_dic_obj2)
# # print(type(python_dic_obj2))
# python_json_string = json.dumps(python_dic_obj2)
# # print(python_json_string)
# # print(type(python_json_string))

# python_json_string1 = json.dumps(python_dic_obj2, indent=0)
# python_json_string2 = json.dumps(python_dic_obj2, indent=4)
# python_json_string3 = json.dumps(python_dic_obj2, indent='\t')

# print(python_json_string1)
# print(python_json_string2)
# print(python_json_string3)




# # Print JSON With Indentation
# import json
# python_dic_obj2 = {"name": {"fname":"Amir", "lname":"Shrestha"}, "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": False}
# # print(python_dic_obj2)
# # print(type(python_dic_obj2))
# python_json_string = json.dumps(python_dic_obj2)
# # print(python_json_string)
# # print(type(python_json_string))

# python_json_string1 = json.dumps(python_dic_obj2, indent=0)
# python_json_string2 = json.dumps(python_dic_obj2, indent=4)
# python_json_string3 = json.dumps(python_dic_obj2, indent='\t')

# print(python_json_string1)
# print(python_json_string2)
# print(python_json_string3)



# # Sort the Keys Json_String ==> json.dump(python_dic_obj2, sort_keys=True)
# import json
# python_dic_obj2 = {"name": "Nora", "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": False}
# python_json_string4 = json.dumps(python_dic_obj2, sort_keys=True)
# print(python_json_string4)



# # Indent and Sort the Keys Json_String ==> json.dumps(python_dic_obj2, indent=4, sort_keys=True)
# import json
# python_dic_obj2 = {"name": "Nora", "age": 56, "id": "45355", "eye_color": "green", "wears_glasses": False}
# python_json_string4 = json.dumps(python_dic_obj2, indent=4, sort_keys=True)
# print(python_json_string4)



# Finaly
# JSON keys should always be inside double_quote ( "keys":value)