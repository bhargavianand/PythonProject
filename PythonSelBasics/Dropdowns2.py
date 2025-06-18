import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
#driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
driver.get("https://www.way2automation.com/angularjs-protractor/banking/registrationform.html")
driver.maximize_window()

dropdown = driver.find_element(By.ID,"gender");
select = Select(dropdown)
items = dropdown.find_elements(By.TAG_NAME,"option")
for item in items:
    print("selecting the item: ",item.text)
    select.select_by_visible_text(item.text)

