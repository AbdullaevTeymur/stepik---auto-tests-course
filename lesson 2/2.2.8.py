import time
from selenium import webdriver
import os

link='http://suninjuly.github.io/file_input.html'
browser=webdriver.Chrome()
browser.get(link)
try:
    input_fname=browser.find_element_by_css_selector('[name=firstname]').send_keys('ivan')
    input_lname=browser.find_element_by_css_selector('[name=lastname]').send_keys('ivanov')
    input_email=browser.find_element_by_css_selector('[name=email]').send_keys('ivan@ivan.rt')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2.2.8.txt')           # добавляем к этому пути имя файла
    element=browser.find_element_by_id('file')
    element.send_keys(file_path)
    submit=browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(10)
    browser.quit()