from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://practice.expandtesting.com/js-dialogs")
driver.maximize_window()
driver.find_element(By.ID,"js-alert").click()

alert = Alert(driver)

#can also use

#alert = driver.switch_to.alert

print(alert.text)
alert.accept()