import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/math.html"
browser=webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
input=browser.find_element_by_css_selector('#answer')
input.send_keys(y)
radiobutton=browser.find_element_by_css_selector('#robotsRule')
radiobutton.click()
checkbox=browser.find_element_by_css_selector('#robotCheckbox')
checkbox.click()
submit=browser.find_element_by_css_selector('.btn')
submit.click()

time.sleep(10)
browser.quit()
