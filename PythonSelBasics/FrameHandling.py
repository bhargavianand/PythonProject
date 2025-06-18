import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://practice.expandtesting.com/iframe")
driver.maximize_window()

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "email-subscribe")))
#driver.switch_to.frame(driver.find_element(By.ID,"email-subscribe"))
driver.find_element(By.ID,"email").send_keys("email@email.com")
