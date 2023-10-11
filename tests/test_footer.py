from base.base_class import Base
from pages.footer import Footer
from pages.url import URLS_MAIN
import pytest
import testit
import time


@testit.displayName("Проверка кнопки VK в футере {url}")
@testit.description("Проверка кнопки VK в футере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_vk_footer(driver, url):
    ft = Footer(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на иконку ВК в футере"):
        ft.get_vk().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Ппроверяем, что попали в группу ВК Страна Девелопмент"):
        assert driver.current_url == "https://vk.com/strana_com"
        print("Проверяем что попали в ВК")


@testit.displayName("Проверка кнопки YT в футере {url}")
@testit.description("Проверка кнопки YT в футере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_yt_footer(driver, url):
    ft = Footer(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на иконку YT в футере"):
        ft.get_yt().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на канал Страна Девелопмент"):
        assert driver.current_url == "https://www.youtube.com/c/%D0%A1%D0%A2%D0%A0%D0%90%D0%9D%D0%90%D0%94%D0%B5%D0%B2%D0%B5%D0%BB%D0%BE%D0%BF%D0%BC%D0%B5%D0%BD%D1%82/"
        print("Проверяем что попали на Ютуб")


@testit.displayName("Проверка кнопки OK в футере {url}")
@testit.description("Проверка кнопки OK в футере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_ok_footer(driver, url):
    ft = Footer(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на иконку OK в футере"):
        ft.get_ok().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали в Одноклассники Страна Девелопмент"):
        assert driver.current_url == "https://ok.ru/stranacom"
        print("Проверяем что попали в Одноклассники")


@testit.displayName("Проверка кнопки tg в футере {url}")
@testit.description("Проверка кнопки tg в футере")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_tg_footer(driver, url):
    ft = Footer(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
    with testit.step("Нажимаем на иконку tg в футере"):
        ft.get_tg().click()
        next_tab_index = (driver.window_handles.index(driver.current_window_handle) + 1) % len(driver.window_handles)
        driver.switch_to.window(driver.window_handles[next_tab_index])
    with testit.step("Проверяем, что попали на Telegram Страна Девелопмент"):
        assert driver.current_url == "https://t.me/strana_com"
        print("Проверяем что попали в телеграм")