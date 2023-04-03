from settings import *
import pytest
from time import sleep


# AT0001 Открывается страница с формой "Авторизация"
def test_authorization_is_exists(browser, auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# AT0002 Пункт меню "Почта" кликабелен и открывает форму авторизации по почте и паролю
def test_mail_is_clickable(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# AT0003, AT0004
# Базовая позитивная проверка авторизации по валидным телефону/почте и паролю.
# По умолчанию при открытии страницы открыта форма авторизации по телефону -- таб "Телефон"
# При вводе почты таб "Телефон" переключается на таб "Почта"
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_valid_data(browser, auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# AT0005, AT0006
# Негативный тест авторизации по валидным телефону/почте и невалидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_fake_password(browser, auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# AT0007 Негативный тест авторизации по пустому полю ввода телефона и валидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_phone(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# AT0008 Негативный тест авторизации по пустому полю ввода почты и валидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_mail(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# AT0009 Негативный тест авторизации по пустому полю ввода логина и валидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_login(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# AT0010 Негативный тест авторизации по пустому полю ввода лицевого счета и валидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_ls(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG


# AT0011 Ссылка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_password(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# AT0012 Ссылка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_register(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# AT0013 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Почта"
@pytest.mark.positive
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_mail(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# AT0014 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Логин"
@pytest.mark.positive
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_login(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# AT0015 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Лицевой счет"
@pytest.mark.positive
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_ls(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert active_tab_name == 'Телефон'
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)












