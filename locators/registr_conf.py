from selenium.webdriver.common.by import By
from locators.base_conf import Base




class BtnReg:
    def __init__(self, driver) -> None:
        self.regist = driver.find_element(By.ID, 'kc-register')



class Registration:
    def __init__(self, driver) -> None:
        self.name_first = driver.find_element(By.NAME, 'firstName')
        self.surname_last = driver.find_element(By.NAME, 'lastName')
        self.address = driver.find_element(By.ID, 'address')
        self.password = driver.find_element(By.ID, 'password')
        self.password_confirm = driver.find_element(By.ID, 'password-confirm')
        self.register_btn = driver.find_element(By.NAME, 'register')
        self.activation_notification = driver.find_element(By.CLASS_NAME, 'card-container__title')



