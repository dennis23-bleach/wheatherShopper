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
item_names = []
item_price = []


def cart_checkout(items, price):
    " checks whether the correct item has been entered into the cart "
    num = 1
    split_price = []
    for item in items:
        xpath_cart_items = ('//body//tbody//tr[{}]').format(num)
        text_cart = browser.find_element_by_xpath(xpath_cart_items).text
        split_item_price = text_cart.split()[-1]
        split_price.append(int(split_item_price))
        num += 1
        if item in text_cart:
            print(item+'is present in the cart')
        else:
            print(item+"is not present")

    item_price = sum(price)
    if item_price == sum(split_price):
        print("prices are matching")


def get_all_product(each_condition, all_products):
    "get the product name and price"
    min_price = 10000
    for each_product in all_products:
        each_product_text = each_product.text
        product_name = each_product_text.splitlines()[0]
        if each_condition in product_name.lower():
            get_product_price = each_product_text.splitlines()[1]
            get_product_price = int(get_product_price.split(" ")[-1])
            #get_product_price = get_product_price.split("Rs.")
            if min_price >= get_product_price:
                min_price = get_product_price
                min_prodcut_name = product_name
    item_names.append(min_prodcut_name)
    item_price.append(min_price)
    browser.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_prodcut_name)).click()


#Find the xpath for all the products 
all_products = browser.find_elements_by_xpath("//div[contains(@class,'col-4')]")
for each_condition in all_condition:
    get_all_product(each_condition,all_products)

browser.find_element_by_xpath("//button[@class='thin-text nav-link']").click()

cart_checkout(item_names, item_price)

payment = browser.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()

iframe_xpath = browser.find_element_by_xpath("//iframe[@name = 'stripe_checkout_app']")
browser.switch_to_frame(iframe_xpath)


xpath_email = '//input[@placeholder="Email"]'
payment_email = browser.find_element_by_xpath(xpath_email).send_keys('dennis.23bleach@gmail.com')

xpath_card_no = '//input[@placeholder = "Card number"]'
payment_card_no = browser.find_element_by_xpath(xpath_card_no).send_keys('4242424242424242')

xpath_date = '//input[@placeholder="MM / YY"]'
payment_date = browser.find_element_by_xpath(xpath_date).send_keys('052020')

xpath_cvc = '//input[@placeholder="CVC"]'
payment_cvc = browser.find_element_by_xpath(xpath_cvc).send_keys('0123')

xpath_zip = '//input[@placeholder="ZIP Code"]'
payment_zip = browser.find_element_by_xpath(xpath_zip).send_keys('560037')

xpath_pay = '//button[@type="submit"]'
payment_pay = browser.find_element_by_xpath(xpath_pay).click()


time.sleep(10)

browser.close()
