import time

from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

#dropdown selection for dynamic value using for loop
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        print(checkbox.is_selected())
        time.sleep(2)
        break
#radio button selection for static value.... use for loop for dynamic value
radioButton = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radioButton[2].click()
assert radioButton[2].is_selected()
time.sleep(2)

#isDisplayed() Method
assert driver.find_element(By.ID,"displayed-text").is_displayed()
print(driver.find_element(By.ID,"displayed-text").is_displayed())
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


