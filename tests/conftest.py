import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(params=["chrome"], scope="class") # scope = class,
# because we want the conftest to run only once for each class, not for each method
def init_driver(request):
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service
    from tests.config import TestData
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        service_obj = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service_obj, options=options)
        web_driver.maximize_window()
    request.cls.driver = web_driver # the driver declared here will be sent to the class object(test_sample1.py)
    yield
    time.sleep(3)
    web_driver.close() #tear down method
