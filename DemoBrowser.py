import time

from selenium import webdriver

# Chrome Driver Service --> Selenium 160-->160 chrome driver
driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)