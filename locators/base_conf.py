from selenium.webdriver.common.by import By


class Base:
    def __init__(self, driver) -> None:
        self.username = driver.find_element(By.ID, 'username')
        self.password = driver.find_element(By.ID, 'password')
        self.email_btn = driver.find_element(By.ID, 't-btn-tab-mail')
        self.login_btn = driver.find_element(By.ID, 'kc-login')
        self.phone_btn = driver.find_element(By.ID, 't-btn-tab-phone')

