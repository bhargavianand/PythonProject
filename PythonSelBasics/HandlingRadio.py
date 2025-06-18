import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)
action = ActionChains(driver)
gender_male = driver.find_element((By.ID,"genderMale"))
print("Clciking on gendermale radio button")
action.move_to_element(gender_male).click().perform()


'''
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"genderMale")))
    element.click()
except:
    print("Element is missing")
'''
#radio_buttons = driver.find_elements(By.CSS_SELECTOR,"[name='gender']")
#print("number of radio buttons is " , len(radio_buttons))
#driver.find_element(By.ID,"genderMale").click()

'''
#printing values of radiobuttons
for radio in radio_buttons:
    print(radio.get_attribute("value"))
    print(radio.is_enabled())

'''
