import time
from selenium import webdriver
# инициализируем браузер для через webdriver
browser = webdriver.Chrome()
time.sleep(5)
# открываем сайт
browser.get('http://suninjuly.github.io/simple_form_find_task.html')
time.sleep(3)
# ищем кнопку по нужному селектору
button_submit = browser.find_element_by_id('submit_button')
if button_submit:
    print('The submit button was found')
browser.quit()

# ------------ также есть второй универсальный метод поиска элементов -----------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
time.sleep(5)
# открываем сайт
browser.get('http://suninjuly.github.io/simple_form_find_task.html')
time.sleep(3)
# ищем кнопку по нужному селектору
button_submit = browser.find_element(By.ID, 'submit_button')
if button_submit:
    print('The submit button was found')
browser.quit()

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#------ Поиск по тексту в ссылке или по частичному её совпадению ----
import math
import time
from selenium import webdriver

try:

    a = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    browser = webdriver.Chrome()
    go_to_url = browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_link_text(a)
    link.click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

#----- Поиск при помощи find_elements_by -----
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[1]/form[1]/div[6]/button[3]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
