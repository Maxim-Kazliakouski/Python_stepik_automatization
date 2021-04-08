import time
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    fly_button = browser.find_element_by_class_name('trollface.btn.btn-primary')
    fly_button.click()
    time.sleep(3)
    # создаём переменную с именем вторй вкладки
    second_tab = browser.window_handles[1]
    # переходим на вторую вкладку
    browser.switch_to_window(second_tab)
    x = browser.find_element_by_id('input_value')
    # переводим полученный текст из переменной в текст
    x = x.text
    # расчитываем формулу
    x_calc = str(math.log(abs(12 * math.sin(int(x)))))
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(x_calc)
    submit_button = browser.find_element_by_class_name('btn.btn-primary')
    submit_button.click()
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    time.sleep(3)
    browser.quit()