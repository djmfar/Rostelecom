from selenium.webdriver.common.by import By
from locators.base_conf import Base


class AuthorizationPage(Base):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.email_btn = driver.find_element(By.ID, 't-btn-tab-mail')
        self.login_btn = driver.find_element(By.ID, 'kc-login')
        self.phone_btn = driver.find_element(By.ID, 't-btn-tab-phone')





