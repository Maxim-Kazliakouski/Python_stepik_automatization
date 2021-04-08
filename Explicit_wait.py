import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    book_button = browser.find_element_by_id('book')
    # задаём условие для выполнения нажатия кнопки, т.е. когда цена $100 мы нажимаем кнопку
    # т.е. браузер ждёт 12 секунд до появления цены $100, а затем выполняется следующая строка кода
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book_button.click()

    x = browser.find_element_by_id('input_value')
    # переводим полученный текст из переменной в текст
    x = x.text
    # расчитываем формулу
    x_calc = str(math.log(abs(12 * math.sin(int(x)))))
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(x_calc)
    submit_button = browser.find_element_by_id('solve')
    submit_button.click()
    time.sleep(5)
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    browser.quit()