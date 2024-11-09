from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service

# Chrome
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)

# implicit wait
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# using JS to scroll down the website to max
# if I want till certain point I have to provide (0,500)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#  to take the ss
driver.get_screenshot_as_file("screen1.png")