from pages.authorization import Authorization
from base.base_class import Base
import pytest
from pages.lk_broker import Lk
import time
import testit


@testit.displayName("Проверка на уникальность в ЛК брокера")
@testit.description("Проверка на уникальность в ЛК брокера")
def test_uniqueness(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
        auth.login_lk_broker()
        lk.get_uniqueness_button().click()
        lk.get_uniqueness_input().send_keys("9960293757")
        time.sleep(3)
        lk.get_uniqueness_button_popup().click()
        time.sleep(3)
        assert lk.get_result_uniqueness().text == "Уникальный"


@testit.displayName("Проверка на закрепление в ЛК брокера")
@testit.description("Проверка на закрепление в ЛК брокера")
def test_fix(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
        auth.login_lk_broker()
        lk.get_uniqueness_button().click()
        lk.get_uniqueness_input().send_keys("9960293757")
        time.sleep(3)
        lk.get_uniqueness_button_popup().click()
        time.sleep(3)
        assert lk.get_result_uniqueness().text == "Уникальный"
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_city())
        lk.get_uniqueness_city_tmn().click()
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_zk())
        lk.get_uniqueness_zk_domashniy().click()
        lk.get_uniqueness_surname().send_keys("Тестовый")
        lk.get_uniqueness_name().send_keys("Тест")
        lk.get_uniqueness_second_name().send_keys("Тестович")
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_consultation())
        lk.get_uniqueness_consultation_office().click()
        lk.get_uniqueness_comment().send_keys("Тест коммент")
        time.sleep(3)


@testit.displayName("Проверка на закрепление в ЛК брокера через кнопку создать сделку")
@testit.description("Проверка на закрепление в ЛК брокера через кнопку создать сделку")
def test_fix_create_deal(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
        auth.login_lk_broker()
        lk.get_uniqueness_button_deal().click()
        lk.get_uniqueness_input().send_keys("9960293757")
        time.sleep(3)
        lk.get_uniqueness_button_popup().click()
        time.sleep(3)
        assert lk.get_result_uniqueness().text == "Уникальный"
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_city())
        lk.get_uniqueness_city_tmn().click()
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_zk())
        lk.get_uniqueness_zk_domashniy().click()
        lk.get_uniqueness_surname().send_keys("Тестовый")
        lk.get_uniqueness_name().send_keys("Тест")
        lk.get_uniqueness_second_name().send_keys("Тестович")
        driver.execute_script("arguments[0].click();", lk.get_uniqueness_consultation())
        lk.get_uniqueness_consultation_office().click()
        lk.get_uniqueness_comment().send_keys("Тест коммент")
        time.sleep(3)


@testit.displayName("Проверка верхних пунктов меню в ЛК брокера")
@testit.description("Проверка верхних пунктов меню в ЛК брокера")
def test_head_menu(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
    with testit.step("Авторизуемся и проверяем страницу сделки"):
        auth.login_lk_broker()
    with testit.step("Проверяем страницу Клиенты"):
        lk.get_clients().click()
        time.sleep(1)
        assert lk.get_clients_h().text == "Клиенты"
    with testit.step("Проверяем страницу Агенты"):
        lk.get_agents().click()
        time.sleep(1)
        assert lk.get_agents_h().text == "Агенты"
    with testit.step("Проверяем страницу Документы"):
        lk.get_documents().click()
        time.sleep(1)
        assert lk.get_documents_h().text == "Документы"
    with testit.step("Проверяем страницу выбор квартиры"):
        lk.get_apart().click()
        time.sleep(1)
        assert lk.get_apart_h().text == "Выберите ЖК"
    with testit.step("Проверям страницу Календарь"):
        lk.get_calendar().click()
        time.sleep(1)
        assert lk.get_calendar_h().text == "Календарь"
    with testit.step("Проверяем страницу Программа лояльности"):
        lk.get_loyalty().click()
        time.sleep(1)
        assert lk.get_loyalty_h().text == "Программа лояльности"
    with testit.step("Проверяем страницу Взаимодействие"):
        lk.get_interaction().click()
        time.sleep(1)
        assert lk.get_interaction_h().text == "Взаимодействие"
    with testit.step("Проверяем страницу Новости и акции"):
        lk.get_news().click()
        time.sleep(1)
        assert lk.get_news_h().text == "Новости"
