import requests

url = "https://finance.daum.net/api/charts/A005930/days?limit=200&adjusted=true"

headers = {
    "referer": "https://finance.daum.net/chart/A005930",
    "user-agent": "Mozilla/5.0"
}

params = {
    "limit": "200",
    "adjusted": "true"
}

resp = requests.get(url, headers=headers, params=params)
print(resp)
data = resp.json()
data = data['data']

for day in data:
    print(day['symbolCode'], day['date'], day['tradePrice'])


