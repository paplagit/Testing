import pytest


import time

@pytest.fixture(params=["edge"], scope="class") # scope = class,
# because we want the conftest to run only once for each class, not for each method
def init_driver(request):
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service
    from tests.config import TestData
    if request.param == "edge":
        service_obj = Service(TestData.chromePath)
        web_driver = webdriver.Edge(service=service_obj)
        web_driver.maximize_window()
    request.cls.driver = web_driver # the driver declared here will be sent to the class object(test_sample1.py)
    yield
    time.sleep(3)
    web_driver.close() #tear down method
