from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import testit


@testit.displayName("Проверка WOW")
@testit.description("Проверка перехода в WOW через хэдер")
@allure.title("Проверка WOW мск")
def test_msk_header_wow(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_wow_from_header()


@testit.displayName("Проверка Озерный")
@testit.description("Проверка перехода в Озерный через хэдер")
@allure.title("Проверка Озёрный мск")
def test_msk_header_ozerniy(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.check_ozerniy_from_header()


@testit.displayName("Проверка ДнВ")
@testit.description("Проверка перехода в ДнВ через хэдер")
@allure.title("Проверка ДнВ спб")
def test_spb_header_dnv(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_dnv_from_header()


@testit.displayName("Проверка Звездный")
@testit.description("Проверка перехода в Звездный через хэдер")
@allure.title("Проверка Звездный тмн")
def test_tmn_header_zvezdniy(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_zvezdniy_from_header()


@testit.displayName("Проверка Юнион")
@testit.description("Проверка перехода в Юнион через хэдер")
@allure.title("Проверка Юнион тмн")
def test_tmn_header_union(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_union_from_header()


@testit.displayName("Проверка Авторский")
@testit.description("Проверка перехода в Авторский через хэдер")
@allure.title("Проверка Авторский тмн")
def test_tmn_header_avtorskiy(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_avtorskiy_from_header()


@testit.displayName("Проверка Колумб")
@testit.description("Проверка перехода в Колумб через хэдер")
@allure.title("Проверка Колумб тмн")
def test_tmn_header_kolumb(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_kolumb_from_header()


@testit.displayName("Проверка Сердце Сибири")
@testit.description("Проверка перехода в Сердце Сибири через хэдер")
@allure.title("Проверка Сердце Сибири тмн")
def test_tmn_header_sersib(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_sersib_from_header()


@testit.displayName("Проверка Домашний")
@testit.description("Проверка перехода в Домашний через хэдер")
@allure.title("Проверка Домашний тмн")
def test_tmn_header_domashniy(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_domashniy_from_header()


@testit.displayName("Проверка ЕБ 2.0")
@testit.description("Проверка перехода в ЕБ 2.0 через хэдер")
@allure.title("Проверка ЕБ 2.0 тмн")
def test_tmn_header_eb(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_eb_from_header()


@testit.displayName("Проверка Сибирский Сад")
@testit.description("Проверка перехода в Сибирский Сад через хэдер")
@allure.title("Проверка Сибирский сад ект")
def test_tmn_header_sibsad(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_sibsad_from_header()
