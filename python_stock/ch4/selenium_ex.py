from selenium import webdriver
import time
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.naver.com")



css_selector = "#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(9) > a"
element = driver.find_element_by_css_selector(css_selector)
print(type(element))

element.click();


time.sleep(10)

url = "https://www.daum.net"
driver.get(url)

driver.quit()

