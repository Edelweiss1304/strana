from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure


@allure.title("Проверка квартир МСК-0")
def test_msk_apart_0(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart_msk_0()


@allure.title("Проверка квартир МСК-1")
def test_msk_apart_1(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart_msk_1()


@allure.title("Проверка квартир МСК-2")
def test_msk_apart_2(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart_msk_2()


@allure.title("Проверка квартир МСК-3")
def test_msk_apart_3(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart_msk_3()


@allure.title("Проверка квартир МСК-4")
def test_msk_apart_4(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_apart_msk_4()
