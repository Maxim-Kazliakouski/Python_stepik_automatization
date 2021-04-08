import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_name('email')
    email.send_keys('123@mail.ru')
# прописываем путь к папке с пректом (текущая папка)
    current_dir = os.path.abspath(os.path.dirname(__file__))
# указываем путь к файлу, который необходимо отправить
    file_path = os.path.join(current_dir, 'file.txt')
    choose_button = browser.find_element_by_name('file')
# передаём файл, который необходимо прикрепить через кнопку
    choose_button.send_keys(file_path)
    submit_button = browser.find_element(By.XPATH, '/html[1]/body[1]/div[1]/form[1]/button[1]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
