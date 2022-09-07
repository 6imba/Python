from urllib import request
import os
from fontTools import ttLib

URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'

# Request byte_data from the server:
req = request.Request(URL) #create request object
req.add_header('User-Agent', 'Mozilla/5.0') #add header to the request object.
reqConn = request.urlopen(req) #send request to the server and receive response(byte_object).
byteData = reqConn.read() # read response byte_data and end the connection.(return object holding byte data.)



# Create new_file to write those response byte_data into new_file in binary formate:
folderPath = 'C:\\Users\\DELL\\Desktop\\Python Node Task\\Task1'
fileName = URL.split('/')[-1]
filepath = os.path.join(folderPath,fileName)
file = open(filepath, 'wb')
file.write(byteData) #open file(binary formate) to write.(create specific file if not exist.)
file.close()
# Till now file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2) is created.



# Manipulating fonts of file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).(fontTools is a library written in Python, for manipulating fonts.)
font = ttLib.TTFont(filepath) #load an existing font_file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).
fontFamilyName = font['name'].getDebugName(1) #none
fullName= font['name'].getDebugName(4)
publisher = font['name'].getDebugName(11)
# print('Font_Name: %s. \nPublisher_Name: %s.'%(fullName,publisher))
print(font['name'])
print(type(font['name']))