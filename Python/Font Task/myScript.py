import urllib.request
import os



# URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
# req = urllib.request.Request(URL)
# print(req)



# # Customize the default User-Agent header value:
# req.add_header('User-Agent', 'Mozilla/5.0')
# print(req)
# r = urllib.request.urlopen(req)
# print(r)
filepath = 'C:\\Users\\DELL\\Desktop\\Python Node Task\\myFont.woff2'
# file = open(filepath, 'wb') #Open file to write binary data
# print(file)
# print(type(file)) # <class '_io.BufferedWriter'>
# file.write(r.read()) # write byte code into file. # Write binary data to the file.
# file.close()



from fontTools import ttLib # ExternalModule:fontTools ==> pip install fonttools==3.13.1 =====> <module 'fontTools.ttLib' from 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\fontTools\\ttLib\\__init__.py'>
# print(ttLib)

font = ttLib.TTFont(filepath)
# print(font)

# fontFamilyName = font['name'].getDebugName(1)
# print(fontFamilyName)

fullName= font['name'].getDebugName(4)
# print(fullName)

publisher = font['name'].getDebugName(11)
# print(publisher)

print('Font_Name: %s. \nPublisher_Name: %s.'%(fullName,publisher))
