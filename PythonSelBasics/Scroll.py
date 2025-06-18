import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 1200)")

