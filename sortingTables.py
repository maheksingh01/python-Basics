from selenium import webdriver

# Chrome
from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver = webdriver.Chrome()

driver.get("https//rahulshettyacademy.com/seleniumPractice/#/offers/")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedVeggieList (A, B, C)
veggieWebElemets = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElemets:
    browserSortedVeggies.append(ele.text)
    
originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this BrowserSortedList => newSortedList -> (A, B, C)
browserSortedVeggies.sort()

# assert BrowserSortedList == newSortedList

assert browserSortedVeggies == originalBrowserSortedList