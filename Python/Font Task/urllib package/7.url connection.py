from urllib import request as requestModule
responseConnectionObj = requestModule.urlopen('https://youtu.be/LosIGgon_KM?t=338')
print(responseConnectionObj.isclosed())
responseConnectionObj.read() # once we read a response object returned by urlopen(), connection is ended.
print(responseConnectionObj.isclosed())
