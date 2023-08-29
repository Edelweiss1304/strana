from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import time
import testit
from pages.header_menu import Burger


@testit.displayName("Проверка кнопки Проекты в бургере {url}")
@testit.description("Проверка кнопки Проекты в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_projects_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
    with testit.step("Наводимся на меню"):
        time.sleep(1.5)
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на проекты"):
        br.get_projects().click()
    with testit.step("Проверяем, что попали в проекты"):
        assert br.get_projects_tittle() == "Проекты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Квартиры в бургере {url}")
@testit.description("Проверка кнопки Квартиры в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_flats_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на квартиры"):
        br.get_flats().click()
    with testit.step("Проверяем, что попали в подборщик"):
        assert br.get_flats_tittle() == "Подобрать квартиру"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Коммерция в бургере {url}")
@testit.description("Проверка кнопки Коммерция в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_commercial_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("Наводимся на Коммерцию"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Коммерцию"):
        br.get_commercial().click()
    with testit.step("Проверяем, что попали на Коммерцию"):
        assert br.get_projects_tittle() == "Проекты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки ВК в бургере {url}")
@testit.description("Проверка кнопки ВК в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_vk_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на ВК"):
        br.get_vk().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Ппроверяем, что попали в группу ВК Страна Девелопмент"):
        assert driver.current_url == "https://vk.com/strana_com"
        print("Проверяем что попали в ВК")


@testit.displayName("Проверка кнопки ОК в бургере {url}")
@testit.description("Проверка кнопки ОК в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_ok_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на ОК"):
        br.get_ok().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали в Одноклассники Страна Девелопмент"):
        assert driver.current_url == "https://ok.ru/stranacom"
        print("Проверяем что попали в Одноклассники")


@testit.displayName("Проверка кнопки YT в бургере {url}")
@testit.description("Проверка кнопки YT в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_yt_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на YT"):
        br.get_yt().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на канал Страна Девелопмент"):
        assert driver.current_url == "https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0" \
                                     "%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82"
        print("Проверяем что попали на Ютуб")


@testit.displayName("Проверка кнопки Telegram в бургере {url}")
@testit.description("Проверка кнопки Telegram в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_tg_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        time.sleep(1.5)
    with testit.step("наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Telegram"):
        br.get_tg().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на Telegram Страна Девелопмент"):
        assert driver.current_url == "https://t.me/stranadevelopment"
        print("Проверяем что попали в телеграм")


@testit.displayName("Проверка кнопки новости в бургере {url}")
@testit.description("Проверка кнопки новости в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_news_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на новости"):
        br.get_news().click()
    with testit.step("Проверяем заголовок"):
        assert br.get_news_tittle() == "Новости"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Компания в бургере {url}")
@testit.description("Проверка кнопки Компания в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_company_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем О компании"):
        br.get_company().click()
    with testit.step("Проверяем, что попали на страницу О компании"):
        assert br.get_company_tittle() == "О компании"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Способы покупки в бургере {url}")
@testit.description("Проверка кнопки Способы покупки в бургере")
@pytest.mark.parametrize("url",
                         [URLS_MAIN['url_ekb'], URLS_MAIN['url_spb'], URLS_MAIN['url_msk'], URLS_MAIN['url_tmn']])
def test_pm_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Способы покупки"):
        br.get_purchase().click()
    with testit.step("Проверяем, что попали на страницу Способы покупки"):
        assert br.get_purchase_tittle() == "Материнский капитал"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Документы в бургере {url}")
@testit.description("Проверка кнопки Документы в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_docs_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Документы"):
        br.get_documents().click()
    with testit.step("Проверяем, что попали на страницу Документы"):
        assert br.get_documents_tittle() == "Документы"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Вакансии в бургере {url}")
@testit.description("Проверка кнопки Вакансии в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_vacancy_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Вакансии"):
        br.get_vacancy().click()
    with testit.step("Проверяем, что попали на страницу Вакансии"):
        assert br.get_vacancy_tittle().text == "Смотреть вакансии"
    with testit.step("Нажимаем на кнопку Смотреть вакансии"):
        br.get_vacancy_tittle().click()
    with testit.step("Проверяем, что кнопка нажалась"):
        assert br.get_vacancy_search() == "Любое направление"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Страна.Бонус в бургере {url}")
@testit.description("Проверка кнопки Страна.Бонус в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_bonus_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Страна.Бонус"):
        br.get_bonus().click()
    with testit.step("Проверяем, что попали на страницу Страна.Бонус"):
        assert br.get_bonus_tittle() == ".БОНУС"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Инвесторам в бургере {url}")
@testit.description("Проверка кнопки Инвесторам в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_investors_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Инвесторам"):
        br.get_investors().click()
    with testit.step("Проверяем, что попали на страницу Инвесторам"):
        assert br.get_investors_tittle() == "Инвесторам"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Партнерам в бургере {url}")
@testit.description("Проверка кнопки Партнерам в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_partners_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Партнерам"):
        br.get_partners().click()
    with testit.step("Проверяем, что попали на страницу Партнерам"):
        assert br.get_partners_tittle() == "Партнеры"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Тендеры в бургере {url}")
@testit.description("Проверка кнопки Тендеры в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_tenders_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на тендеры"):
        br.get_tenders().click()
        time.sleep(1)
    with testit.step("Проверяем, что попали на страницу Тендеры"):
        assert driver.current_url == "https://tender.strana.com/"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Контакты в бургере {url}")
@testit.description("Проверка кнопки Контакты в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_contacts_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Контакты"):
        br.get_contacts().click()
    with testit.step("Проверяем, что попали на страницу Контакты"):
        assert br.get_contacts_tittle() == "Контакты"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Акции в бургере {url}")
@testit.description("Проверка кнопки Акции в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_actions_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Акции"):
        br.get_offers().click()
    with testit.step("Проверяем заголовок"):
        assert br.get_offers_tittle() == "Акции"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки Ход строительства в бургере {url}")
@testit.description("Проверка кнопки Ход строительства в бургере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_progress_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Ход строительства"):
        br.get_progress().click()
    with testit.step("Проверяем заголовок"):
        assert br.get_progress_tittle() == "Ход строительства"
        print("Проверяем заголовок")


@testit.displayName("Проверка кнопки SALE % в бургере {url}")
@testit.description("Проверка кнопки SALE % в бургере")
@pytest.mark.parametrize("url",
                         [URLS_MAIN['url_ekb'], URLS_MAIN['url_spb'], URLS_MAIN['url_msk'], URLS_MAIN['url_tmn']])
def test_sale_from_header_menu(driver, url):
    br = Burger(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base = Base(driver)
        base.click_accept_city()
        time.sleep(1.5)
    with testit.step("Наводимся на меню"):
        br.actions.move_to_element(br.get_menu_button()).perform()
    with testit.step("Кликаем на Способы покупки"):
        br.get_sale().click()
    with testit.step("Проверяем, что попали на страницу Способы покупки"):
        assert br.get_flats_tittle() == "Подобрать квартиру"
        print("Проверяем заголовок")
