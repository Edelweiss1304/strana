from pages.header_links import Header
from base.base_class import Base
from utilities.Conftest import driver

#MSK
def test_msk_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    driver.save_screenshot('screen/failure_screenshot.png')
    head.check_projects()

def test_msk_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_apart()

def test_msk_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_commercial()

def test_msk_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_actions()

def test_msk_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_about()

def test_msk_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_purchase_methods()

def test_msk_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_msk)
    head.check_vacancies()

#MO

def test_mo_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_mo)
    head.check_commercial()

def test_mo_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_mo)
    head.check_actions()

#def test_mo_header_purchase_methods(driver):   ###404 ошибка###
    #head = Header(driver)
   # Base.open_page(driver, Base.url_mo)
   # head.check_purchase_methods()

def test_mo_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_mo)
    head.check_about()

def test_mo_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_mo)
    head.check_vacancies()

    #SPB

def test_spb_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_projects()

def test_spb_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_apart()

def test_spb_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_commercial()

def test_spb_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_actions()

def test_spb_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_about()

def test_spb_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_purchase_methods()

def test_spb_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_spb)
    head.check_vacancies()

    #EKB

def test_ekb_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_projects()

def test_ekb_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_apart()

def test_ekb_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_commercial()

def test_ekb_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_actions()

def test_ekb_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_about()

def test_ekb_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_purchase_methods()

def test_ekb_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_ekb)
    head.check_vacancies()

    #TMN

def test_tmn_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_projects()

def test_tmn_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_apart()

def test_tmn_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_commercial()

def test_tmn_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_actions()

def test_tmn_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_about()

def test_tmn_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_purchase_methods()

def test_tmn_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_tmn)
    head.check_vacancies()

    #NSK

def test_nsk_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_nsk)
    head.check_about()

def test_nsk_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, Base.url_nsk)
    head.check_vacancies()