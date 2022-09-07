from urllib import request
URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
req = request.Request(URL)
# print(req) #<urllib.request.Request object at 0x000001F6F924AE90>
# till date no connection is established.
# print(dir(req))
# print(req.add_header) #<bound method Request.add_header of <urllib.request.Request object at 0x00000218AA54AE60>>
req.add_header('User-Agent', 'Mozilla/5.0')
# print(req)
reqConn = request.urlopen(req)
# print(reqConn)
byteData = reqConn.read() #object holding byte data.

