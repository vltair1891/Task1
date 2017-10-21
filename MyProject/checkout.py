from selenium.webdriver.support.ui import WebDriverWait

def FillTheFormAsAGuest(driver):
    """
    Fill the checkout as a guest function
    driver:
    type: chrome iwebdriver
    """
    WebDriverWait(driver, 5)
    driver.find_element_by_id('gh-cart-i').click()
    WebDriverWait(driver, 4)
    driver.find_element_by_id('ptcBtnRight').click()
    WebDriverWait(driver, 4)
    driver.find_element_by_id('gtChk').click()
    driver.find_element_by_id('af-first-name').send_keys('Vadim')
    driver.find_element_by_id('af-last-name').send_keys('Aliev')
    driver.find_element_by_id('af-address1').send_keys('Sahlave 6/16')
    driver.find_element_by_id('af-city').send_keys('Lod')
    driver.find_element_by_id('af-state').send_keys('Merkaz')
    driver.find_element_by_id('af-zip').send_keys('7147512')
    driver.find_element_by_id('af-email').send_keys('valtair1891@gmail.com')
    driver.find_element_by_id('af-email-confirm').send_keys('valtair1891@gmail.com')
    driver.find_element_by_xpath('//input[@class="input-field ipt-phone"]').send_keys('0541111111')
    driver.find_element_by_xpath('//button[@data-click-id=7310]').click()