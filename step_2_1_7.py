from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x_element.get_attribute('valuex')))
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()


finally:
    time.sleep(10)
    browser.quit()