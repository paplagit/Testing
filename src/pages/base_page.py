import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def clickOnElement(self, locator):            # method to click on any web element
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()

    def enterInput(self, locator, data):         #method to enter data into input field
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).clear()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(data)
        