from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('ivanov@supernatural.ru')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()