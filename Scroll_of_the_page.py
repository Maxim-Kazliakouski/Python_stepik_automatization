import math
from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    x_element = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/label[1]/span[2]')
    x_element = x_element.text
    # print(x_element)
    x_calc = str(math.log(abs(12 * math.sin(int(x_element)))))
    input_str = browser.find_element_by_tag_name('input')
    input_str.send_keys(x_calc)
    # поиск чекбокса
    check_box = browser.find_element_by_id('robotCheckbox')
    # выбор необходимого чекбокса
    check_box.click()
    # поиск радиобатона
    radio_button = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[4]/input[1]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    # выбор необходимого radiobutton
    radio_button.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(10)
    browser.quit()