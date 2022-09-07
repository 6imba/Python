#3
import requests
argument_parameter = {'rel_rhy':'funny'}
page = requests.get("https://api.datamuse.com/words",argument_parameter)
print(page)
print("\n .............................. \n")
print(page.text)
print("\n .............................. \n")
print(page.text[:150])
print("\n .............................. \n")
print(page.url)

