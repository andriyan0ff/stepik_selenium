from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(calc(x))
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot_checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
