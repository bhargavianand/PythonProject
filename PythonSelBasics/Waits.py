from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "genderMale")))
