# In this code, there is necessary to choice number of link before starting autotest
import time
from selenium import webdriver

try:

    print('1-st link without error', end='\n2-nd link with error')

    def choice_of_link(choice=int(input('\nPlease, choose the number of link: '))):
        if choice == 1:
            link_1 = 'http://suninjuly.github.io/registration1.html'
            return link_1
        else:
            link_2 = 'http://suninjuly.github.io/registration2.html'
            return link_2

    browser = webdriver.Chrome()
    browser.get(choice_of_link())
    first_name = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/input[1]')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/input[1]')
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/form[1]/div[1]/div[3]/input[1]')
    email.send_keys('123@mail.com')
    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()
    time.sleep(3)

    congrats = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/h1[1]')
    congrats = congrats.text

    assert congrats == 'Congratulations! You have successfully registered!'

finally:

    time.sleep(3)
    browser.quit()
