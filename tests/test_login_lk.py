from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import allure


@pytest.mark.parametrize("url", URLS_MAIN.values())
@pytest.mark.allure_feature("Проверка авторизации в ЛК клиента")
@allure.title("Проверка авторизации в ЛК клиента")
def test_authorization_client(driver, url):
    auth = Authorization(driver)
    Base.open_page(driver, url)
    auth.login_lk()
    assert auth.get_check_lk() == "Брони и договоры"
    print('Успешный вход в ЛК')
