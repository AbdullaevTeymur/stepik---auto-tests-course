import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link='http://SunInJuly.github.io/execute_script.html'
browser=webdriver.Chrome()
browser.get(link)
try:
    x=browser.find_element_by_id('input_value').text
    y=calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    browser.execute_script("window.scrollBy(0, 130);")
    checkbox=browser.find_element_by_id('robotCheckbox').click()
    radiobutton=browser.find_element_by_id('robotsRule').click()
    submit=browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(5)
    browser.quit()