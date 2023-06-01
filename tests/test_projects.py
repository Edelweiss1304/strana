from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
from selenium.common.exceptions import StaleElementReferenceException

from selenium.common.exceptions import StaleElementReferenceException


def handle_stale_element_reference(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except StaleElementReferenceException:
            pass

    return wrapper


@allure.title("Переход из проектов в WOW")
@handle_stale_element_reference
def test_projects_wow(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.click_projects()
    pp = ProjectsPage(driver)
    pp.click_wow()
    assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"


@allure.title("Переход из проектов в Озерный")
@handle_stale_element_reference
def test_projects_ozerniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.click_projects()
    driver.refresh()
    pp.click_ozerniy()
    assert head.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"


@allure.title("Переход из проектов в Днв")
@handle_stale_element_reference
def test_projects_dnv(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.click_projects()
    driver.refresh()
    pp.click_dnv()
    assert head.get_project_dnv_check() == "Санкт-Петербург"


@allure.title("Переход из проектов в Принцип")
@handle_stale_element_reference
def test_projects_princip(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.click_projects()
    driver.refresh()
    pp.click_princip()
    assert head.get_project_comfort_tittle() == "ПРИНЦИП"


@allure.title("Переход из проектов в Сибирский сад")
@handle_stale_element_reference
def test_projects_sibsad(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.click_projects()
    driver.refresh()
    pp.click_sibsad()
    assert head.get_project_comfort_tittle() == "Сибирский сад"


@allure.title("Переход из проектов в Звездный")
@handle_stale_element_reference
def test_projects_zvezdniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_zvezdniy()
    assert head.get_project_comfort_tittle() == "Звездный"


@allure.title("Переход из проектов в Юнион")
@handle_stale_element_reference
def test_projects_union(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_union()
    assert head.get_project_comfort_tittle() == "Юнион"


@allure.title("Переход из проектов в Авторский")
@handle_stale_element_reference
def test_projects_avtorskiy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_avtorskiy()
    assert head.get_project_comfort_tittle() == "Авторский"


@allure.title("Переход из проектов в Колумб")
@handle_stale_element_reference
def test_projects_kolumb(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_kolumb()
    assert head.get_project_comfort_tittle() == "Колумб"


@allure.title("Переход из проектов в Сердце Сибири")
@handle_stale_element_reference
def test_projects_sersib(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_sersib()
    assert head.get_project_comfort_tittle() == "Сердце Сибири"


@allure.title("Переход из проектов в Домашний")
@handle_stale_element_reference
def test_projects_domashniy(driver):
    head = Header(driver)
    pp = ProjectsPage(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.click_projects()
    driver.refresh()
    pp.click_domashniy()
    assert head.get_project_comfort_tittle() == "Домашний"
