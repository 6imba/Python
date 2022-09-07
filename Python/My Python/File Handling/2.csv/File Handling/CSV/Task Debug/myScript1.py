from urllib import request
import os
from fontTools import ttLib
import csv

# Function to Retrive data of font_file on given URL:
def retrive_font_data(url):
    url
    # Request byte_data from the server:
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    reqConn = request.urlopen(req)
    byteData = reqConn.read()
    # Create new_file to write those response byte_data into new_file in binary formate:
    folderPath = './fonts'
    fileName = url.split('/')[-1]
    filepath = os.path.join(folderPath,fileName)
    print(filepath)
    file = open(filepath, 'wb')
    file.write(byteData)
    file.close()
    # Till now file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2) is created.
    # Manipulating fonts of file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).(fontTools is a library written in Python, for manipulating font files.)
    font = ttLib.TTFont(filepath) #load an existing font_file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).    
    fontData = []
    for i in range(0,16):
        fontData.append(font['name'].getDebugName(i))
    save_in_csv(fontData)

def save_in_csv(dataList):
    # csvFile = open('fontData.csv','a',newline='') #file_object
    # csvFile = open('fontData.csv','a',encoding='utf-8') #file_object
    csvFile = open('fontData.csv','a',encoding='utf-8',newline='') #file_object
    writerObj = csv.writer(csvFile) # writer_object of writer class.
    writerObj.writerow(dataList) # returns character length. # overwrite file_content with new_row + two linw_break(/n)
    # csvFile.close()

    
# Main Python Program Execution:
# urlList = ["https://fast.fonts.net/FontsCom/Live/static/2.15.911.0/font/ss-pika.woff","https://static-webfonts.myfonts.com/kit/RooneySans_normal_normal/font.woff2","https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2"]
# url = "https://fast.fonts.net/FontsCom/Live/static/2.15.911.0/font/ss-pika.woff"
# url = "https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2"

url = "https://static-webfonts.myfonts.com/kit/RooneySans_normal_normal/font.woff2"
retrive_font_data(url)

