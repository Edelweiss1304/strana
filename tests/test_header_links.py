from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import pytest



#MSK
@allure.title("Проверка кнопки проекты мск")
def test_msk_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_projects()
    
@allure.title("Проверка кнопки квартиры мск")
def test_msk_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart()

@allure.title("Проверка кнопки коммерции мск")
def test_msk_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_commercial()

@allure.title("Проверка кнопки акции мск")
def test_msk_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_actions()

@allure.title("Проверка кнопки о нас мск")
def test_msk_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_about()

@allure.title("Проверка кнопки способы покупки мск")
def test_msk_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_purchase_methods()

@allure.title("Проверка кнопки вакансии мск")
def test_msk_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_vacancies()

#MO
@allure.title("Проверка кнопки коммерции мо")
def test_mo_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_mo'])
    head.check_commercial()

@allure.title("Проверка кнопки акции мо")
def test_mo_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_mo'])
    head.check_actions()

#def test_mo_header_purchase_methods(driver):   ###404 ошибка###
    #head = Header(driver)
   # Base.open_page(driver, Base.url_mo)
   # head.check_purchase_methods()

@allure.title("Проверка кнопки о нас мо")
def test_mo_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_mo'])
    head.check_about()

@allure.title("Проверка кнопки вакансии мо")
def test_mo_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_mo'])
    head.check_vacancies()

    #SPB
@allure.title("Проверка кнопки проекты спб")
def test_spb_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_projects()

@allure.title("Проверка кнопки квартиры спб")
def test_spb_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_apart()

@allure.title("Проверка кнопки коммерции спб")
def test_spb_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_commercial()

@allure.title("Проверка кнопки акции спб")
def test_spb_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_actions()

@allure.title("Проверка кнопки о нас спб")
def test_spb_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_about()

@allure.title("Проверка кнопки методы покупки спб")
def test_spb_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_purchase_methods()

@allure.title("Проверка кнопки вакансии спб")
def test_spb_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_vacancies()

    #EKB
@allure.title("Проверка кнопки проекты екб")
def test_ekb_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_projects()

@allure.title("Проверка кнопки квартиры екб")
def test_ekb_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_apart()

@allure.title("Проверка кнопки коммерция екб")
def test_ekb_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_commercial()

@allure.title("Проверка кнопки акции екб")
def test_ekb_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_actions()

@allure.title("Проверка кнопки о нас екб")
def test_ekb_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_about()

@allure.title("Проверка кнопки методы покупки екб")
def test_ekb_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_purchase_methods()

@allure.title("Проверка кнопки вакансии екб")
def test_ekb_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_vacancies()

    #TMN
@allure.title("Проверка кнопки вакансии тмн")
def test_tmn_header_projects(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_projects()

@allure.title("Проверка кнопки квартиры тмн")
def test_tmn_header_apart(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_apart()

@allure.title("Проверка кнопки коммерция тмн")
def test_tmn_header_commercial(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_commercial()

@allure.title("Проверка кнопки акции тмн")
def test_tmn_header_actions(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_actions()

@allure.title("Проверка кнопки о нас тмн")
def test_tmn_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_about()

@allure.title("Проверка кнопки методы покупки тмн")
def test_tmn_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_purchase_methods()

@allure.title("Проверка кнопки вакансии тмн")
def test_tmn_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_vacancies()

    #NSK

@allure.title("Проверка кнопки о нас тмн")
def test_nsk_header_about(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_nsk'])
    head.check_about()

@allure.title("Проверка кнопки вакансии тмн")
def test_nsk_header_vacancies(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_nsk'])
    head.check_vacancies()