# this file contains a class which is a parent of all the test classes
# this file actually invoke setup and to be used by all the test classes

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from tests.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseClass:
    pass
