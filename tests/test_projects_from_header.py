from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import selenium


@allure.title("Проверка WOW мск")
def test_msk_header_wow(driver):
    head = Header(driver)
    print(selenium.__file__)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_wow_from_header()


@allure.title("Проверка Озёрный мск")
def test_msk_header_ozerniy(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_ozerniy_from_header()


@allure.title("Проверка ДнВ спб")
def test_spb_header_dnv(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_dnv_from_header()


@allure.title("Проверка Принцип спб")
def test_spb_header_princip(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.check_princip_from_header()


@allure.title("Проверка Звездный тмн")
def test_tmn_header_zvezdniy(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_zvezdniy_from_header()


@allure.title("Проверка Юнион тмн")
def test_tmn_header_union(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_union_from_header()


@allure.title("Проверка Авторский тмн")
def test_tmn_header_avtorskiy(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_avtorskiy_from_header()


@allure.title("Проверка Колумб тмн")
def test_tmn_header_kolumb(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_kolumb_from_header()


@allure.title("Проверка Сердце Сибири тмн")
def test_tmn_header_sersib(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_sersib_from_header()


@allure.title("Проверка Домашний тмн")
def test_tmn_header_domashniy(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.check_domashniy_from_header()


@allure.title("Проверка Сибирский сад ект")
def test_tmn_header_sibsad(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.check_sibsad_from_header()
