

from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import testit
import time


@testit.displayName("Проверка WOW")
@testit.description("Проверка перехода в WOW через страницу проектов")
def test_projects_wow(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на Проекты"):
        head.click_projects()
        pp = ProjectsPage(driver)
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на WOW"):
        driver.execute_script("arguments[0].click();", pp.get_wow())
    with testit.step("Проверяем, что попали на WOW"):
        assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_wow()).perform()
    #     head.actions.move_to_element(pp.get_wow_flats_button()).perform()
    #     time.sleep(2)
    #     driver.execute_script("arguments[0].click();", pp.get_wow_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Озерный")
@testit.description("Проверка перехода в Озерный через страницу проектов")
def test_projects_ozerniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Страна.Озерный"):
        driver.execute_script("arguments[0].click();", pp.get_ozerniy())
    with testit.step("Проверяем, что попали на Озерный"):
        assert head.get_project_business_tittle() == "Оазис спокойствия в мегаполисе"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_ozerniy()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_ozernya_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


# @testit.displayName("Проверка ДнВ")
# @testit.description("Проверка перехода в ДнВ через страницу проектов")
# def test_projects_dnv(driver):
#     head = Header(driver)
#     pp = ProjectsPage(driver)
#     with testit.step("Открываем главную страницу"):
#         Base.open_page(driver, URLS_MAIN['url_spb'])
#         base_inst = Base(driver)
#         base_inst.click_accept_city()
#     with testit.step("Кликаем на проекты"):
#         head.click_projects()
#         pp.get_accept_cookie().click()
#     with testit.step("Кликаем на ДнВ"):
#         pp.get_dnv().click()
#     with testit.step("Проверяем, что попали на ДнВ"):
#         assert head.get_project_dnv_check() == "Санкт-Петербург"
#     # with testit.step("Возвращаемся назад"):
#     #     driver.back()
#     # with testit.step("Кликаем на кнопку квартиры"):
#     #     pp.get_dnv_flats_button().click()
#     # with testit.step("проверяем, что попали на flats"):
#     #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Сибирский Сад")
@testit.description("Проверка перехода в Сибирский Сад через страницу проектов")
def test_projects_sibsad(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Сибирский сад"):
        driver.execute_script("arguments[0].click();", pp.get_sibsad())
    with testit.step("Проверяем, что попали на Сибирский Сад"):
        assert head.get_project_comfort_tittle() == "ЖК\nСибирский сад"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_sibsad()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_sibsad_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Звездный")
@testit.description("Проверка перехода в Звездный через страницу проектов")
def test_projects_zvezdniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Звездный"):
        driver.execute_script("arguments[0].click();", pp.get_zvezdniy())
    with testit.step("Проверяем, что попали на Звездный"):
        assert head.get_project_comfort_tittle() == "ЖК\nЗвездный"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_zvezdniy()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_zvezdniy_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Юнион")
@testit.description("Проверка перехода в Юнион через страницу проектов")
def test_projects_union(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Юнион"):
        driver.execute_script("arguments[0].click();", pp.get_union())
    with testit.step("Проверяем, что попали на Юнион"):
        assert head.get_project_comfort_tittle() == "ЖК\nЮнион"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_union()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_union_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Авторский")
@testit.description("Проверка перехода в Авторский через страницу проектов")
def test_projects_avtorskiy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Авторский"):
        driver.execute_script("arguments[0].click();", pp.get_avtorskiy())
    with testit.step("Проверяем, что попали на Авторский"):
        assert head.get_project_comfort_tittle() == "ЖК\nАвторский"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_avtorskiy()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_avtorskiy_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Сердце Сибири")
@testit.description("Проверка перехода в Сердце Сибири через страницу проектов")
def test_projects_sersib(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Сердце Сибири"):
        driver.execute_script("arguments[0].click();", pp.get_sersib())
    with testit.step("Проверяем, что попали на Сердце Сибири"):
        assert head.get_project_comfort_tittle() == "ЖК\nСердце Сибири"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_sersib()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_sersib_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка Домашний")
@testit.description("Проверка перехода в Домашний через страницу проектов")
def test_projects_domashniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        time.sleep(1)
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на Домашний"):
        driver.execute_script("arguments[0].click();", pp.get_domashniy())
    with testit.step("Проверяем, что попали на Домашний"):
        assert head.get_project_comfort_tittle() == "ЖК\nДомашний"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_domashniy()).perform()
    #     driver.execute_script("arguments[0].click();", pp.get_domashniy_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"


@testit.displayName("Проверка ЕБ 2.0")
@testit.description("Проверка перехода в ЕБ 2.0 через страницу проектов")
def test_projects_eb(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        base_inst = Base(driver)
        base_inst.click_accept_city()
    with testit.step("Кликаем на проекты"):
        head.click_projects()
        pp.get_accept_cookie().click()
    with testit.step("Кликаем на ЕБ 2.0"):
        driver.execute_script("arguments[0].click();", pp.get_eb())
    with testit.step("Проверяем, что попали на ЕБ 2.0"):
        assert head.get_project_comfort_tittle() == "ЖК\nЕвропейский берег 2.0"
    # with testit.step("Возвращаемся назад"):
    #     driver.back()
    # with testit.step("Кликаем на кнопку квартиры"):
    #     head.actions.move_to_element(pp.get_eb()).perform()
    #     time.sleep(2)
    #     driver.execute_script("arguments[0].click();", pp.get_eb2_flats_button())
    # with testit.step("проверяем, что попали на flats"):
    #     assert head.get_apart_check() == "Подобрать квартиру"
