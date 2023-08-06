from pages.header_links import Header
from pages.flats import Flats
from base.base_class import Base
from pages.url import URLS_MAIN
import allure
import pytest
import testit


# MSK
@testit.displayName('Проверка кнопки проекты мск')
@testit.description('Проверка кнопки проекты мск')
@allure.title("Проверка кнопки проекты мск")
def test_msk_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_projects()


@allure.title("Проверка кнопки квартиры мск")
@testit.displayName("Проверка кнопки квартиры мск")
@testit.description("Проверка кнопки квартиры мск")
def test_msk_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_apart()


@allure.title("Проверка кнопки помещения мск")
@testit.displayName("Проверка кнопки помещения мск")
@testit.description("Проверка кнопки помещения мск")
def test_msk_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_commercial()


@allure.title("Проверка кнопки акции мск")
@testit.displayName("Проверка кнопки акции мск")
@testit.description("Проверка кнопки акции мск")
def test_msk_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_actions()


@allure.title("Проверка кнопки о нас мск")
@testit.displayName("Проверка кнопки о нас мск")
@testit.description("Проверка кнопки о нас мск")
def test_msk_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_about()


@allure.title("Проверка кнопки способы покупки мск")
@testit.displayName("Проверка кнопки способы покупки мск")
@testit.description("Проверка кнопки способы покупки мск")
def test_msk_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_msk'])
        head.check_purchase_methods()


# @allure.title("Проверка кнопки sale мск")
# @testit.displayName("Проверка кнопки sale мск")
# @testit.description("Проверка кнопки sale мск")
# def test_msk_header_sale(driver):
#     head = Header(driver)
#     with testit.step("Открываем главную страницу"):
#         Base.open_page(driver, URLS_MAIN['url_msk'])
#         head.check_sale()


# MO
@allure.title("Проверка кнопки помещения мо")
@testit.displayName("Проверка кнопки помещения мо")
@testit.description("Проверка кнопки помещения мо")
def test_mo_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        head.check_commercial()


@allure.title("Проверка кнопки акции мо")
@testit.displayName("Проверка кнопки акции мо")
@testit.description("Проверка кнопки акции мо")
def test_mo_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        head.check_actions()


@testit.displayName("Проверка кнопки методы покупки мо")
@testit.description("Проверка кнопки методы покупки мо")
def test_mo_header_purchase_methods(driver):
    head = Header(driver)
    Base.open_page(driver, URLS_MAIN['url_mo'])
    head.check_purchase_methods()


@allure.title("Проверка кнопки о нас мо")
@testit.displayName("Проверка кнопки о нас мо")
@testit.description("Проверка кнопки о нас мо")
def test_mo_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_mo'])
        head.check_about()

    # SPB


@allure.title("Проверка кнопки проекты спб")
@testit.displayName("Проверка кнопки проекты спб")
@testit.description("Проверка кнопки проекты спб")
def test_spb_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_projects()


@allure.title("Проверка кнопки квартиры спб")
@testit.displayName("Проверка кнопки квартиры спб")
@testit.description("Проверка кнопки квартиры спб")
def test_spb_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_apart()


@allure.title("Проверка кнопки помещения спб")
@testit.displayName("Проверка кнопки помещения спб")
@testit.description("Проверка кнопки помещения спб")
def test_spb_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_commercial()


@allure.title("Проверка кнопки акции спб")
@testit.displayName("Проверка кнопки акции спб")
@testit.description("Проверка кнопки акции спб")
def test_spb_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_actions()


@allure.title("Проверка кнопки о нас спб")
@testit.displayName("Проверка кнопки о нас спб")
@testit.description("Проверка кнопки о нас спб")
def test_spb_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_about()


@allure.title("Проверка кнопки методы покупки спб")
@testit.displayName("Проверка кнопки методы покупки спб")
@testit.description("Проверка кнопки методы покупки спб")
def test_spb_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_purchase_methods()


@allure.title("Проверка кнопки sale спб")
@testit.displayName("Проверка кнопки sale спб")
@testit.description("Проверка кнопки sale спб")
def test_spb_header_sale(driver):
    head = Header(driver)
    fl = Flats(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_spb'])
        head.check_sale()

    # EKB


@allure.title("Проверка кнопки проекты екб")
@testit.displayName("Проверка кнопки проекты екб")
@testit.description("Проверка кнопки проекты екб")
def test_ekb_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_projects()


@allure.title("Проверка кнопки квартиры екб")
@testit.displayName("Проверка кнопки квартиры екб")
@testit.description("Проверка кнопки квартиры екб")
def test_ekb_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_apart()


@allure.title("Проверка кнопки помещения екб")
@testit.displayName("Проверка кнопки помещения екб")
@testit.description("Проверка кнопки помещения екб")
def test_ekb_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_commercial()


@allure.title("Проверка кнопки акции екб")
@testit.displayName("Проверка кнопки акции екб")
@testit.description("Проверка кнопки акции екб")
def test_ekb_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_actions()


@allure.title("Проверка кнопки о нас екб")
@testit.displayName("Проверка кнопки о нас екб")
@testit.description("Проверка кнопки о нас екб")
def test_ekb_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_about()


@allure.title("Проверка кнопки методы покупки екб")
@testit.displayName("Проверка кнопки методы покупки екб")
@testit.description("Проверка кнопки методы покупки екб")
def test_ekb_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_purchase_methods()


@allure.title("Проверка кнопки sale екб")
@testit.displayName("Проверка кнопки sale екб")
@testit.description("Проверка кнопки sale екб")
def test_ekb_header_sale(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_ekb'])
        head.check_sale()

    # TMN


@allure.title("Проверка кнопки проекты тмн")
@testit.displayName("Проверка кнопки проекты тмн")
@testit.description("Проверка кнопки проекты тмн")
def test_tmn_header_projects(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_projects()


@allure.title("Проверка кнопки квартиры тмн")
@testit.displayName("Проверка кнопки квартиры тмн")
@testit.description("Проверка кнопки квартиры тмн")
def test_tmn_header_apart(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_apart()


@allure.title("Проверка кнопки помещения тмн")
@testit.displayName("Проверка кнопки помещения тмн")
@testit.description("Проверка кнопки помещения тмн")
def test_tmn_header_commercial(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_commercial()


@allure.title("Проверка кнопки акции тмн")
@testit.displayName("Проверка кнопки акции тмн")
@testit.description("Проверка кнопки акции тмн")
def test_tmn_header_actions(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_actions()


@allure.title("Проверка кнопки о нас тмн")
@testit.displayName("Проверка кнопки о нас тмн")
@testit.description("Проверка кнопки о нас тмн")
def test_tmn_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_about()


@allure.title("Проверка кнопки методы покупки тмн")
@testit.displayName("Проверка кнопки методы покупки тмн")
@testit.description("Проверка кнопки методы покупки тмн")
def test_tmn_header_purchase_methods(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_purchase_methods()


@allure.title("Проверка кнопки sale тмн")
@testit.displayName("Проверка кнопки sale тмн")
@testit.description("Проверка кнопки sale тмн")
def test_tmn_header_sale(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_tmn'])
        head.check_sale()

    # NSK


@allure.title("Проверка кнопки о нас тмн")
@testit.displayName("Проверка кнопки о нас нск")
@testit.description("Проверка кнопки о нас нск")
def test_nsk_header_about(driver):
    head = Header(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, URLS_MAIN['url_nsk'])
        head.check_about()
