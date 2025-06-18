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
#driver.execute_script("window.scrollTo(0, 1200)")
time.sleep(3)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print("number of checkboxes is " , len(checkboxes))
for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    checkbox.click()

'''
print(checkboxes[0].is_displayed())
print(checkboxes[0].get_attribute("value"))
print(checkboxes[0].is_enabled())
checkboxes[0].click()
print(checkboxes[1].is_displayed())
print(checkboxes[1].get_attribute("value"))
print(checkboxes[1].is_enabled())
checkboxes[1].click()

'''
'''
def verify_checkbox_selected(checkbox):
    if checkbox.is_selected():
        return True
    else:
        return False
'''

'''
for checkbox in checkboxes:
    print("Checkbox value is " ,checkbox.get_attribute("value"))
    checkbox.click()
'''

'''
for i in range(len(checkboxes)):
    print(i)
    checkboxes[i].click()
'''
'''
  if(verify_checkbox_selected(checkbox)):
        print("The checkbox is selected")
    else:
        print("The checkbox is not selected")


'''

