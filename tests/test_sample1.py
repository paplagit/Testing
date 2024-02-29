import pytest
from tests.test_base import BaseClass
import time
from src.pages.home_page import HomePage
import json
class Test_OpenPage(BaseClass):
    
    def test_PopulateDataIntoTable(self):
        home = HomePage(self.driver)
        home.click_tabledata()                                   #step to click table data button
        
        testDataJson = home.enterTableData()                     #step to input testdata into text field
        home.click_Refreshbutton()                               #step to click refresh button to load data into table
        tableDataInjson = home.get_tabledata()                   #Getting table data
        dict1 = json.loads(testDataJson)
        dict2 = json.loads(tableDataInjson)
        assert dict1 == dict2, "JSON objects are not equal"       #Asserting testdata with data in table
        

