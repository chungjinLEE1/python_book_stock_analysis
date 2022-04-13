import requests

url = "https://translate.kakao.com/translator/translate.json"

headers = {
    "Referer": "https://translate.kakao.com/",
    "User-Agent": "Mozilla/5.0"
}


data = {
    "queryLanguage": "kr",
    "resultLanguage": "en",
    "q": "안녕하세요"
}

resp = requests.post(url, headers=headers, data=data)
data = resp.json()
print(data)


output = data['result']['output'][0][0]
print(output)
