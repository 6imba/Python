# from urllib import request

# url1 = "https://jsonplaceholder.typicode.com/users"

# req1 = request.Request(url1)
# print(req1)
# reqConn1 = request.urlopen(req1)
# print(reqConn1)
# byteData1 = reqConn1.read()
# print(byteData1)

# file_obj_1 = open("./file_store/test.json", 'wb')
# file_obj_1.write(byteData1)
# file_obj_1.close()


# from urllib import request
# url2 = "https://static-webfonts.myfonts.com/kit/RooneySans_normal_normal/font.woff2"
# req2 = request.Request(url2)
# print(req2)
# req2.add_header('User-Agent', 'Mozilla/5.0')
# reqConn2 = request.urlopen(req2)
# print(reqConn2)
# byteData2 = reqConn2.read()
# print(byteData2)
# file_obj_2 = open("./file_store/font.woff2", 'wb')
# file_obj_2.write(byteData2)
# file_obj_2.close()


# from urllib.request import Request, urlopen
# req3 = Request(
#     url = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/fonts/slick.woff',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn3 = urlopen(req3)
# byteData3 = reqConn3.read()
# file_obj_3 = open("./file_store/slick.woff", 'wb')
# file_obj_3.write(byteData3)
# file_obj_3.close()


# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://jsonplaceholder.typicode.com',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/index.html", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://www.linotype.com/css/fonts/fontello.woff2?30518695',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/fontello.woff2", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# from urllib.request import Request, urlopen
# req4 = Request(
#     url = 'https://www.linotype.com/css/fonts/fontello.woff2?30518695',
#     headers = {'User-Agent': 'Mozilla/5.0'}
# )
# reqConn4 = urlopen(req4)
# byteData4 = reqConn4.read()
# file_obj_4 = open("./file_store/fontello.txt", 'wb')
# file_obj_4.write(byteData4)
# file_obj_4.close()



# Reference:
    # https://fluentprogramming.com/python-urllib-error-httperror-http-error-403-forbidden/
    # https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/


# mod security ===> scraping bot ===> detecting/blocking ===> include user-agent/s in our scraper -> headers = {'User-Agent': 'Mozilla/5.0'}

# The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.



