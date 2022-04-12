from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/item/main.naver?code=252670"
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'jpg')
    pgrr = html.find('td', class_='pgPR')
    print(pgrr.a['href'])

print(pgrr.prettify())
print(pgrr.text)





