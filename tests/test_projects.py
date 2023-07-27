from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import time
import testit


@testit.displayName("Проверка WOW")
@testit.description("Проверка перехода в WOW через страницу проектов")
@allure.title("Переход из проектов в WOW")
def test_projects_wow(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.click_projects()
        pp = ProjectsPage(driver)
        pp.click_accept_cookie()
        pp.click_wow()
    with testit.step("Проверяем, что попали на WOW"):
        assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"


@testit.displayName("Проверка Озерный")
@testit.description("Проверка перехода в Озерный через страницу проектов")
@allure.title("Переход из проектов в Озерный")
def test_projects_ozerniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_ozerniy()
    with testit.step("Проверяем, что попали на Озерный"):
        assert head.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"


@testit.displayName("Проверка ДнВ")
@testit.description("Проверка перехода в ДнВ через страницу проектов")
@allure.title("Переход из проектов в Днв")
def test_projects_dnv(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_dnv()
    with testit.step("Проверяем, что попали на ДнВ"):
        assert head.get_project_dnv_check() == "Санкт-Петербург"


@testit.displayName("Проверка Сибирский Сад")
@testit.description("Проверка перехода в Сибирский Сад через страницу проектов")
@allure.title("Переход из проектов в Сибирский сад")
def test_projects_sibsad(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_sibsad()
    with testit.step("Проверяем, что попали на Сибирский Сад"):
        assert head.get_project_comfort_tittle() == "Сибирский сад"


@testit.displayName("Проверка Звездный")
@testit.description("Проверка перехода в Звездный через страницу проектов")
@allure.title("Переход из проектов в Звездный")
def test_projects_zvezdniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_zvezdniy()
    with testit.step("Проверяем, что попали на Звездный"):
        assert head.get_project_comfort_tittle() == "Звездный"


@testit.displayName("Проверка Юнион")
@testit.description("Проверка перехода в Юнион через страницу проектов")
@allure.title("Переход из проектов в Юнион")
def test_projects_union(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_union()
    with testit.step("Проверяем, что попали на Юнион"):
        assert head.get_project_comfort_tittle() == "Юнион"


@testit.displayName("Проверка Авторский")
@testit.description("Проверка перехода в Авторский через страницу проектов")
@allure.title("Переход из проектов в Авторский")
def test_projects_avtorskiy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_avtorskiy()
    with testit.step("Проверяем, что попали на Авторский"):
        assert head.get_project_comfort_tittle() == "Авторский"


@testit.displayName("Проверка Колумб")
@testit.description("Проверка перехода в Колумб через страницу проектов")
@allure.title("Переход из проектов в Колумб")
def test_projects_kolumb(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_kolumb()
    with testit.step("Проверяем, что попали на Колумб"):
        assert head.get_project_comfort_tittle() == "Колумб"


@testit.displayName("Проверка Сердце Сибири")
@testit.description("Проверка перехода в Сердце Сибири через страницу проектов")
@allure.title("Переход из проектов в Сердце Сибири")
def test_projects_sersib(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_sersib()
    with testit.step("Проверяем, что попали на Сердце Сибири"):
        assert head.get_project_comfort_tittle() == "Сердце Сибири"


@testit.displayName("Проверка Домашний")
@testit.description("Проверка перехода в Домашний через страницу проектов")
@allure.title("Переход из проектов в Домашний")
def test_projects_domashniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        pp.click_accept_cookie()
        pp.click_domashniy()
    with testit.step("Проверяем, что попали на Домашний"):
        assert head.get_project_comfort_tittle() == "Домашний"
