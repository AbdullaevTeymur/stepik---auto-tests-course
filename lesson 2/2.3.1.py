import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link='http://suninjuly.github.io/alert_accept.html'
browser=webdriver.Chrome()
browser.get(link)


try:
    button=browser.find_element_by_css_selector('.btn').click()
    alert=browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    submit = browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(10)
    browser.quit()