# import urllib.request
# folder1=r'C:\Users\jhab\Desktop\FontFiles'


# URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
# # print(URL.split('/')[-1])
# # print(URL.split('/'))
# # print(URL.split())
# print(URL.split('/'))
# print(URL.split('/')[-1])
# print(type(URL.split('/')[-1])) # <class 'str'>

# import os
# # filepath = os.path.join(folder1, URL.split('/')[-1])
# dirPath = os.getcwd()
# print(dirPath) # C:\Users\DELL\Desktop\Python Node Task
# fileList = os.listdir()
# print(fileList) 
# fontFolder = os.listdir()[0]
# print(fontFolder) 
# # print(fontFolder.listdir()) 


# fontFilePath = 'C:\Users\DELL\Desktop\Python Node Task\myFont.woff2'


# filepath1 = os.path.join('C:\Users\DELL\Desktop\Python Node Task', URL.split('/')[-1])
# print(filepath1)
# filepath1 = os.path.join('C:\Users\DELL\Desktop\Python Node Task', 'myFont.woff2')
# print(filepath1)
# print('myFont.woff2')
# print(type('myFont.woff2'))
# filepath1 = os.path.join('C:\\Users\\DELL\\Desktop\\Python Node Task', 'myFont.woff2')
# print(filepath1)
# filepath2 = 'C:\\Users\\DELL\\Desktop\\Python Node Task\\myFont.woff2'
# print(filepath2)


# f1 = open("urllib package.txt", "r")
# print(f1.read())
# f2 = open("urllib package.txt", "wb")
# f2.write("\napple")
# b'wOF2\x00\x01\x1c\x91\xbb\xf6\xe0\xde\'

import urllib.request
print(urllib.request.Request)
# import urllib VS import urllib.request