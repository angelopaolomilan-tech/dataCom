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

def test_first_name():
    field_first_name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[1]/label[1]")
    assert field_first_name.text == "First Name", "First name not field"

def test_last_name():
    field_last_name = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[2]/label[1]")
    assert field_last_name.text == "Last Name*", "Last name field is not visible"

def test_phone_number():
    field_phone_number = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[3]/label[1]")
    assert field_phone_number.text == "Phone Number*", "Phone number field is not visible"

def test_country():
    field_country = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[4]/label[1]")
    assert field_country.text == "Country", "Country field is not visible"

def test_email():
    field_email = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[5]/label[1]")
    assert field_email.text == "Email address*", "Email address field is not visible"

def test_password():
    field_password = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/div[6]/label[1]")
    assert field_password.text == "Password*", "Email address field is not visible"

#Validate required fields

def test_required_field_password_min_input():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("123456")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text != "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_password_max_input():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("12345678901234567890")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text != "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_password_below_min_input():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("12345")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text == "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_password_above_max_input():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("123456789012345678901")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text == "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_password_blank():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text == "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_password_spaces():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("      ")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    password_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert password_error_message.text == "The password should contain between [6,20] characters!", "Error message not displayed"

def test_required_field_Phone_number_blank():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    phone_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert phone_error_message.text == "The phone number should contain at least 10 numbers!", "Error message not displayed"

def test_required_field_Phone_number_spaces():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("           ")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    phone_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert phone_error_message.text == "The phone number should contain at least 10 numbers!", "Error message not displayed"

def test_required_field_Phone_number_characters():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("abcdefghijklmnop")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    phone_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert phone_error_message.text == "The phone number should contain at least 10 numbers!", "Error message not displayed"

def test_required_field_Phone_number_below_minimum():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("789123456")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    phone_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert phone_error_message.text == "The phone number should contain at least 10 numbers!", "Error message not displayed"

def test_required_field_Phone_number_minimum():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("1234567890")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    phone_error_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert phone_error_message.text != "The phone number should contain at least 10 numbers!", "Error message not displayed"
    assert phone_error_message.text != "Successfully registered the following information", "Message not displayed"

def test_required_last_name():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("1234567890")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    last_name_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert last_name_message.text == "The last name is a required field", "Error message not displayed"

def test_required_last_name():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("1234567890")
    last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
    last_name.clear()
    last_name.send_keys("O")
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    last_name_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert last_name_message.text != "The last name is a required field", "Error message not displayed"
    assert last_name_message.text == "Successfully registered the following information", "Message not displayed"

def test_required_email():
    password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
    password_locator.clear()
    password_locator.send_keys("password12345")
    phone_number_locator = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number_locator.clear()
    phone_number_locator.send_keys("1234567890")
    last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
    last_name.clear()
    last_name.send_keys("O")
    email = driver.find_element(By.XPATH, "//input[@id='emailAddress']")
    email.clear()
    register_button = driver.find_element(By.XPATH, "//button[@id='registerBtn']")
    register_button.click()
    email_message = driver.find_element(By.XPATH, "//div[@id='message']")
    assert email_message.text == "The email address is a required field", "Error message not displayed"
    assert email_message.text != "Successfully registered the following information", "Message not displayed"

# Validate checkbox for terms and conditions

def test_terms_and_conditions():
    terms_and_conditions = driver.find_element(By.XPATH, "//input[@id='exampleCheck1']")
    terms_and_conditions.click()
    assert terms_and_conditions.is_selected() == True





