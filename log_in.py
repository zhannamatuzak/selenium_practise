import os  # package to interact with the operating system
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By  # By class to locate elements / see line 17

# global variables
driver = webdriver.Chrome()
# Configure environment variables within PyCharm to use secret keys
username = os.environ["BS_USERNAME"]
password = os.environ["BS_PASSWORD"]
# To verify the environment variables are correctly loaded,
# execute in the console:
# print(os.environ.get("BS_USERNAME"))
# print(os.environ.get("BS_PASSWORD"))


# opens the login area
def login_input_area():
    driver.get("https://www.browserstack.com/automate")
    sleep(3)
    driver.maximize_window()
    sign_in_button_locator = (By.XPATH, '//a[@title="Sign in"]//span[@class="item-text"]')
    # sign_in_button = driver.find_element(by=sign_in_button_locator[0], value=sign_in_button_locator[1])
    sign_in_button = driver.find_element(*sign_in_button_locator)
    sign_in_button.click()
    sleep(1)


# reject cookies
def reject_cookies():
    # find the button on the page using the specified locator
    reject_all_button = driver.find_element("xpath", '//button[@id="reject-cookie-notification"]')
    # Click the button
    reject_all_button.click()


# inputs secret keys (username and password) and submits the login form
def login_process_success():
    reject_cookies()
    email_input_locator = (By.XPATH, '//input[@id="user_email_login"]')
    email_input = driver.find_element(*email_input_locator)
    email_input.send_keys(username)
    sleep(1)
    password_input_locator = (By.XPATH, '//input[@id="user_password"]')
    password_input = driver.find_element(*password_input_locator)
    password_input.send_keys(password)
    sleep(1)
    sign_me_in_button_locator = (By.XPATH, '//input[@type="submit"]')
    sign_me_in_button = driver.find_element(*sign_me_in_button_locator)
    sign_me_in_button.click()


# the construct shows that the code runs as the main script, not as a module
if __name__ == "__main__":
    login_input_area()
    login_process_success()
