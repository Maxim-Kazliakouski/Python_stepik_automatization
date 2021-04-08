# import math
# from selenium import webdriver
# import time
#
# try:
#
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/math.html')
#     x_element = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/label[1]/span[2]')
#     x_element = x_element.text
#     # print(x_element)
#     x_calc = str(math.log(abs(12 * math.sin(int(x_element)))))
#     input_str = browser.find_element_by_tag_name('input')
#     input_str.send_keys(x_calc)
#     # поиск чекбокса
#     check_box = browser.find_element_by_id('robotCheckbox')
#     # выбор необходимого чекбокса
#     check_box.click()
#     # поиск радиобатона
#     radio_button = browser.find_element_by_id('robotsRule')
#     # выбор необходимого radiobutton
#     radio_button.click()
#     submit_button = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/button[1]')
#     submit_button.click()
#     time.sleep(10)
#
# finally:
#     browser.quit()

# -----------------------------------------
import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    # picture_gold = browser.find_element_by_id('treasure')
    # # при помощи метода get_attribute мы берём занчение аттрибута
    # value_gold = picture_gold.get_attribute('valuex')
    # print(value_gold)
    #
    # x_calc = str(math.log(abs(12 * math.sin(int(value_gold)))))
    # input_str = browser.find_element_by_tag_name('input')
    # input_str.send_keys(x_calc)
    # # поиск чекбокса
    # check_box = browser.find_element_by_id('robotCheckbox')
    # # выбор необходимого чекбокса
    # check_box.click()
    # # поиск радиобатона
    # radio_button = browser.find_element_by_id('robotsRule')
    # # выбор необходимого radiobutton
    # radio_button.click()

    button = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/button[1]')
    time.sleep(10)
    x = button.get_attribute('disabled')
    # if not x:
    #     print('The submit button is active')
    # else:
    #     print('The submit button is non-active')

    if x:
        print('The Submit button has condition disabled')
    else:
        print('Enabled')

finally:
    time.sleep(3)
    browser.quit()