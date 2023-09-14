from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Provide the path to your Chrome WebDriver
webdriver_path = "path/to/chromedriver"

# Provide the target phone number (include country code, without '+' or '0')
phone_number = "+916297079012"

# Start the webdriver
driver = webdriver.Chrome(service=Service(webdriver_path))
driver.get("https://web.whatsapp.com/")

# Wait for the page to load
time.sleep(5)

# Find the search input field and enter the target phone number
search_box = driver.find_element(By.CSS_SELECTOR, "div._2FVVk > div._2_1wd")
search_box.click()
search_box.send_keys(phone_number)

# Wait for the contact to load and click on it
time.sleep(2)
contact = driver.find_element(By.CSS_SELECTOR, "div._3ko75 > div._19RFN")
contact.click()

# Find the message input field and type your message
message_box = driver.find_element(By.CSS_SELECTOR, "div._2FVVk > div._13mgZ")
message_box.click()
message_box.send_keys("Hello, this is a WhatsApp message sent using Python!")

# Send the message by pressing the 'Enter' key
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

# Wait for a few seconds and then close the browser
time.sleep(2)
driver.quit()
