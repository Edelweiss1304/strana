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
        time.sleep(2)
    with testit.step("Проверяем страницу Агенты"):
        lk.get_agents().click()
        time.sleep(3)
        assert lk.get_agents_h().text == "Агенты"
    with testit.step("Проверяем страницу Документы"):
        lk.get_documents().click()
        time.sleep(3)
        assert lk.get_documents_h().text == "Документы"
    with testit.step("Проверяем страницу каталог квартир"):
        lk.get_apart().click()
        time.sleep(3)
        assert lk.get_apart_h().text == "Квартиры"
    with testit.step("Проверям страницу Календарь"):
        lk.get_calendar().click()
        time.sleep(3)
        assert lk.get_calendar_h().text == "Календарь"
    with testit.step("Проверяем страницу Программа лояльности"):
        lk.get_loyalty().click()
        time.sleep(3)
        assert lk.get_loyalty_h().text == "Программа лояльности"
    with testit.step("Проверяем страницу Взаимодействие"):
        lk.get_interaction().click()
        time.sleep(3)
        assert lk.get_interaction_h().text == "Взаимодействие"
    with testit.step("Проверяем страницу Новости и акции"):
        lk.get_news().click()
        time.sleep(3)
        assert lk.get_news_h().text == "Новости"
    with testit.step("Проверяем страницу Шахматка"):
        lk.get_shahmatka().click()
        time.sleep(3)
        assert lk.get_shahmatka_h().text == "Выберите ЖК"


