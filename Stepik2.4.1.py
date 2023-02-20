from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element.text
    x = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(x)
    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()