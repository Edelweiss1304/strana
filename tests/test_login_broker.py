from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import allure
from pages.header_links import Header
import time


@pytest.mark.parametrize("url", URLS_MAIN.values())
@pytest.mark.allure_feature("Проверка авторизации в ЛК брокера через хедер")
@allure.title("Проверка авторизации в ЛК брокера через хедер")
def test_authorization_agent_from_header(driver, url):
    auth = Authorization(driver)
    Base.open_page(driver, url)
    auth.login_page_broker_from_header(url)
    auth.login_lk_broker()
    assert auth.get_broker_agent_check().text == "Сделки"
    print('Успешный вход в ЛК брокера, как агент')


@pytest.mark.parametrize("url", URLS_MAIN.values())
@pytest.mark.allure_feature("Проверка авторизации в ЛК брокера через главную страницу")
@allure.title("Проверка авторизации в ЛК брокера через главную страницу")
def test_authorization_agent_from_main_page(driver, url):
    auth = Authorization(driver)
    Base.open_page(driver, url)
    time.sleep(1)
    auth.login_broker_from_main_page(url)
    auth.login_lk_broker()
    assert auth.get_broker_agent_check().text == "Сделки"
    print('Успешный вход в ЛК брокера')
