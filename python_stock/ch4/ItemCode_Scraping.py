import requests

url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
resp = requests.get(url)
resp.encoding = "utf-8-sig"
comp = resp.json()
data = comp['Co']

print(data)

