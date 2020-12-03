import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link='http://suninjuly.github.io/selects1.html'
browser=webdriver.Chrome()
browser.get(link)


try:
    x=browser.find_element_by_id('num1').text
    y=browser.find_element_by_id('num2').text
    z=str(int(x)+int(y))
    select=Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(z)
    submit=browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()

