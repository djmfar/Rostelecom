import pytest
from selenium import webdriver
import configparser

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture(autouse=True)
def config():
    # with open("./config.ini", "r") as f:
    #     x = f.read()
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf8")
    yield config




