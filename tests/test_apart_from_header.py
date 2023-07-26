from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import pytest
import time
import testit


@testit.displayName("Проверка квартир по комнатности МСК-{index}")
@testit.description('Проверяем, что при нажатии на х-комнатную квартиру в хэдере, мы попадаем на выборщик с нужной '
                    'комнатностью.')
@allure.title("Проверка квартир по комнатности МСК-{index}")
@pytest.mark.parametrize("index", range(5))
def test_msk_apart(driver, index):
    head = Header(driver)
    with testit.step("Открываем главную страницу МСК"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.move_to_apart()
    with testit.step("Выбираем комнатность {index}"):
        link_index = 8 + index
        getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    with testit.step("Смотрим, что находимся в выборщике нужного города"):
        assert head.get_city_in_apart() == "Москва"
        time.sleep(1)
    with testit.step("Смотрим, какая комнатность выбрана"):
        assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@testit.description('Проверяем, что при нажатии на х-комнатную квартиру в хэдере, мы попадаем на выборщик с нужной '
                    'комнатностью.')
@testit.displayName("Проверка квартир по комнатности ТМН-{index}")
@allure.title("Проверка квартир ТМН-{index}")
@pytest.mark.parametrize("index", range(5))
def test_tmn_apart(driver, index):
    head = Header(driver)
    with testit.step("Открываем главную страницу ТМН"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.move_to_apart()
    with testit.step("Выбираем комнатность {index}"):
        link_index = 9 + index
        getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    with testit.step("Смотрим, что находимся в выборщике нужного города"):
        assert head.get_city_in_apart() == "в Тюмени"
        time.sleep(1)
    with testit.step("Смотрим, какая комнатность выбрана"):
        assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@testit.description('Проверяем, что при нажатии на х-комнатную квартиру в хэдере, мы попадаем на выборщик с нужной '
                    'комнатностью.')
@testit.displayName("Проверка квартир по комнатности ЕКБ-{index}")
@allure.title("Проверка квартир ЕКБ-{index}")
@pytest.mark.parametrize("index", range(5))
def test_ekb_apart(driver, index):
    head = Header(driver)
    with testit.step("Открываем главную страницу ЕКБ"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.move_to_apart()
    with testit.step("Выбираем комнатность {index}"):
        link_index = 9 + index
        getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    with testit.step("Смотрим, что находимся в выборщике нужного города"):
        assert head.get_city_in_apart() == "в Екатеринбурге"
        time.sleep(1)
    with testit.step("Смотрим, какая комнатность выбрана"):
        assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@testit.description('Проверяем, что при нажатии на х-комнатную квартиру в хэдере, мы попадаем на выборщик с нужной '
                    'комнатностью.')
@testit.displayName("Проверка квартир по комнатности СПБ-{index}")
@allure.title("Проверка квартир СПБ-{index}")
@pytest.mark.parametrize("index", [0])
def test_spb_apart(driver, index):
    head = Header(driver)
    with testit.step("Открываем главную страницу СПБ"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.move_to_apart()
    with testit.step("Выбираем комнатность {index}"):
        link_index = 9 + index
        getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    with testit.step("Смотрим, что находимся в выборщике нужного города"):
        assert head.get_city_in_apart() == "Санкт-Петербург"

        if index == 0:
            target_index = 0
        elif index == 1:
            target_index = 3
        elif index == 2:
            target_index = 4
        time.sleep(1)
    with testit.step("Смотрим, какая комнатность выбрана"):
        assert getattr(head, f"get_apart_{target_index}")().value_of_css_property("color") == head.text_color


@testit.description('Проверяем, что при нажатии на паркинг, мы попадаем на паркинг.')
@testit.displayName("Проверка паркинга")
@pytest.mark.parametrize("url", [URLS_MAIN['url_ekb'], URLS_MAIN['url_spb']])
@allure.title("Проверка паркинга")
def test_parking_from_header(driver, url):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        head.move_to_apart()
    with testit.step("Открываем паркинг"):
        head.click_s_link_parking_from_header()
    with testit.step("Проверяем, что открылся паркинг"):
        assert head.get_prking_tittle() == "Паркинг"
