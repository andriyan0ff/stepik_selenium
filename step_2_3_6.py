from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_page.html?"
    browser = webdriver.Chrome()
    browser.get(link)



    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME, 'button').click()
    otvet = browser.switch_to.alert.text
    print(otvet)


finally:
    time.sleep(10)
    browser.quit()