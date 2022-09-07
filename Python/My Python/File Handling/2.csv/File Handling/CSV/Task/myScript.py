from urllib import request
import os
from fontTools import ttLib
import csv

# Process url list:
def process_url(urlList):
    for url in urlList:
        retrive_font_data(url)

# Function to Retrive data of font_file on given URL:
def retrive_font_data(url):
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
    for i in range(0,20):
        fontData.append(font['name'].getDebugName(i))
    save_in_csv(fontData)

def save_in_csv(dataList):
    csvFile = open('./csv/fontData.csv','a',encoding='utf-8',newline='') #file_object
    writerObj = csv.writer(csvFile) # writer_object of writer class.
    writerObj.writerow(dataList)
    csvFile.close()

def get_url():
    csvUrl = open('./csv/fontUrl.csv','r',newline="")
    head = [next(csvUrl) for x in range(20)]
    return head

# Main Python Program Execution:
urlList = [
    "https://quiz.marquiz.ru/static/fonts/Gilroy/Medium.woff2",
    "https://static.parastorage.com/services/wix-vod-widget/df009336a13c216ac2eaaac90f0ac4fa2c61bed7c394488f045e2a28/fonts/fontello-6ca0253cd9b16fcb5dcf9e7f7ca6c1ef.woff",
    "https://westcoastin.com/wp-content/themes/porto/fonts/minicart-font/minicart-font.woff",
    "https://www.hbm.hu/wp-content/plugins/ct-ultimate-gdpr/assets/css/fonts/montserrat/Montserrat-SemiBold.woff2",
    "https://ontarioberries.com/css/fontkit/elsnerflake_-_windsoref-bold-webfont.woff2",
    "https://zavak.com.vn/wp-content/themes/flatsome/assets/css/icons/fl-icons.woff",
    "https://batavia90.nl/wp-content/plugins/elementor/assets/lib/font-awesome/webfonts/fa-solid-900.woff2",
    "https://www.mrshortgame.com/wp-content/plugins/bloom/core/admin/fonts/modules.ttf",
    "https://static.wixstatic.com/ufonts/c59cfc_157f288f30c743499a8cf98575c10d0b/woff2/file.woff2",
    "https://sf.wildapricot.org/BuiltTheme/building_blocks_duotone.v3.0/current/0dbf01d4/Fonts/ubuntu-m-webfont.woff2",
    "https://www.agriland.ee/templates/purity_iii/fonts/sourcesanspro/sourcesanspro-semibold.woff2",
    "https://autohoist.com.au/wp-content/plugins/elementor/assets/lib/font-awesome/webfonts/fa-solid-900.woff2",
    "https://www.tutorialmaster.org/wp-content/themes/Extra/core/admin/fonts/modules.ttf",
]
process_url(urlList)



