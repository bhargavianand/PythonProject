import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 1200)")
time.sleep(3)


chooseFile_button = driver.find_element(By.ID,"profilePic")
print(driver.find_element(By.ID,"profilePic").is_enabled())

#create an action chain object
action = ActionChains(driver)

action.move_to_element(chooseFile_button).click().perform()