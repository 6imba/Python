import csv

csvLink = open('./fontLink.csv','r') #file_object
csvUrl = open('./fontUrl.csv','w',newline='') #file_object

readerObject = csv.reader(csvLink)
writerObject = csv.writer(csvUrl)

for row in readerObject:
    writerObject.writerow([row[1]])

