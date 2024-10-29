# import time

# from selenium import webdriver

# # Chrome Driver Service --> Selenium 160-->160 chrome driver
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice/")

# # ID, Xpath, CSSSelector, Classname, name, linkText

# driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
# driver.find_element(By.ID, "exampleCheck1").click()

# # Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# # CSS - tagname[attribute='value'] -> //input[@type='submit']
# driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")

# time.sleep(5)

from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")

driver.find_element_by_id("exampleCheck1").click()

#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message