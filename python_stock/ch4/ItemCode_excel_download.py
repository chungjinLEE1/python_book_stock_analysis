import pandas as pd
import requests
url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
resp = requests.get(url)
resp.encoding = "utf-8-sig"
comp = resp.json()
data = comp['Co']


df = pd.DataFrame(data=data)

cond = df['gb'] == '701'
df2 = df[cond].copy()
df2.to_excel("code.xlsx")

