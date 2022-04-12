import pandas as pd

df = pd.read_html('http://kind.krx.co.kr/corgeneral/corpList.do?method=download&searchType=13')[0]
df = df.sort_values(by='종목코드')
print(df)


