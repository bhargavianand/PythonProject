from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
#driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
#driver.get("https://with-bugs.practicesoftwaretesting.com/#/contact")
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

#finding all the links from the page

links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links:", len(links))

for link in links:
    print("href value is " , link.get_attribute("href"))