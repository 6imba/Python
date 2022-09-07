from urllib import request as requestModule
# Success:
youtubeResposneObject  =  requestModule.urlopen('https://www.youtube.com/watch?v=LosIGgon_KM&t=98s')
print(youtubeResposneObject)
print(youtubeResposneObject.code)
# Forbidden: search_query(may be because of sql_query_injection)
goggleSearchQueryResposneObject  =  requestModule.urlopen('https://www.google.com/search?q=amir')
print(goggleSearchQueryResposneObject)