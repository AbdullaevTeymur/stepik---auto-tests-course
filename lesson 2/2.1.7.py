import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link='http://suninjuly.github.io/get_attribute.html'
browser=webdriver.Chrome()
browser.get(link)
try:
    picture=browser.find_element_by_id('treasure')
    x=picture.get_attribute('valuex')
    y=calc(x)
    input=browser.find_element_by_id('answer')
    input.send_keys(y)
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    submit = browser.find_element_by_css_selector('.btn')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()