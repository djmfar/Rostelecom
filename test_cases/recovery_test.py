import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.recovery_conf import Recovery
from time import sleep



@pytest.fixture
def open_page(driver, config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_activation"])



# 19 Восстановление пароля с корректными данными
def test_recovery_phone_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку телефон
    rec.phone_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["phone2"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы перешли на страницу активации, где нужно выбрать метод активации
    assert driver.find_elements(By.XPATH, '//*[contains(text(), "Восстановление пароля")]')
    assert driver.find_elements(By.XPATH, '//*[contains(text(), "По номеру телефона")]')
    sleep(3)



# 20 Восстановление пароля с несуществующим номером телефона
def test_recovery_phone_invalid_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку телефон
    rec.phone_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["invalid_phone"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы остались на той же странице и вышла подсказка "Неверный формат телефона"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление пароля")
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный формат телефона")]')
    sleep(2)


# Восстановление пароля с помощью Почты
# 21 Восстановление пароля с корректными данными
def test_recovery_mail_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку Почта
    rec.email_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["email"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы перешли на страницу активации, где нужно выбрать метод активации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление пароля")
    assert driver.find_elements(By.XPATH, '//*[contains(text(), "По e-mail")]')
    sleep(2)

# 22 Восстановление пароля с незарегестрированной почтой
def test_recovery_mail_new_email(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку Почта
    rec.email_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["new_email"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы остались на той же странице и вышла подсказка "Неверный логин или текст с картинки"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление пароля")
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный логин или текст с картинки")]')
    sleep(2)