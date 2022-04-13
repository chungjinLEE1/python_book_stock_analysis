import requests

def kor2eng(query):
    url = "https://translate.kakao.com/translator/translate.json"

    headers = {
        "Referer": "https://translate.kakao.com/",
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "queryLanguage": "kr",
        "resultLanguage": "en",
        "q": query
    }

    resp = requests.post(url, headers=headers, data=data)
    data = resp.json()
    output = data['result']['output'][0][0]
    return output


if __name__ == "__main__":
    print(kor2eng("밥은 먹었니?"))
    print(kor2eng("코로나19 조심해"))