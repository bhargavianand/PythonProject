from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://practice.expandtesting.com/windows")
driver.maximize_window()
parentwindow = driver.window_handles
print(parentwindow)
driver.execute_script("window.scrollTo(0, 1200)")
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()

handles = driver.window_handles

for handle in handles:
    if handle != parentwindow:
        driver.switch_to.window(handle)
        print(driver.title)

