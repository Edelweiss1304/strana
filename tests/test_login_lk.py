from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import testit
import time


@testit.displayName("Проверка авторизации в ЛК {url}")
@testit.description("Проверка авторизации в ЛК через кнопку входа рядом с избранным")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_client(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        time.sleep(1)
    with testit.step("Нажимаем иконку входа"):
        auth.click_login_lk_button()
    with testit.step("Заполняем телефон"):
        time.sleep(5)
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        time.sleep(10)
        auth.get_login_client_phone_field().send_keys(9198629250)
    with testit.step("Кликаем Получить код"):
        auth.click_get_code_btn()
    with testit.step("Вводим код"):
        auth.get_enter_code_field().send_keys(1313)
    with testit.step("Проверяем, что вошли в ЛК"):
        assert auth.get_check_lk() == "Выбрать квартиру"
        print('Успешный вход в ЛК')


@testit.displayName("Проверка авторизации в ЛК через избранное {url}")
@testit.description("Проверка авторизации в ЛК через кнопку входа через избранное")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_client_favorite(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        time.sleep(1)
    with testit.step("Нажимаем на  избранное"):
        auth.get_favorite_button().click()
    with testit.step("Нажимаем на  вход в ЛК"):
        auth.get_login_from_favorite_button().click()
    with testit.step("Заполняем телефон"):
        tabs = driver.window_handles
        current_index = tabs.index(driver.current_window_handle)
        next_index = (current_index + 1) % len(tabs)
        driver.switch_to.window(tabs[next_index])
        time.sleep(10)
        auth.get_login_client_phone_field().send_keys(9198629250)
    with testit.step("Кликаем Получить код"):
        auth.click_get_code_btn()
    with testit.step("Вводим код"):
        auth.get_enter_code_field().send_keys(1313)
    with testit.step("Проверяем, что вошли в ЛК"):
        assert auth.get_check_lk() == "Выбрать квартиру"
        print('Успешный вход в ЛК')
