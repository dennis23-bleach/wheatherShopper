"""
1. navigating to the url
2. finding the xpath for the text
3. compare the text and based on the results find the corresponding xpaths and click
4. close the browser
"""


from selenium import webdriver
import time

#initialising geckodriver
driver = webdriver.Firefox()


driver.get('https://weathershopper.pythonanywhere.com/moisturizer')
time.sleep(5)

add_to_cart = driver.find_elements_by_xpath("//button[contains(@class,'btn btn-primary')]")
total_no_of_items = len(add_to_cart)

for item in add_to_cart:
    item.click()

cart = driver.find_element_by_xpath("//button[@class='thin-text nav-link']")
cart.click()


no_of_items = len(driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody//tr"))

if no_of_items == total_no_of_items:
    print("Success: all items have been added")
else:
    print("Failed")

time.sleep(5)

driver.close()
