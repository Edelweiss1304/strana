from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
from selenium.webdriver.common.by import By
import pytest
import time
import testit


@testit.displayName("Проверка кнопки Проекты в меню")
@testit.description("Проверка кнопки Проекты в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Проекты в меню")
def test_projects_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(7)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(4)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(8)

        else:
            locator = Base.get_s_link_wrapper_locator(9)
    with testit.step("Кликаем на проекты"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали в проекты"):
        assert head.get_projects_check() == "Проекты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Квартиры в меню")
@testit.description("Проверка кнопки Квартиры в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Квартиры в меню")
def test_aparts_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(8)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(5)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(9)

        else:
            locator = Base.get_s_link_wrapper_locator(10)

    with testit.step("Кликаем на квартиры"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали в подборщик"):
        assert head.get_apart_check() == "Подобрать квартиру"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Коммерция в меню")
@testit.description("Проверка кнопки Коммерция в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Коммерция в меню")
def test_commercial_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на Коммерцию"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(9)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(6)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(10)

        else:
            locator = Base.get_s_link_wrapper_locator(11)
    with testit.step("Кликаем на Коммерцию"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на Коммерцию"):
        assert head.get_projects_check() == "Проекты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки ВК в меню")
@testit.description("Проверка кнопки ВК в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки ВК в меню")
def test_vk_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(10)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(7)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(11)

        else:
            locator = Base.get_s_link_wrapper_locator(12)

    with testit.step("Кликаем на ВК"):
        driver.execute_script("arguments[0].click();", Base.get_element_visibility(driver, (By.XPATH, locator)))
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Ппроверяем, что попали в группу ВК Страна Девелопмент"):
        assert driver.current_url == "https://vk.com/strana_com"
        print("Проверяем что попали в ВК")


@testit.displayName("Проверка кнопки ОК в меню")
@testit.description("Проверка кнопки ОК в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки OK в меню")
def test_ok_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(11)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(8)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(12)

        else:
            locator = Base.get_s_link_wrapper_locator(13)

    with testit.step("Кликаем на ОК"):
        driver.execute_script("arguments[0].click();", Base.get_element_visibility(driver, (By.XPATH, locator)))
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали в Одноклассники Страна Девелопмент"):
        assert driver.current_url == "https://ok.ru/stranacom"
        print("Проверяем что попали в Одноклассники")


@testit.displayName("Проверка кнопки YT в меню")
@testit.description("Проверка кнопки YT в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки YT в меню")
def test_yt_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(12)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(9)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(13)

        else:
            locator = Base.get_s_link_wrapper_locator(14)

    with testit.step("Кликаем на YT"):
        driver.execute_script("arguments[0].click();", Base.get_element_visibility(driver, (By.XPATH, locator)))
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на канал Страна Девелопмент"):
        assert driver.current_url == "https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0" \
                                     "%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82"
        print("Проверяем что попали на Ютуб")


@testit.displayName("Проверка кнопки Telegram в меню")
@testit.description("Проверка кнопки Telegram в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Telegram в меню")
def test_tg_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(13)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(10)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(14)

        else:
            locator = Base.get_s_link_wrapper_locator(15)

    with testit.step("Кликаем на Telegram"):
        driver.execute_script("arguments[0].click();", Base.get_element_visibility(driver, (By.XPATH, locator)))
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на Telegram Страна Девелопмент"):
        assert driver.current_url == "https://t.me/stranadevelopment"
        print("Проверяем что попали на Ютуб")


# @pytest.mark.parametrize("url", URLS_MAIN.values())
# @allure.title("Проверка кнопки Новости в меню")
# def test_news_from_header_menu(driver, url):
#     head = Header(driver)
#     Base.open_page(driver, url)
#     time.sleep(2)
#     head.actions.move_to_element(head.get_menu_button()).perform()
#
#     if url == 'https://mo.strana.com':
#         locator = Base.get_s_link_wrapper_locator(19)
#
#     elif url == 'https://nsk.strana.com':
#         locator = Base.get_s_link_wrapper_locator(16)
#
#     else:
#         locator = Base.get_s_link_wrapper_locator(21)
#
#     Base.get_element_visibility(driver, (By.XPATH, locator)).click()
#     assert head.get_news_tittle() == "Новости Страны"
#     print("Проверяем заголовок")

@testit.displayName("Проверка кнопки Компания в меню")
@testit.description("Проверка кнопки Компания в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Компания в меню")
def test_company_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(14)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(11)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(15)

        else:
            locator = Base.get_s_link_wrapper_locator(16)

    with testit.step("Кликаем О компании"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу О компании"):
        assert head.get_about_check() == "О компании"
        print("Проверяем заголовок")
