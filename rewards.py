import argparse

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

SITE_URL = 'https://watch.eune.lolesports.com/en-US'


def define_arguments():
    p = argparse.ArgumentParser(description='LOL-esports rewards bot')
    p.add_argument('-u', '--username', required=True, help='League of Legends account name')
    p.add_argument('-p', '--password', required=True, help='League of Legends account password')
    p.add_argument('-s', '--server', required=True, help='League of Legends account region')

    return p


def inti():
    chrome_driver = webdriver.Chrome('/home/satner/PycharmProjects/lol-esports-dummy-bot/chromedriver')
    chrome_driver.set_window_size(1250, 937)
    # driver.implicitly_wait(10)
    chrome_driver.get(SITE_URL)
    try:
        myElem = WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="riotbar-account"]')))
        print("lol-esports page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    return chrome_driver


def login(username, password, server):
    login_container = driver.find_element_by_xpath('//div[@id="riotbar-account"]')

    login_link = login_container.find_elements_by_tag_name('a')[1]
    login_link.click()

    login_page_form = ''
    try:
        login_page_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//form')))
        print("Login page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    form_input_fields = login_page_form.find_elements_by_xpath('//form//input')
    login_page_form.find_element_by_xpath('//div[@id="region-selector"]//span').click()

    username_field = form_input_fields[0]
    username_field.send_keys(username)

    password_field = form_input_fields[1]
    password_field.send_keys(password)

    expanded_dropdown = Select(driver.find_element_by_xpath('//select[@class="custom-select-combobox"]'))
    expanded_dropdown.select_by_value(server)

    driver.find_element_by_xpath('//button').click()


if __name__ == '__main__':
    parser = define_arguments()
    args = vars(parser.parse_args())
    if len(args) < 3:
        parser.print_help()
        exit()

    driver = inti()
    login(args['username'], args['password'], args['server'])
