from pages.city_change import CityChange
from base.base_class import Base
from pages.url import URLS_MAIN
import testit
import time


@testit.displayName('Проверка переключений городов МО')
@testit.description('Проверка переключения городов в хэдере на главной МО')
def test_header_city_change_mo(driver):
    city = CityChange(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Проверяем, что попали в Москву"):
        assert city.get_city_select_header().text == "Москва"
    with testit.step("Открываем селектор"):
        time.sleep(1.5)
        city.get_city_select_header().click()
    with testit.step("Выбираем Московскую область"):
        city.get_city_header_mo().click()
    with testit.step("Проверяем, что попали в Московскую область"):
        assert city.get_city_select_header().text == "Московская область"


@testit.displayName('Проверка переключений городов СПБ')
@testit.description('Проверка переключения городов в хэдере на главной СПБ')
def test_header_city_change_spb(driver):
    city = CityChange(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Проверяем, что попали в Москву"):
        assert city.get_city_select_header().text == "Москва"
    with testit.step("Открываем селектор"):
        time.sleep(1.5)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        city.get_city_select_header().click()
    with testit.step("Выбираем Санкт-Петербург"):
        city.get_city_header_spb().click()
    with testit.step("Проверяем, что попали в Санкт-Петербург"):
        assert city.get_city_select_header().text == "Санкт-Петербург"


@testit.displayName('Проверка переключений городов ЕКБ')
@testit.description('Проверка переключения городов в хэдере на главной ЕКБ')
def test_header_city_change_ekb(driver):
    city = CityChange(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Проверяем, что попали в Москву"):
        assert city.get_city_select_header().text == "Москва"
    with testit.step("Открываем селектор"):
        time.sleep(1.5)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        city.get_city_select_header().click()
    with testit.step("Выбираем Московскую Екатеринбург"):
        city.get_city_header_ekb().click()
    with testit.step("Проверяем, что попали в Екатеринбург"):
        assert city.get_city_select_header().text == "Екатеринбург"


@testit.displayName('Проверка переключений городов ТМН')
@testit.description('Проверка переключения городов в хэдере на главной ТМН')
def test_header_city_change_tmn(driver):
    city = CityChange(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Проверяем, что попали в Москву"):
        assert city.get_city_select_header().text == "Москва"
    with testit.step("Открываем селектор"):
        time.sleep(1.5)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        city.get_city_select_header().click()
    with testit.step("Выбираем Московскую область"):
        city.get_city_header_tmn().click()
    with testit.step("Проверяем, что попали в Тюмень"):
        assert city.get_city_select_header().text == "Тюмень"


@testit.displayName('Проверка переключений городов НСК')
@testit.description('Проверка переключения городов в хэдере на главной НСК')
def test_header_city_change_nsk(driver):
    city = CityChange(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Проверяем, что попали в Москву"):
        assert city.get_city_select_header().text == "Москва"
    with testit.step("Открываем селектор"):
        time.sleep(1.5)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        city.get_city_select_header().click()
    with testit.step("Выбираем Московскую область"):
        city.get_city_header_nsk().click()
    with testit.step("Проверяем, что попали в Новосибирск"):
        assert city.get_city_select_header().text == "Новосибирск"
