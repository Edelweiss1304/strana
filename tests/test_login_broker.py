from pages.authorization import Authorization
from utilities.Conftest import driver
from base.base_class import Base


def test_authorization_agent_tmn(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_tmn)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agent_msk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_msk)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agent_spb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_spb)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agent_ekb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_ekb)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agent_mo(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_mo)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agent_nsk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_nsk)
    auth.login_lk_broker_agent()
    auth.check_broker_agent()


def test_authorization_agency_tmn(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_tmn)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()


def test_authorization_agency_msk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_msk)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()


def test_authorization_agency_ekb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_ekb)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()


def test_authorization_agency_nsk(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_nsk)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()


def test_authorization_agency_mo(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_tmn)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()


def test_authorization_agency_spb(driver):
    auth = Authorization(driver)
    Base.open_page(driver, Base.url_spb)
    auth.login_lk_broker_agency()
    auth.check_broker_agent()
