from selenium.webdriver.common.by import By
from locators.base_conf import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw

class Recovery:
    def __init__(self, driver) -> None:
        self.continue_btn = driver.find_element(By.ID, 'reset')
        self.phone_btn = driver.find_element(By.ID, 't-btn-tab-phone')
        self.username = driver.find_element(By.ID, 'username')
        self.email_btn = driver.find_element(By.ID, 't-btn-tab-mail')


