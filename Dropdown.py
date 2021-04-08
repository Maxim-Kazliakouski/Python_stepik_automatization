import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    # time.sleep(1)
    first_element = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/h2[1]/span[2]')
    second_element = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/h2[1]/span[4]')
    first_element = first_element.text
    second_element = second_element.text
    summa = int(first_element) + int(second_element)
    summa = str(summa)

    select_element = Select(browser.find_element_by_id('dropdown'))
    # time.sleep(3)
    select_element.select_by_value(summa)
    # time.sleep(5)
    button = browser.find_elements_by_xpath('/html[1]/body[1]/div[1]/form[1]/button[1]')
    button.click()

finally:
    time.sleep(1)
    browser.quit()







