from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("http://naver.com")

css_selector = "#query"
elem = driver.find_element_by_css_selector(css_selector)
elem.send_keys("부동산")
elem.send_keys(Keys.RETURN)