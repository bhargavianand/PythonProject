import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.way2automation.com/angularjs-protractor/banking/registrationform.html")
driver.maximize_window()
submit = driver.find_element(By.XPATH,"//button[text()='Register']")
submit.click()
time.sleep(3)
error_message = driver.find_element(By.ID,"errorMessage").text
assert "All fields must be filled" in error_message
#assert "success" in error_message
