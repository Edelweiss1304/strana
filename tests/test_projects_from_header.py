from base.base_class import Base
from pages.url import URLS_MAIN
import testit
from pages.to_projects_from_header import ProjectsFromHeader


@testit.displayName("Проверка WOW в выпадающем меню")
@testit.description("Проверка перехода в WOW через хэдер")
def test_msk_header_wow(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на WOW"):
        pfh.get_wow().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"


@testit.displayName("Проверка Озерный в выпадающем меню")
@testit.description("Проверка перехода в Озерный через хэдер")
def test_msk_header_ozerniy(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Страна.Озерная"):
        pfh.get_ozernaya().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"


@testit.displayName("Проверка ДнВ в выпадающем меню")
@testit.description("Проверка перехода в ДнВ через хэдер")
def test_spb_header_dnv(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Дом на Васильевском"):
        pfh.get_dnv().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_dnv_tittle() == "Санкт-Петербург"


@testit.displayName("Проверка Звездный в выпадающем меню")
@testit.description("Проверка перехода в Звездный через хэдер")
def test_tmn_header_zvezdniy(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Звездный"):
        pfh.get_zvezdiy().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Звездный"


@testit.displayName("Проверка Юнион в выпадающем меню")
@testit.description("Проверка перехода в Юнион через хэдер")
def test_tmn_header_union(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Юнион"):
        pfh.get_union().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Юнион"


@testit.displayName("Проверка Авторский в выпадающем меню")
@testit.description("Проверка перехода в Авторский через хэдер")
def test_tmn_header_avtorskiy(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Авторский"):
        pfh.get_avtorskiy().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Авторский"


@testit.displayName("Проверка Сердце Сибири в выпадающем меню")
@testit.description("Проверка перехода в Сердце Сибири через хэдер")
def test_tmn_header_sersib(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Сердце Сибири"):
        pfh.get_sersib().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Сердце Сибири"


@testit.displayName("Проверка Домашний в выпадающем меню")
@testit.description("Проверка перехода в Домашний через хэдер")
def test_tmn_header_domashniy(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Домашний"):
        pfh.get_domashniy().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Домашний"


@testit.displayName("Проверка ЕБ 2.0 в выпадающем меню")
@testit.description("Проверка перехода в ЕБ 2.0 через хэдер")
def test_tmn_header_eb(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Европейский Берег 2.0"):
        pfh.get_eb2().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Европейский берег 2.0"


@testit.displayName("Проверка Сибирский Сад в выпадающем меню")
@testit.description("Проверка перехода в Сибирский Сад через хэдер")
def test_tmn_header_sibsad(driver):
    pfh = ProjectsFromHeader(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
    with testit.step("Наводимся на проекты"):
        pfh.actions.move_to_element(pfh.get_projects_button()).perform()
    with testit.step("Кликаем на Сибирский сад"):
        pfh.get_sibsad().click()
    with testit.step("Проверяем заголовок"):
        assert pfh.get_project_comfort_tittle() == "Сибирский сад"
