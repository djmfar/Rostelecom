import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.registr_conf import Registration, BtnReg

from time import sleep
import configparser


@pytest.fixture
def open_page(driver, config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_auth"])


# 11 Регистрация с корректными данными
def test_registration_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["new_email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы перешли на страницу c надписью "Подтверждение email"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение email"
    sleep(1)

# 12 Регестрация с пустыми полями всех данных
def test_registration_empty_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Пропускаем все поля ввода
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации и вышло 5 подсказок о всех полях
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "Необходимо заполнить поле кириллицей")]')) == 2
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "Длина пароля должна быть не менее 8 символов")]')) == 2
    assert driver.find_element(By.XPATH, '//*[contains(text(), "email в формате example@email.ru")]')
    sleep(1)

# 13 Регестрация с пустыми полями Имени и Фамилии
def test_registration_empty_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект классs BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Пропускаем ввод Имени и Фамилии
    # Вводим почту
    reg.address.send_keys(config["auth"]["new_email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации и вышли 2 подсказки о формате полей
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "Необходимо заполнить поле кириллицей")]')) == 2
    sleep(1)

# 14 Регестрация с некорректной почтой
def test_registration_invalid_email(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["invalid_email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем что мы остались на странице Регистрации и вышла подсказка о формате почты
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "email в формате example@email.ru")]')
    sleep(1)

# 15 Регистрация с вводом цифр в поле Имя и Фамилия
def test_registration_numbers_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["phone1"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["phone1"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации и вышли 2 подсказки о кириллице
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "Необходимо заполнить поле кириллицей")]')) == 2
    sleep(1)


# 16 Регистрация с вводом 260 символов в поля Имя и Фамилия
def test_registration_260_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["email260"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["email260"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации и вышли 2 подсказки о размере полей
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "От 2 до 30 символов")]')) == 2
    sleep(1)


# 17 Регистрация с вводом спецсимволов в поля Имя и Фамилия
def test_registration_special_characters_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["symbols"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["symbols"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации и вышли 2 подсказки о формате
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert len(driver.find_elements(By.XPATH, '//*[contains(text(), "Необходимо заполнить поле кириллицей")]')) == 2
    sleep(1)


# Регестрация по телефону
# 18 Регистрация с корректными данными
def test_registration_valid_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["phone1"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(1)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем что мы перешли на страницу c надписью "Подтверждение телефона"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение телефона"
    sleep(1)
