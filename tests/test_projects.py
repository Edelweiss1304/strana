from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import allure


@allure.title("Переход из проектов в WOW")
def test_projects_wow(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.click_projects()
    pp.click_wow()
    assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"


@allure.title("Переход из проектов в Озерный")
def test_projects_ozerniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.click_projects()
    pp.click_ozerniy()
    assert head.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"


@allure.title("Переход из проектов в Днв")
def test_projects_dnv(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.click_projects()
    pp.click_dnv()
    assert head.get_project_dnv_check() == "Санкт-Петербург"


@allure.title("Переход из проектов в Принцип")
def test_projects_princip(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.click_projects()
    pp.click_princip()
    assert head.get_project_comfort_tittle() == "ПРИНЦИП"


@allure.title("Переход из проектов в Сибирский сад")
def test_projects_sibsad(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.click_projects()
    pp.click_sibsad()
    assert head.get_project_comfort_tittle() == "Сибирский сад"


@allure.title("Переход из проектов в Звездный")
def test_projects_zvezdniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_zvezdniy()
    assert head.get_project_comfort_tittle() == "Звездный"


@allure.title("Переход из проектов в Юнион")
def test_projects_union(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_union()
    assert head.get_project_comfort_tittle() == "Юнион"


@allure.title("Переход из проектов в Авторский")
def test_projects_avtorskiy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_avtorskiy()
    assert head.get_project_comfort_tittle() == "Авторский"


@allure.title("Переход из проектов в Колумб")
def test_projects_kolumb(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_kolumb()
    assert head.get_project_comfort_tittle() == "Колумб"


@allure.title("Переход из проектов в Сердце Сибири")
def test_projects_sersib(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_sersib()
    assert head.get_project_comfort_tittle() == "Сердце Сибири"


@allure.title("Переход из проектов в Домашний")
def test_projects_domashniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    pp.click_domashniy()
    assert head.get_project_comfort_tittle() == "Домашний"
