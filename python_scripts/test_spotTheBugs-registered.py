from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to Web page
driver.get("https://qa-practice.netlify.app/bugs-form")

# Validate field names are displayed correct

# Validate the inputs are reflecting as expected

first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name.clear()
first_name.send_keys("test 1st name")
last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name.clear()
last_name.send_keys("test last name")
phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
phone_number_locator.clear()
phone_number_locator.send_keys("1234567890")
country_locator = driver.find_element(By.XPATH, "//select[@id='countries_dropdown_menu']")
select = Select(country_locator)
options = select.options
random_option = random.choice(options)
selected_text = random_option.text
selected_value = random_option.get_attribute("value")
select.select_by_visible_text(selected_text)
email = driver.find_element(By.XPATH, "//input[@id='emailAddress']")
email.clear()
email.send_keys("email@test.com")
password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
password_locator.clear()
password_locator.send_keys("password12345")
register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
register_button.click()

def test_first_name_registered():
    first_name_registered = driver.find_element(By.XPATH, "//div[@id='resultFn']")
    assert first_name_registered.text == "First Name: test 1st name", "First Name not matching with user input"

def test_last_name_registered():
    last_name_registered = driver.find_element(By.XPATH, "//div[@id='resultLn']']")
    assert last_name_registered.text == "Last Name: test last name", "Last Name not matching with user input"

def test_phone_registered():
    phone_registered = driver.find_element(By.XPATH, "// div[ @ id = 'resultPhone']")
    assert phone_registered.text == "Phone Number: 1234567890", "Phone number not matching with user input"

def test_country_registered():
    country_registered = driver.find_element(By.XPATH, "// div[ @ id = 'country']")
    assert country_registered.text == f"Country: {selected_text}", "Country not matching with user input"

def test_email_registered():
    email_registered = driver.find_element(By.XPATH, "// div[ @ id = 'resultEmail']")
    assert email_registered.text == "Email: email@test.com", "Email not matching with user input"




