from pages.header_links import Header
from pages.projects_page import ProjectsPage
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
from selenium.common.exceptions import StaleElementReferenceException


def rerun_on_StaleElementReferenceException(func):
    def wrapper(*args, **kwargs):
        for _ in range(5):  # Максимальное число попыток
            try:
                return func(*args, **kwargs)  # Пытаемся выполнить тест
            except StaleElementReferenceException:  # Если возникает StaleElementReferenceException, перезапускаем тест
                continue
        raise  # Если после всех попыток тест все еще не прошел, выбрасываем исключение

    return wrapper


@allure.title("Переход из проектов в WOW")
def test_projects_wow(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.click_projects()
        pp = ProjectsPage(driver)
        pp.click_wow()
        assert head.get_project_business_tittle() == "КАМЕРНЫЙ ДОМ НА БЕРЕГУ МОСКВЫ-РЕКИ"

    run_test()


@allure.title("Переход из проектов в Озерный")
def test_projects_ozerniy(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.click_projects()
        driver.refresh()
        pp.click_ozerniy()
        assert head.get_project_business_tittle() == "ОАЗИС СПОКОЙСТВИЯ В МЕГАПОЛИСЕ"

    run_test()


@allure.title("Переход из проектов в Днв")
def test_projects_dnv(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.click_projects()
        driver.refresh()
        pp.click_dnv()
        assert head.get_project_dnv_check() == "Санкт-Петербург"

    run_test()


@allure.title("Переход из проектов в Принцип")
def test_projects_princip(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.click_projects()
        driver.refresh()
        pp.click_princip()
        assert head.get_project_comfort_tittle() == "ПРИНЦИП"

    run_test()


@allure.title("Переход из проектов в Сибирский сад")
def test_projects_sibsad(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.click_projects()
        driver.refresh()
        pp.click_sibsad()
        assert head.get_project_comfort_tittle() == "Сибирский сад"

    run_test()


@allure.title("Переход из проектов в Звездный")
def test_projects_zvezdniy(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_zvezdniy()
        assert head.get_project_comfort_tittle() == "Звездный"

    run_test()


@allure.title("Переход из проектов в Юнион")
def test_projects_union(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_union()
        assert head.get_project_comfort_tittle() == "Юнион"

    run_test()


@allure.title("Переход из проектов в Авторский")
def test_projects_avtorskiy(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_avtorskiy()
        assert head.get_project_comfort_tittle() == "Авторский"

    run_test()


@allure.title("Переход из проектов в Колумб")
def test_projects_kolumb(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_kolumb()
        assert head.get_project_comfort_tittle() == "Колумб"

    run_test()


@allure.title("Переход из проектов в Сердце Сибири")
def test_projects_sersib(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_sersib()
        assert head.get_project_comfort_tittle() == "Сердце Сибири"

    run_test()


@allure.title("Переход из проектов в Домашний")
def test_projects_domashniy(driver):
    @rerun_on_StaleElementReferenceException
    def run_test():
        head = Header(driver)
        pp = ProjectsPage(driver)
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.click_projects()
        driver.refresh()
        pp.click_domashniy()
        assert head.get_project_comfort_tittle() == "Домашний"

    run_test()
