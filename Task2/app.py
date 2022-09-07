from urllib import request
import os
from fontTools import ttLib
import csv
import pandas as pd
    
def iterate_url_list(url_list):
    for url in url_list:
        create_font_file(url)

def create_font_file(url):
    # read font_file's byte_data from the server:
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    reqConn = request.urlopen(req)
    byteData = reqConn.read()
    # Create font_file from those read byte_data.
    folderPath = './fonts'
    fileName = url.split('/')[-1]
    filepath = os.path.join(folderPath,fileName)
    file = open(filepath, 'wb')
    file.write(byteData)
    file.close()
    # Till now file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2) is created.
    retrive_font_data(filepath)
    
def retrive_font_data(filepath):
    print(filepath)
    font_data = []
    font = ttLib.TTFont(filepath)
    for i in range(0,20):
        font_data.append(font['name'].getDebugName(i))
    
    # Extract fontFile data into csv file:
    csvFilePath = './file_base/font_detial.csv'
    csvFile = open(csvFilePath, 'a', newline='')
    writerObj = csv.writer(csvFile)
    print(font_data)
    writerObj.writerow(font_data)

def get_url_list():
    url_list = []
    url_file = open('./file_base/demo_url.txt')
    for url in url_file:
        url_list.append(url.strip())
    return url_list

# Main Python Program Execution:
url_list = get_url_list()
iterate_url_list(url_list)








# def retrieve_url():
#     read_file = pd.read_excel (r'./file_base/excel.xlsx', index_col=0) # read spreadsheet file by skipping first column
#     read_file.to_csv (r'./file_base/font_url.txt', header=False)  # read csv file by skiping header&index from read spreadsheet file

# retrieve_url()


