from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import allure
import testit


@testit.displayName("Проверка авторизации в ЛК")
@testit.description("Проверка авторизации в ЛК через кнопку входа рядом с избранным")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка авторизации в ЛК клиента")
def test_authorization_client(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        auth.login_lk()
    with testit.step("Проверяем, что вошли в ЛК"):
        assert auth.get_check_lk() == "Брони и договоры"
        print('Успешный вход в ЛК')
