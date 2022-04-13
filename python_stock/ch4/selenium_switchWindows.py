from selenium import webdriver


driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.get('http://naver.com')
#
# selector = ""
# elem = driver.find_element_by_css_selector(selector)
# elem.click()
#
# print(driver.window_handles)
# print("to_switch" + driver.to_switch(driver.window_handles[1]))



driver.get('http://google.co.kr')


selector = ""

elem = driver.get_find_element_by_selector(selector)

href = elem.get_attribute('href')
print(href)