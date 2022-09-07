import urllib.request
import os
folder1=r'C:\Users\jhab\Desktop\FontFiles'


URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
filepath = os.path.join(folder1, URL.split('/')[-1])



req = urllib.request.Request(URL)



# Customize the default User-Agent header value:
req.add_header('User-Agent', 'Mozilla/5.0')
r = urllib.request.urlopen(req)



file = open(filepath, 'wb')
file.write(r.read()) #open file(binary formate) to write.(create specific file if not exist.)
file.close()


# fontTools is a library written in Python, for manipulating fonts.
from fontTools import ttLib
font = ttLib.TTFont(filepath)
fontFamilyName = font['name'].getDebugName(1)
fullName= font['name'].getDebugName(4)
publisher = font['name'].getDebugName(11)
publisher,fullName