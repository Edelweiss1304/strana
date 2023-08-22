from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import testit
import time


@testit.displayName("Проверка авторизации в ЛК {url}")
@testit.description("Проверка авторизации в ЛК через кнопку входа рядом с избранным")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_client(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1)
    with testit.step("Нажимаем иконку входа"):
        auth.click_login_lk_button()
    with testit.step("Заполняем телефон"):
        time.sleep(2)
        auth.get_login_client_phone_field().send_keys(+79198629250)
    with testit.step("Кликаем Получить код"):
        auth.click_get_code_btn()
    with testit.step("Вводим код"):
        auth.get_enter_code_field().send_keys(1313)
    with testit.step("Нажимаем Войти"):
        auth.click_fin_login_btn()
    with testit.step("Проверяем, что вошли в ЛК"):
        assert auth.get_check_lk() == "Брони и договоры"
        print('Успешный вход в ЛК')
