import pytest
from tests.config import TestData
import time
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver                              #loading driver for current class
        self.driver.get(TestData.baseUrl)                 #intializing browser
    
    def click_tabledata(self):
        print("Click table")
        table = (By.XPATH, "//summary[normalize-space()='Table Data']")
        self.clickOnElement(table)                          #method to click on a  web element

    def enterTableData(self):
        print("Enter Table")
        inputLocator = (By.ID, "jsondata")
        self.clickOnElement(inputLocator)
        with open('testdata.json', "r") as f:                 #getting data from json file in read mode
            inputData = f.read()
        self.enterInput(inputLocator, inputData)              #method to enter data in text input field
        return inputData
    
    def click_Refreshbutton(self):
        buttonLocator = (By.ID, "refreshtable")
        self.clickOnElement(buttonLocator)

    def get_tabledata(self):                                   
        table = self.driver.find_element(By.ID,"dynamictable")
        rows = table.find_elements(By.TAG_NAME, 'tr')        #getting all rows
        table_data = []
        header_row = rows[0]
        header_cells = header_row.find_elements(By.TAG_NAME, 'th')
        column_names = [cell.text for cell in header_cells]
        for row in rows[1:]:                                  #iterating over all row 
            cells = row.find_elements(By.TAG_NAME, 'td')      #getting all columns
            row_data = {}
            for index, cell in enumerate(cells):             #iterating over all columns
                if column_names[index] == "age":
                    row_data[column_names[index]] = int(cell.text)
                else:
                    row_data[column_names[index]] = cell.text
            table_data.append(row_data)
        table_json = json.dumps(table_data)
        return table_json