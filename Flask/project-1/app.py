from flask import Flask,render_template,request,redirect,url_for
from urllib import request as request2
import os
from fontTools import ttLib
import json
import csv

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def searchFont():
    if request.method=='POST':
        print("---Lets process url------------------------------------------------------------")
        URL = request.form['url']

        # Request byte_data from the server:
        req = request2.Request(URL) #create request object
        req.add_header('User-Agent', 'Mozilla/5.0') #add header to the request object.
        reqConn = request2.urlopen(req) #send request to the server and receive response(byte_object).
        byteData = reqConn.read() # read response byte_data and end the connection.(return object holding byte data.)

        # Create new_file to write those response byte_data into new_file in binary formate:
        folderPath = './static/fonts'
        fontFileName = URL.split('/')[-1]
        fontFilePath = os.path.join(folderPath,fontFileName)
        fontFile = open(fontFilePath, 'wb')
        fontFile.write(byteData) #open file(binary formate) to write.(create specific file if not exist.)
        fontFile.close()
        # Till now file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2) is created.

        # Extract fontFile data.
        # Manipulating fonts of file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).(fontTools is a library written in Python, for manipulating font files.)
        font = ttLib.TTFont(fontFilePath) #load an existing font_file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).
        fontData1 = []

        for i in range(0,20):
            fontData1.append(font['name'].getDebugName(i))
        
        # Store fonFile data into csv file:
        # csvFileName = fontFileName.split('.')[0]+'.csv'
        # csvFilePath = os.path.join('./static/csv',csvFileName)
        csvFilePath = '.\static\csv\\fontData.csv'
        csvFile = open(csvFilePath, 'w', newline='')
        writerObj = csv.writer(csvFile)
        writerObj.writerow(fontData1)
    
        return fontData1

    print("---Get Landing page------------------------------------------------------------")
    return render_template('search-font.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)