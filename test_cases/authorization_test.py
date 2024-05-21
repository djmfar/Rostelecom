import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.authorization_conf import AuthorizationPage
from time import sleep


@pytest.fixture
def open_page(driver, config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_auth"])

# ---------------------------------------------------
# Авторизация клиента на вкладке Телефон

# 0. Авторизация с корректными данными
# Этот тест нужен для того, чтобы ввести капчу и на следующих тестах капча не потребовалась
# Он пудет падать при вводе капчи. Как это исправить я не знаю и менторы мне не помогли
# Это "костыль" для других тестов во избежания в них капчи
# Следующий тест точно такой же и он не падает
def test_authorization_phone_valid_data_vvod_kapchi(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим телефон
    ap.username.send_keys(config.get("auth", "phone2"))
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(23)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    #driver.switch_to.window()
    # Проверяем, что мы перешли в личный кабинет с учетными данными и аватаркой пользователя
    wdw(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//img[@class="user-avatar"]')))
    assert driver.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"
    assert driver.find_element(By.XPATH, '//img[@class="user-avatar"]')
    sleep(3)

# 1. Авторизация с корректными данными
def test_authorization_phone_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим телефон
    ap.username.send_keys(config.get("auth", "phone2"))
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверяем, что мы перешли в личный кабинет с учетными данными и аватаркой пользователя
    wdw(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//img[@class="user-avatar"]')))
    assert driver.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"
    assert driver.find_element(By.XPATH, '//img[@class="user-avatar"]')
    sleep(3)

# 2. Авторизация с сиволами в поле Номер
def test_symbols_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    # Вводим телефон
    ap.username.send_keys(config["auth"]["invalid_data"])
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того, что мы остались на странице авторизации и выводится подсказка "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')
    #assert driver.find_element(By.XPATH, '//span[@id="form-error-message"]').text == "Неверный логин или пароль"
    sleep(3)


# 3. Авторизация с пустым полем номера телефона
def test_empty_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Пропускаем ввод поля номера телефона
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(2)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того, что мы остались на странице авторизации и видна подсказка: "Введите номер телефона"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//span[@id="username-meta"]').text == "Введите номер телефона"
    sleep(3)

# 4. Авторизация с пустым полем пароля на вкладке Телефон
# Баг - ничего не сообщается пользователю!
def test_empty_password_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим телефон
    ap.username.send_keys(config.get("auth", "phone2"))
    # Пропускаем ввод поля пароля
    # Время для ввода символов с картинки
    sleep(2)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того, что мы остались на странице авторизации и видна подсказка "Введите пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//span[@id="username-meta"]').text == "Введите пароль"
    sleep(3)

# ---------------------------------------------------
# Авторизация клиента по вкладке "Почта"
# 5. Авторизация с корректными данными
def test_authorization_mail_valid_data(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверяем, что мы перешли в личный кабинет с учетными данными и аватаркой пользователя
    wdw(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//img[@class="user-avatar"]')))
    assert driver.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"
    assert driver.find_element(By.XPATH, '//img[@class="user-avatar"]')
    sleep(3)

# 6. Авторизация с некорректным паролем
def test_authorization_mail_invalid_data(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Вводим невалидный password в поле password
    ap.password.send_keys(config["auth"]["invalid_data"])
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации и выводится подсказка "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')
    #wdw(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')))
    #assert driver.find_element(By.XPATH, '//span[@data-error="Неверный логин или пароль"]')
    sleep(3)

# 7. Авторизация с пустым полем ввода email
def test_empty_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Пропускаем ввод email
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации и выводится подсказка "Введите адрес, указанный при регистрации"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Введите адрес, указанный при регистрации")]')
    sleep(3)


# 8. Авторизация с пустым полем Пароля
# Баг - ничего не сообщается пользователю!
def test_empty_password(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Пропускаем ввод поля пароль
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации и выводится подсказка "Введите пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Введите пароль")]')
    #assert driver.find_element(By.XPATH, '//span[@id="username-meta"]').text() == "Введите пароль"
    sleep(3)


# 9. Авторизация с 260 символами в полем Почта
def test_260_symbols_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email260"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации и выводится подсказка "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')
    #assert driver.find_element(By.XPATH, '//span[@id="form-error-message"]').text == "Неверный логин или пароль"
    sleep(3)

# 10. Авторизация с спецсимволами в полем Почта
def test_special_characters_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["symbols"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    sleep(3)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации и выводится подсказка "Неверный логин или пароль"
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Неверный логин или пароль")]')
    #assert driver.find_element(By.XPATH, '//span[@id="form-error-message"]').text == "Неверный логин или пароль"
    sleep(3)
