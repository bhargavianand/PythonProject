from operator import truediv

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
#driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
#driver.get("https://with-bugs.practicesoftwaretesting.com/#/contact")
driver.get("https://www.wikipedia.org/")
#driver.implicitly_wait(10)
driver.maximize_window()
print("Without using method is_displayed() : ")
print(driver.find_element(By.CSS_SELECTOR,"#searchInput").is_displayed())

def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False
print("using custom method is_element_present() :findElement ")
print(is_element_present(By.CSS_SELECTOR,"#searchInput"))


def is_element_present_findElements(how, what):
        if(len(driver.find_elements(by = how, value = what )) == 0):
            return False
        else:
            return True
print("using custom method is_element_present() :findElements ")
print(is_element_present_findElements(By.XPATH,"//select[@id='searchLanguage']/option"))



