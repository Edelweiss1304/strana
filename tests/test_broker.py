from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
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
        assert lk.get_result_uniqueness().text == "Уникальны"