@testit.displayName("Проверка меню для агента в ЛК брокера")
@testit.description("Проверка меню для агента в ЛК брокера")
def test_menu_agent(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
    with testit.step("Авторизуемся как агент"):
        auth.login_lk_broker_agent()
    with testit.step("Проверяем профиль агента"):
        lk.get_menu_button().click()
        lk.get_menu_profile_agent().click()
        assert lk.get_agent_profile_poup_up().text == "Профиль агента"
        lk.get_close_poup_up().click()
        time.sleep(3)
    with testit.step("Проверяем профиль агентства"):
        lk.get_menu_button().click()
        lk.get_menu_profile_agency().click()
        assert lk.get_agency_profile_poup_up().text == "Профиль агентства"
        lk.get_close_poup_up().click()
        time.sleep(3)
    with testit.step("Проверяем программу лояльности"):
        lk.get_menu_button().click()
        lk.get_menu_loyalty_program().click()
        assert lk.get_loyalty_h().text == "Программа лояльности"
        time.sleep(3)
    with testit.step("Проверяем кнопку выхода"):
        lk.get_menu_button().click()
        lk.get_menu_exit().click()
        assert lk.get_menu_exit_check().text == "Вход в кабинет"


@testit.displayName("Проверка меню для агентства в ЛК брокера")
@testit.description("Проверка меню для агентства в ЛК брокера")
def test_menu_agency(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
    with testit.step("Авторизуемся как агентство"):
        auth.login_lk_broker()
    with testit.step("Проверяем профиль представителя"):
        lk.get_menu_button().click()
        lk.get_menu_profile_representative().click()
        assert lk.get_representative_profile_poup_up().text == "Профиль представителя агентства"
        lk.get_close_poup_up().click()
        time.sleep(3)
    with testit.step("Проверяем профиль агентства"):
        lk.get_menu_button().click()
        lk.get_menu_profile_agency().click()
        assert lk.get_agency_profile_poup_up().text == "Профиль агентства"
        lk.get_close_poup_up().click()
        time.sleep(3)
    with testit.step("Проверяем программу лояльности"):
        lk.get_menu_button().click()
        lk.get_menu_loyalty_program().click()
        assert lk.get_loyalty_h().text == "Программа лояльности"
        time.sleep(3)
    with testit.step("Проверяем кнопку выхода"):
        lk.get_menu_button().click()
        lk.get_menu_exit().click()
        assert lk.get_menu_exit_check().text == "Вход в кабинет"


@testit.displayName("Проверка бургер-меню для агентства в ЛК брокера")
@testit.description("Проверка бургер-меню для агентства в ЛК брокера")
def test_burger_menu_agency(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
    with testit.step("Авторизуемся как агентство"):
        auth.login_lk_broker()
        time.sleep(10)
    with testit.step("Проверяем ЧаВО"):
        lk.get_burger_menu_button().click()
        lk.get_burger_faq().click()
        assert lk.get_burger_faq_tittle().text == "Часто задаваемые вопросы"
        time.sleep(2)
    with testit.step("Проверяем сделки"):
        lk.get_burger_menu_button().click()
        time.sleep(2)
        driver.execute_script("arguments[0].click();", lk.get_burger_deals())
        assert auth.get_broker_agent_check().text == "Сделки"
        time.sleep(2)
    with testit.step("Проверяем выбор квартиры"):
        #lk.get_burger_menu_button().click()
        lk.get_burger_flats().click()
        assert lk.get_apart_h().text == "Выберите ЖК"
        time.sleep(2)
    with testit.step("Проверяем новости"):
        lk.get_burger_menu_button().click()
        lk.get_burger_news().click()
        assert lk.get_news_h().text == "Новости"
        time.sleep(2)
    with testit.step("Проверяем программу лояльности"):
        lk.get_burger_menu_button().click()
        lk.get_burger_loyalty().click()
        assert lk.get_loyalty_h().text == "Программа лояльности"
        time.sleep(2)
    with testit.step("Проверяем календарь"):
        lk.get_burger_menu_button().click()
        lk.get_burger_calendar().click()
        assert lk.get_calendar_h().text == "Календарь"
        time.sleep(2)
    with testit.step("Проверяем документы"):
        lk.get_burger_menu_button().click()
        lk.get_burger_documents().click()
        assert lk.get_documents_h().text == "Документы"
        time.sleep(2)
    with testit.step("Проверяем взаимодействие"):
        lk.get_burger_menu_button().click()
        lk.get_burger_interaction().click()
        assert lk.get_interaction_h().text == "Взаимодействие"
        time.sleep(2)
    with testit.step("Проверяем агенты"):
        lk.get_burger_menu_button().click()
        lk.get_burger_agents().click()
        assert lk.get_agents_h().text == "Агенты"
        time.sleep(2)
    with testit.step("Проверяем проекты на сайте"):
        lk.get_burger_menu_button().click()
        lk.get_burger_projects().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_projects_tittle().text == "Новостройки"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем квартиры на сайте"):
        lk.get_burger_flats_site().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_flats_site_tittle().text == "Квартиры"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем коммерцию на сайте"):
        lk.get_burger_commercial().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_commercial_tittle().text == "Коммерческие помещения в других городах"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем проектные документы"):
        lk.get_burger_project_documents().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_project_documents_tittle().text == "Проектные документы"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем контакты"):
        lk.get_burger_contacts().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_contacts_tittle().text == "Контакты"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)


@testit.displayName("Проверка бургер-меню для агента в ЛК брокера")
@testit.description("Проверка бургер-меню для агента в ЛК брокера")
def test_burger_menu_agent(driver):
    url = "https://broker.strana.com/"
    auth = Authorization(driver)
    lk = Lk(driver)
    with testit.step("Открываем страницу авторизации"):
        Base.open_page(driver, url)
        auth.click_first_login_broker_button()
    with testit.step("Авторизуемся как агент"):
        auth.login_lk_broker_agent()
    with testit.step("Проверяем ЧаВО"):
        lk.get_burger_menu_button().click()
        lk.get_burger_faq().click()
        assert lk.get_burger_faq_tittle().text == "Часто задаваемые вопросы"
        time.sleep(2)
    with testit.step("Проверяем сделки"):
        lk.get_burger_menu_button().click()
        lk.get_burger_deals().click()
        assert auth.get_broker_agent_check().text == "Сделки"
        time.sleep(2)
    with testit.step("Проверяем выбор квартиры"):
        lk.get_burger_menu_button().click()
        lk.get_burger_flats().click()
        assert lk.get_apart_h().text == "Выберите ЖК"
        time.sleep(2)
    with testit.step("Проверяем новости"):
        lk.get_burger_menu_button().click()
        lk.get_burger_news().click()
        assert lk.get_news_h().text == "Новости"
        time.sleep(2)
    with testit.step("Проверяем программу лояльности"):
        lk.get_burger_menu_button().click()
        lk.get_burger_loyalty().click()
        assert lk.get_loyalty_h().text == "Программа лояльности"
        time.sleep(2)
    with testit.step("Проверяем календарь"):
        lk.get_burger_menu_button().click()
        lk.get_burger_calendar().click()
        assert lk.get_calendar_h().text == "Календарь"
        time.sleep(2)
    with testit.step("Проверяем документы"):
        lk.get_burger_menu_button().click()
        lk.get_burger_documents().click()
        assert lk.get_documents_h().text == "Документы"
        time.sleep(2)
    with testit.step("Проверяем взаимодействие"):
        lk.get_burger_menu_button().click()
        lk.get_burger_interaction().click()
        assert lk.get_interaction_h().text == "Взаимодействие"
        time.sleep(2)
    with testit.step("Проверяем проекты на сайте"):
        lk.get_burger_menu_button().click()
        lk.get_burger_projects().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_projects_tittle().text == "Новостройки"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем квартиры на сайте"):
        lk.get_burger_flats_site().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_flats_site_tittle().text == "Квартиры"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем коммерцию на сайте"):
        lk.get_burger_commercial().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_commercial_tittle().text == "Коммерческие помещения в других городах"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем проектные документы"):
        lk.get_burger_project_documents().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_project_documents_tittle().text == "Проектные документы"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    with testit.step("Проверяем контакты"):
        lk.get_burger_contacts().click()
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        assert lk.get_burger_contacts_tittle().text == "Контакты"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



