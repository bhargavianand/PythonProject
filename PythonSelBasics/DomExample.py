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
print(driver.title)
drop_down = driver.find_element(By.CSS_SELECTOR,"#searchLanguage")
select = Select(drop_down)
#select.select_by_visible_text("Eesti")
select.select_by_value("hi")
#total count of items in the dropdown list

items =driver.find_elements(By.XPATH,"//select[@id='searchLanguage']/option")

for item in items:
    print("Option Text is " , item.text , "Lang is: " +item.get_attribute("lang"))

print("Total dropdown values are : " , len(items))


'''
driver.find_element(By.ID,"first_name").send_keys("John")
driver.find_element(By.ID,"last_name").send_keys("Doe")
driver.find_element(By.ID,"email").send_keys("JohnDoe@xyz.com")
driver.find_element(By.ID,"subject").send_keys("webmaster")

#driver.find_element(By.CSS_SELECTOR,".btnSubmit").click()

assert "Registration" in driver.title

'''


#assert in title




'''elements = driver.find_elements(By.CLASS_NAME,"fields12")
print(len(elements))
if(len(elements)>0):
    for element in elements:
        print(element.text)
else:
    print("No elements found")

'''
