from pages.header_links import Header
from pages.projects_page import ProjectsPage
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


@testit.displayName("Проверка кнопки новости в меню")
@testit.description("Проверка кнопки новости в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Новости в меню")
def test_news_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(19)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(16)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(20)

        else:
            locator = Base.get_s_link_wrapper_locator(21)
    with testit.step("Кликаем на новости"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем заголовок"):
        assert head.get_news_tittle() == "Новости"
        print("Проверяем заголовок")


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


@testit.displayName("Проверка кнопки Способы покупки в меню")
@testit.description("Проверка кнопки Способы покупки в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_pm_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(15)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(12)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(16)

        else:
            locator = Base.get_s_link_wrapper_locator(17)

    with testit.step("Кликаем на Способы покупки"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Способы покупки"):
        pp = ProjectsPage(driver)
        pp.click_accept_cookie()
        assert head.get_purchase_method_new().text == "Рассчитать ипотеку"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Документы в меню")
@testit.description("Проверка кнопки Документы в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_docs_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(16)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(13)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(17)

        else:
            locator = Base.get_s_link_wrapper_locator(18)

    with testit.step("Кликаем на Документы"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Документы"):
        assert head.get_h1_documents() == "Документы"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Вакансии в меню")
@testit.description("Проверка кнопки Вакансии в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_vacancy_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(17)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(14)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(18)

        else:
            locator = Base.get_s_link_wrapper_locator(19)

    with testit.step("Кликаем на Вакансии"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Вакансии"):
        assert head.get_vacancy_check() == "Работа в Стране Девелопмент"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Страна.Бонус в меню")
@testit.description("Проверка кнопки Страна.Бонус в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_bonus_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(21)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(18)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(22)

        else:
            locator = Base.get_s_link_wrapper_locator(23)

    with testit.step("Кликаем на Страна.Бонус"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Страна.Бонус"):
        assert head.get_bonus() == ".БОНУС"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Инвесторам в меню")
@testit.description("Проверка кнопки Инвесторам в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_investors_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(22)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(19)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(23)

        else:
            locator = Base.get_s_link_wrapper_locator(24)

    with testit.step("Кликаем на Инвесторам"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Инвесторам"):
        assert head.get_investors() == "Инвесторам"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Партнерам в меню")
@testit.description("Проверка кнопки Партнерам в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_partners_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(24)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(21)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(25)

        else:
            locator = Base.get_s_link_wrapper_locator(26)

    with testit.step("Кликаем на Партнерам"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Партнерам"):
        assert head.get_partners() == "Партнеры"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Тендеры в меню")
@testit.description("Проверка кнопки Тендеры в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_tenders_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(25)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(22)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(26)

        else:
            locator = Base.get_s_link_wrapper_locator(27)

    with testit.step("Кликаем на тендеры"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Тендеры"):
        assert head.get_tenders() == "Заключить договор проще, чем ты думаешь"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Контакты в меню")
@testit.description("Проверка кнопки Контакты в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_contacts_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(26)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(23)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(27)

        else:
            locator = Base.get_s_link_wrapper_locator(28)

    with testit.step("Кликаем на Контакты"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем, что попали на страницу Контакты"):
        assert head.get_contacts() == "Контакты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Акции в меню")
@testit.description("Проверка кнопки Акции в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
@allure.title("Проверка кнопки Новости в меню")
def test_actions_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(18)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(15)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(19)

        else:
            locator = Base.get_s_link_wrapper_locator(20)
    with testit.step("Кликаем на Акции"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем заголовок"):
        assert head.get_actions_check() == "Акции"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Ход строительства в меню")
@testit.description("Проверка кнопки Ход строительства в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_progress_from_header_menu(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(2)
    with testit.step("Наводимся на меню"):
        head.actions.move_to_element(head.get_menu_button()).perform()

        if url == 'https://mo.strana.com':
            locator = Base.get_s_link_wrapper_locator(20)

        elif url == 'https://nsk.strana.com':
            locator = Base.get_s_link_wrapper_locator(17)

        elif url == 'https://msk.strana.com':
            locator = Base.get_s_link_wrapper_locator(21)

        else:
            locator = Base.get_s_link_wrapper_locator(22)
    with testit.step("Кликаем на Ход строительства"):
        Base.get_element_visibility(driver, (By.XPATH, locator)).click()
    with testit.step("Проверяем заголовок"):
        assert head.get_progress() == "Ход строительства"
        print("Проверяем заголовок")
