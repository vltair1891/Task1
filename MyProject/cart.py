from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import re

def AddToCart(driver, element):
    """
    Add item to cart function
    driver:
    type: chrome iwebdriver
    element:
    type: iwebelement
    """
    WebDriverWait(driver, 5)
    element.click()
    WebDriverWait(driver, 5)
    try:
        driver.find_element_by_id("isCartBtn_btn").click()
        print("Item was Added to cart")
    except NoSuchElementException:
        driver.find_element_by_id('smtBackToAnchor').click
    WebDriverWait(driver, 4)
    driver.find_element_by_id("contShoppingBtn").click()

def CheckCart(driver):
    """
    Check total acoount in cart function
    driver:
    type: chrome iwebdriver
    """
    WebDriverWait(driver, 5)
    driver.find_element_by_id('gh-cart-i').click()
    WebDriverWait(driver, 5)
    element = driver.find_element_by_xpath('//div[2][@id="syncTotal"]/span[2]')
    total = re.sub("[^0-9]", "", element.text)
    total = float(total)
    result = total/100
    WebDriverWait(driver, 4)
    try:
        driver.find_element_by_id('contShoppingBtn').click()
    except NoSuchElementException:
        driver.back()
        driver.back()
    return result