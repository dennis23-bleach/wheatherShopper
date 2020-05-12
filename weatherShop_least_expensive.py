"""
1. Goto /moisturizers page
2. Add the least expensive aloe and least expensive almond
3. To the cart
"""
from selenium import webdriver
import time

#Create the instance of the webdreiver
browser = webdriver.Firefox()

#Navigate the URL
browser.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(5)

#Condidtion to add moisturizer
all_condition = ['aloe','almond']

def get_all_product(each_condition,all_products):
    "get the product name and price"
    min_price = 10000
    for each_product in all_products:
        each_product_text = each_product.text
        product_name = each_product_text.splitlines()[0]
        if each_condition in product_name.lower():
            print(each_product_text.lower())
            get_product_price = each_product_text.splitlines()[1]
            get_product_price = int(get_product_price.split(" ")[-1])
            #get_product_price = get_product_price.split("Rs.")
            print(get_product_price,type(get_product_price))
            if min_price >= get_product_price:
                min_price = get_product_price
                min_prodcut_name = product_name
    print("aloe",min_prodcut_name,min_price)

    browser.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_prodcut_name)).click()



#Find the xpath for all the products 
all_products = browser.find_elements_by_xpath("//div[contains(@class,'col-4')]")
for each_condition in all_condition:
    get_all_product(each_condition,all_products)

browser.close()
