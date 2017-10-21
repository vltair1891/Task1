from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def SearchFor(driver, search):
    """
    Scpecific search function
    driver:
    type: chrome iwebdriver
    search:
    type: string
    """
    driver.find_element_by_xpath("//div[@id='gh-ac-box2']/input").send_keys(Keys.CONTROL + 'a')
    driver.find_element_by_xpath("//div[@id='gh-ac-box2']/input").send_keys(search)
    WebDriverWait(driver, 4)
    driver.find_element_by_id("gh-btn").click()