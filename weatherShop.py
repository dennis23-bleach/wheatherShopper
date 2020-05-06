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


driver.get('https://weathershopper.pythonanywhere.com')

temp = driver.find_element_by_xpath("//span[@id='temperature']")

#spliting the value to get only the numbers desired
current_temp = temp.text.split()[0]
print(current_temp)

time.sleep(5)



#temp comparison
if int(current_temp) < 19:
    driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    if driver.title == "The Best Moisturizers in the World!":
        print('Passed : In the moisturizers page')
    else:
        print('Failed : could not get into the moisturizers page')
    time.sleep(10)
elif int(current_temp) > 34:
    driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    if driver.title == "The Best Sunscreens in the World!":
        print('Passed : In the Sunscreens page')
    else:
        print('Failed : could not get into the sunscreen page')
    time.sleep(10)
else:
    print('Failed : Temperature not in range')


#close the browser
driver.close()
