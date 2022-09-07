# params = {"name":"Amir Shrestha", "age":22}
# print(params)

# from urllib import parse
# print(parse) #<module 'urllib.parse' from 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib\\parse.py'>
# print(dir(parse))

# params = {"name":"Amir Shrestha", "age":22}
# from urllib import parse
# print(parse.urlencode(params))

from urllib import parse,request
paramsData = {"v":"LosIGgon_KM", "t":"98s"}
queryString = parse.urlencode(paramsData)
url = "https://www.youtube.com/watch?" + queryString
youtubeResposneObject  =  request.urlopen(url)
print(youtubeResposneObject.isclosed())
print(youtubeResposneObject.read())
print(youtubeResposneObject.isclosed())
