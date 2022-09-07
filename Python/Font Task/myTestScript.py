import urllib.request
import os

# folder1=r'C:\Users\jhab\Desktop\FontFiles'
URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
# filepath = os.path.join(folder1, URL.split('/')[-1])
# filepath = 'C:\Users\DELL\Desktop\Python Node Task\myFont.woff2'
# print(filepath)
req = urllib.request.Request(URL) #open url
print(req)




print('1 *************************************************************')

# Customize the default User-Agent header value:
req.add_header('User-Agent', 'Mozilla/5.0')
print(req)
r = urllib.request.urlopen(req)
print(r)



# filepath = 'C:\\Users\\DELL\\Desktop\\Python Node Task'
filepath = 'C:\\Users\\DELL\\Desktop\\Python Node Task\\myFont.woff2'

file = open(filepath, 'wb') # The wb indicates that the file is opened for writing in binary mode.
print(file)
print(type(file)) # <class '_io.BufferedWriter'>
# print(r.read()) # byte code
file.write(r.read()) # write byte code into file.
file.close()




print('2 *************************************************************')

from fontTools import ttLib # ExternalModule:fontTools ==> pip install fonttools==3.13.1 =====> <module 'fontTools.ttLib' from 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\fontTools\\ttLib\\__init__.py'>
print(ttLib)

# font = ttLib.TTFont(filepath)
# print(font)
# The WOFF2 decoder requires the Brotli Python extension, available at: https://github.com/google/brotli
# ImportError: No module named brotli
# ==> pip install brotli

font = ttLib.TTFont(filepath)
print(font)

fontFamilyName = font['name'].getDebugName(1)
print(fontFamilyName)

fullName= font['name'].getDebugName(4)
print(fullName)

publisher = font['name'].getDebugName(11)
print(publisher)

print('Font_Name: %s. \nPublisher_Name: %s.'%(fullName,publisher))
