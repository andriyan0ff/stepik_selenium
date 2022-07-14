from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()
    otvet = browser.switch_to.alert.text
    print(otvet)

finally:
    time.sleep(10)
    browser.quit()