from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.execute_script("alert('Hello world!')")
driver.switch_to.alert.accept()