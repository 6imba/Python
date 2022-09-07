from urllib import request
import os
from fontTools import ttLib
import csv
import time
import mysql.connector
from db import save_in_metadata, save_in_site_url

def get_url_list():
    url_file = open('../file_base/font_url.csv')
    for row in url_file:
        urls = row.strip().split(',')
        print(len(urls))
        fontData = process_url(urls[1])
        fk = save_in_metadata(fontData)
        save_in_site_url([urls[0],1,0])
        save_in_site_url([urls[1],2,fk])

def process_url(url):
    fileName = url.split('/')[-1]
    extension = fileName.split('.')[-1]
    filePath = os.path.join('../font_dir',fileName)
    if extension not in ['woff','woff2','ttf','otf','eot']: return # only 'woff','woff2','ttf','otf' extension is allowed.
    try:
        return retrive_font_data(url,filePath)
    except Exception as e:
        if os.path.exists(filePath): os.remove(filePath)
        print("Error ==> ",e)

def retrive_font_data(url,filePath):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    reqConn = request.urlopen(req)
    byteData = reqConn.read()
    file = open(filePath, 'wb')
    file.write(byteData)
    file.close()
    # Till now we have just downloaded the file.
    font = ttLib.TTFont(filePath) #load an existing font_file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).    
    fontData = []
    fontData.append(url) # add url of all meta data
    for i in range(0,19):
        fontData.append(font['name'].getDebugName(i))
    os.remove(filePath) # delete local downloaded font file.
    return fontData


# Main Python Program Execution:
url_list = get_url_list()
