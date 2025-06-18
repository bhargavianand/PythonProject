from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
#driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
#driver.get("https://with-bugs.practicesoftwaretesting.com/#/contact")
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

drop_down = driver.find_element(By.CSS_SELECTOR,"#searchLanguage")
select = Select(drop_down)
#select.select_by_visible_text("Eesti")
#select.select_by_value("hi")
#total count of items in the dropdown list

items =drop_down.find_elements(By.XPATH,"//select[@id='searchLanguage']/option")
print("Total dropdown values are : " , len(items))

print("First Item is " , drop_down.find_elements(By.TAG_NAME,"option").__getitem__(0).text)

'''
for item in items:
    print("Option Text is " , item.text , "Lang is: " +item.get_attribute("lang"))

print("Total dropdown values are : " , len(items))
'''