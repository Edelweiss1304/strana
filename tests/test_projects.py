import time

from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import testit


@testit.displayName("Проверка WOW")
@testit.description("Проверка перехода в WOW через страницу проектов")
def test_projects_wow(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Кликаем на Проекты"):
        head.click_projects()
        pp = ProjectsPage(driver)
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на WOW"):
        pp.get_wow().click()
    with testit.step("Проверяем, что попали на WOW"):
        assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_wow()).perform()
        driver.execute_script("arguments[0].click();", pp.get_wow_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Озерный")
@testit.description("Проверка перехода в Озерный через страницу проектов")
def test_projects_ozerniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Страна.Озерный"):
        pp.get_ozerniy().click()
    with testit.step("Проверяем, что попали на Озерный"):
        assert head.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_ozerniy()).perform()
        driver.execute_script("arguments[0].click();", pp.get_ozernya_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка ДнВ")
@testit.description("Проверка перехода в ДнВ через страницу проектов")
def test_projects_dnv(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на ДнВ"):
        pp.get_dnv().click()
    with testit.step("Проверяем, что попали на ДнВ"):
        assert head.get_project_dnv_check() == "Санкт-Петербург"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     pp.get_dnv_flats_button().click()
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Сибирский Сад")
@testit.description("Проверка перехода в Сибирский Сад через страницу проектов")
def test_projects_sibsad(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Сибирский сад"):
        pp.get_sibsad().click()
    with testit.step("Проверяем, что попали на Сибирский Сад"):
        assert head.get_project_comfort_tittle() == "Сибирский сад"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_sibsad()).perform()
        driver.execute_script("arguments[0].click();", pp.get_sibsad_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Звездный")
@testit.description("Проверка перехода в Звездный через страницу проектов")
def test_projects_zvezdniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Звездный"):
        pp.get_zvezdniy().click()
    with testit.step("Проверяем, что попали на Звездный"):
        assert head.get_project_comfort_tittle() == "Звездный"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_zvezdniy()).perform()
        driver.execute_script("arguments[0].click();", pp.get_zvezdniy_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Юнион")
@testit.description("Проверка перехода в Юнион через страницу проектов")
def test_projects_union(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Юнион"):
        pp.get_union().click()
    with testit.step("Проверяем, что попали на Юнион"):
        assert head.get_project_comfort_tittle() == "Юнион"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_union()).perform()
        driver.execute_script("arguments[0].click();", pp.get_union_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Авторский")
@testit.description("Проверка перехода в Авторский через страницу проектов")
def test_projects_avtorskiy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Авторский"):
        pp.get_avtorskiy().click()
    with testit.step("Проверяем, что попали на Авторский"):
        assert head.get_project_comfort_tittle() == "Авторский"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_avtorskiy()).perform()
        driver.execute_script("arguments[0].click();", pp.get_avtorskiy_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Сердце Сибири")
@testit.description("Проверка перехода в Сердце Сибири через страницу проектов")
def test_projects_sersib(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Сердце Сибири"):
        pp.get_sersib().click()
    with testit.step("Проверяем, что попали на Сердце Сибири"):
        assert head.get_project_comfort_tittle() == "Сердце Сибири"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_sersib()).perform()
        driver.execute_script("arguments[0].click();", pp.get_sersib_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Домашний")
@testit.description("Проверка перехода в Домашний через страницу проектов")
def test_projects_domashniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Домашний"):
        pp.get_domashniy().click()
    with testit.step("Проверяем, что попали на Домашний"):
        assert head.get_project_comfort_tittle() == "Домашний"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        head.actions.move_to_element(pp.get_domashniy()).perform()
        driver.execute_script("arguments[0].click();", pp.get_domashniy_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка ЕБ 2.0")
@testit.description("Проверка перехода в ЕБ 2.0 через страницу проектов")
def test_projects_eb(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на ЕБ 2.0"):
        pp.get_eb().click()
    with testit.step("Проверяем, что попали на ЕБ 2.0"):
        assert head.get_project_comfort_tittle() == "Европейский берег 2.0"
    with testit.step("Возвращаемся назад"):
        driver.back()
    with testit.step("Кликаем на кнопку квартиры"):
        # head.actions.move_to_element(pp.get_eb()).perform()
        driver.execute_script("arguments[0].scrollIntoView();", pp.get_eb())
        time.sleep(2)
        driver.execute_script("arguments[0].click();", pp.get_eb2_flats_button())
    with testit.step("проверяем, что попали на flats"):
        assert head.get_apart_check() == "Подобрать квартиру"
