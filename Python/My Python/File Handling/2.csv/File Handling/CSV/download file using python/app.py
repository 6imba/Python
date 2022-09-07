import requests

URL = "https://monotype-my.sharepoint.com/:x:/p/roshan_shrestha/EfFeB8cZDHFIvj1OgFTuqx4B9kU0wBinnbMkw3rMYJGvOw?e=4%3AP4KJ1h&at=9"
response = requests.get(URL)
open("./excelfile.xlsx", "wb").write(response.content)