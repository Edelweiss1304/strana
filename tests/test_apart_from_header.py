from pages.header_links import Header
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import pytest
import time


@allure.title("Проверка квартир МСК-{index}")
@pytest.mark.parametrize("index", range(5))
def test_msk_apart(driver, index):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_msk'])
    head.move_to_apart()
    link_index = 9 + index
    getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    assert head.get_city_in_apart() == "Москва"
    time.sleep(1)
    assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@allure.title("Проверка квартир ТМН-{index}")
@pytest.mark.parametrize("index", range(5))
def test_tmn_apart(driver, index):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_tmn'])
    head.move_to_apart()
    time.sleep(1)
    link_index = 9 + index
    getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    assert head.get_city_in_apart() == "в Тюмени"
    time.sleep(1)
    assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@allure.title("Проверка квартир ЕКБ-{index}")
@pytest.mark.parametrize("index", range(5))
def test_ekb_apart(driver, index):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_ekb'])
    head.move_to_apart()
    link_index = 9 + index
    getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    assert head.get_city_in_apart() == "в Екатеринбурге"
    time.sleep(1)
    assert getattr(head, f"get_apart_{index}")().value_of_css_property("color") == head.text_color


@allure.title("Проверка квартир СПБ-{index}")
@pytest.mark.parametrize("index", [0, 1])
def test_spb_apart(driver, index):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_spb'])
    head.move_to_apart()
    link_index = 9 + index
    getattr(head, f"click_s_link_wrapper_{link_index}_from_header")()
    assert head.get_city_in_apart() == "Санкт-Петербург"

    if index == 0:
        target_index = 0
    elif index == 1:
        target_index = 3
    elif index == 2:
        target_index = 4
    time.sleep(1)
    assert getattr(head, f"get_apart_{target_index}")().value_of_css_property("color") == head.text_color


@pytest.mark.parametrize("url", [URLS_MAIN['url_ekb'], URLS_MAIN['url_spb']])
@allure.title("Проверка паркинга")
def test_parking_from_header(driver, url):
    head = Header(driver)
    Base.open_page(driver, url)
    head.move_to_apart()
    head.click_s_link_parking_from_header()
    assert head.get_prking_tittle() == "Паркинг"
