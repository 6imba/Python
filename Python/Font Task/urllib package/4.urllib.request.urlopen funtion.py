# # <function urlopen at 0x000001EBBB710670>: used to open a specific url.
# import urllib.request as requestModule
# print(requestModule.urlopen) #<function urlopen at 0x000001EBBB710670>
# print(dir(requestModule.urlopen)) #['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



# <function urlopen at 0x000001EBBB710670>: used to open a specific url.
# Return: response object

import urllib.request as requestModule
responseObject = requestModule.urlopen("https://en.wikipedia.org/wiki/Arjen_Robben")



# print(responseObject) #<http.client.HTTPResponse object at 0x000001E7F9024130>
# print(dir(responseObject)) #['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_chunked', '_read_next_chunk_size', '_read_status', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
# print(responseObject.code) #200: status code
# print(responseObject.length) #604911: size of response in bytes.
# print(responseObject.peek()) # provide small part of response in the form of byte_object.
    # - web server can host binary data in addition to plain HTML file.
# byteObject = responseObject.peek()
# print(type(byteObject)) # <class 'bytes'>
# print(len(byteObject)) # <class 'bytes'>
# print(responseObject.length) #604911: size of response in bytes.

# print(responseObject.read()) # provide entire of response in the form of byte_object.
# print(type(responseObject.read())) #<class 'bytes'>
# print(len(responseObject.read())) #<class 'bytes'>



# # decode data:
# decodedStringData = responseObject.read().decode("UTF-8")
# print(decodedStringData)
# print(type(decodedStringData))
# print(len(decodedStringData))

# # If you read url for the second time and it will give you empty byte_object because once you read the response python will closes the connection.
# responseObject.read()
# print(responseObject.read())









    # json.dumps(responseObject) #TypeError: Object of type HTTPResponse is not JSON serializable.




