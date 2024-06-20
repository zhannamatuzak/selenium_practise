from selenium import webdriver

# Define a global variable
driver = webdriver.Chrome()


# Function to reject cookies
def reject_cookies():
    # open the web browser at the specified URL
    driver.get('https://www.google.com')
    # find the button on the page using the specified locator
    reject_all_button = driver.find_element("xpath", '//button[@id="W0wltc"]')
    # Click the button
    reject_all_button.click()


# Function to find the search field and type there smth
def search_field_type():
    # find the search field area
    google_search_field = driver.find_element("xpath", '//textarea[@id="APjFqb"]')
    # click on the field to have it active
    google_search_field.click()
    # find the text we want to search and click enter (\n)
    google_search_field.send_keys('xpath cheat sheets\n')


if __name__ == "__main__":
    reject_cookies()
    search_field_type()
    driver.quit()
