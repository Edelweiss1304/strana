from pages.authorization import Authorization
from utilities.Conftest import driver
from base.base_class import Base


def test_authorization_client_tmn(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_tmn)
    auth.login_lk()
    auth.check_lk_authorization()


def test_authorization_client_msk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_msk)
    auth.login_lk()
    auth.check_lk_authorization()


def test_authorization_client_spb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_spb)
    auth.login_lk()
    auth.check_lk_authorization()


def test_authorization_client_ekb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_ekb)
    auth.login_lk()
    auth.check_lk_authorization()


def test_authorization_client_mo(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_mo)
    auth.login_lk()
    auth.check_lk_authorization()


def test_authorization_client_nsk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_nsk)
    auth.login_lk()
    auth.check_lk_authorization()
