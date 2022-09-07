# loads ==> str -> dict/keys
# dumps ==> dict/list -> str


# JSON Syntax Rules
# Data is in name/value pairs
# Data is separated by commas
# Curly braces hold objects
# Square brackets hold arrays

# example:
# JSON data : JSON data is written as name/value pairs.A  name/value pair consists of a field name (in double quotes), followed by a colon ==> "firstName":"John",
# JSON Objects : JSON objects are written inside curly braces. Objects can contain multiple name/value pairs. {} ==> employees
# JSON Arrays : JSON arrays are written inside square brackets. An array can contain objects: [] ==>  {"firstName":"John", "lastName":"Doe"}

# {
# "employees":[
#     {"firstName":"John", "lastName":"Doe"},
#     {"firstName":"Anna", "lastName":"Smith"},
#     {"firstName":"Peter", "lastName":"Jones"}
# ]
# }

# # 1
# # 17.3. Processing JSON results
# # JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists in python when we write them out
#  as literals in a program, but with a few small differences (e.g., the word null instead of None). When your program receives a JSON-formatted string,
#  generally you will want to convert it into a python object, a list or a dictionary.

# # Again, python provides a module for doing this. The module is called json. We will be using two functions in this module, loads and dumps.

# # json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.

# # Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:


# # 2
# #loads()

# import json
# x = '{ "resultCount":25, "results": [{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
# print(x)
# print("------")

# a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
# print(a_string)
# print("------")
# \
# d = json.loads(a_string)
# print(type(d))
# print(d.keys())
# print(d['resultCount'])
# print(d)
# # print(a_string['resultCount']) error as a_string is not dict to access key'resultCount'


# 3
# a_string => simply string cantaining different character like \n_newlinecharacter,{}_suggest_string is goona be dict.....
# json.loads() => take string as input and returns either python dic or list
# d hold type dict


# # 4
# #dumps()
# #The other function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary or a list, and 
# returns a string, in JSON format. 
# # It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, 
# the keys of dictionaries are output in alphabetic order with their values.
# # The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and 
# indentation for nested lists or dictionaries.
# # For example, the following function uses json.dumps to make a human-readable printout of a nested data structure.

# import json

# dictionary = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}
# print(dictionary)
# print('--------')

# Dict_Json1 = json.dumps(dictionary, indent=2)
# print(Dict_Json1)

# Dict_Json2 = json.dumps(dictionary,sort_keys=True, indent=2) # When the value True is passed for the sort_keys parameter,  the keys of dictionaries are output in alphabetic order with their values
# print(Dict_Json2)
# print(type(Dict_Json2))


# # JSON dot Load S, loads from a string, into a Python object, either a list or a dictionary, 
# # and 
# # JSON dot dump S dumps from a Python list or dictionary into a string. 
# #indent ==> JSON dot Dump S, with the indent parameter, yields a string with indentation, that makes it easier for people to read and understand.
# # sort_ker=True ==> sort the key of dict


# # 5


# # we have the two most useful functions. Let's take a look at them. The first one is called Load S. It takes a string as input, and it returns a dictionary or a list. So, here we have little code snippet. We're importing the JSON module, and then we've got a variable called A string whose value is naturally a string, and that string has some newline characters in it, and then it's got the curly brace which would suggest to you that it's going to be a Python dictionary. It's really just a string, but once we take that string and on line three, we pass it as an input to the Load S function, which is part of the JSON module. The Load S function, in the JSON module, takes a string as an input and as an output it produces either a Python list or a Python dictionary depending on what the contents of the string were. So, in this case the string has its first non blank space its non white space character, the first one is a curly brace. So, what's going to be output is a dictionary. So on line four, we print out the type of D, and it is a dictionary. Since it's a dictionary, we can ask for its keys and it has two keys; result count and results. We can ask for the value associated with result count and it's 25. That's the 25 that you see there in the string. One important thing to keep track of here, is when you have a string, and when you have a dictionary. So, we start with something that's a character string, and by passing it in to the Load S function, we get a dictionary as an output. If I lost track of that let's say, and I tried to print a_string square bracket result count. Because a_string kind of looks like a dictionary, and I try to run this, I'm going to get an error. It says its string indices must be integers not strings on line seven. Let's say on line seven, we're trying to treat a_string as if it's a dictionary. It isn't a dictionary, it's a string. We're allowed to ask for a_string square bracket four to get the fourth character, but we can't ask for a_string square bracket result count. We can ask for D square bracket result count, because D is a dictionary. The second useful function from the JSON module is called Dump S. It does the opposite of Load S. It takes a Python list or dictionary, even a nested one, and converts it into a string that's in the JSON format. Once we have a string in the JSON format, we can write it to a file or do anything else that we would do with a string. The Dump S function always takes a list or a dictionary as an input. But it also can take a couple of other parameters. If you pass sort keys equals true, then, whenever you have a dictionary it's going to output those in alphabetic order. If you pass the indent parameter, it will pretty print the string. It'll do some indentation in line breaks. You can specify how many characters of indentation you want. So let's see what happens when we run this.
# # Play video starting at 4 minutes 53 seconds and follow transcript4:53
# # Oops! I got an error. It's telling me that on line two, JSON is not defined. The reason is that I forgot, and I need to import the JSON module. So, the Dump S function is in the JSON module, and this code snippet didn't have the JSON module imported. So let me run it again. Now you can see, when I pass D to the pretty function on line nine, that it is creating a string by calling the json.dumps function and that string, because I said indent equals two, each time I descend one level into this next to the data structure, it's adding two more levels, two more spaces. That makes it just a lot easier for a person to read when I print out that string. Now, you may have noticed little funny pronunciation that I've done here. Instead of calling this Dumps and Loads, I've called it Dump S and Load S. That's very deliberate. It helps me to remind me that that S is for string. The S is not for plural. You still have to remember which of Dump S and Load S reads from a string and which one writes to a string. Here's how I think of it. The JSON format is a set of conventions for how a string should be structured so that it can be loaded into a Python object. Thus, Load S means load from a string or load a string into an object. Dump S means dump an object to a string. Dumping from a string wouldn't really make sense, so that's how I can keep track of it. Dump S, dump an object to a string. Load S, load an object from a string. That's the JSON format folks. We'll be seeing a lot more of it when we look at rest APIs that let us fetch data from servers on the internet, like from iTunes or OMDb. JSON dot Load S, loads from a string, into a Python object, either a list or a dictionary, and JSON dot dump S dumps from a Python list or dictionary into a string. JSON dot Dump S, with the indent parameter, yields a string with indentation, that makes it easier for people to read and understand. See you next time.


# # 6
# # 1.Because we can only write strings into a file, if we wanted to convert a dictionary d into a json-formatted string so that we could store it in a file, what would we use?
# # B. json.dumps(d)


# # 2.nested-9-2: Say we had a JSON string in the following format. How would you convert it so that it is a python list?
# # entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""
# # C. json.loads(entertainment)



# JSON can store Lists, bools, numbers, tuples and dictionaries. But to be saved into a file, all these structures must be reduced to strings. It is the string version that can be read or written to a file. Python has a JSON module that will help converting the datastructures to JSON strings. Use the import function to import the JSON module.

# import json
# The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

# json_string = json.dumps(datastore)
# The JSON module can also take a JSON string and convert it back to a dictionary structure:

# datastore = json.loads(json_string)
# While the JSON module will convert strings to Python datatypes, normally the JSON functions are used to read and write directly from JSON files.

# Writing a JSON fil