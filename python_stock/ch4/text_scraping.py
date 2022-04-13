from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver.exe")
url = "https://m.stock.naver.com/"
driver.get(url)

css_selector = "#content > div > div:nth-child(13) > div.NewsList_newsArea__TY6KM > ul > li:nth-child(1) > div > a"
elem = driver.find_element_by_css_selector(css_selector)
print(elem.text)

css_selector = "#content > div > div:nth-child(13) > div.NewsList_newsArea__TY6KM > ul > li:nth-child(2) > div > a"
elem = driver.find_element_by_css_selector(css_selector)
print(elem.text)


for i in range(1, 10):
    css_selector ="#content > div > div:nth-child(13) > div.NewsList_newsArea__TY6KM > ul > li:nth-child({i}) > div > a"
    elem = driver.find_element_by_css_selector(css_selector)
    print(elem.text)


css_selector = "#content > div > div:nth-child(13) > div.NewsList_newsArea__TY6KM > ul > li:nth-child({i}) > div > a"
result = driver.find_element_by_css_selector(css_selector)
print(type(result))
print(type(result[0]))


for item in result:
    print(item.text)