from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from MyProject import search
from MyProject import cart
from MyProject import checkout

driver = webdriver.Chrome("C:\\Users\\אולגה\\Selenium\\chromedriver.exe")
url = "https://www.ebay.com/"
driver.get(url)
driver.maximize_window()
search.SearchFor(driver, "lego")
elements = driver.find_elements_by_xpath("//w-root/div/div/ul/li")
L = [element.get_attribute('id') for element in elements]
for id in L:
    try:
        el = driver.find_element_by_id(id)
    except NoSuchElementException:
        driver.find_element_by_id('smtBackToAnchor').click
    cart.AddToCart(driver, el.find_element_by_xpath('.//div/div/a'))
    if cart.CheckCart(driver) >= 500:
        print ("Checkout")
        checkout.FillTheFormAsAGuest(driver)
        WebDriverWait(driver, 600)
        driver.close()
        break
