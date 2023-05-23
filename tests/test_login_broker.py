from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest


@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_agent_tmn(driver, url):
    auth = Authorization(driver)
    Base.open_page(driver, url)
    auth.login_lk_broker_agent()
    assert auth.get_broker_agent_check().text == "Клиенты"
    print('Успешный вход в ЛК брокера, как агент')


@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_agency_tmn(driver, url):
    auth = Authorization(driver)
    Base.open_page(driver, url)
    auth.login_lk_broker_agency()
    assert auth.get_broker_agent_check().text == "Клиенты"
    print('Успешный вход в ЛК брокера')
